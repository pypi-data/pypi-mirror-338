"""evohomeasync provides an async client for the v0 Resideo TCC API."""

from __future__ import annotations

import json
import logging
from abc import ABC, abstractmethod
from functools import cached_property
from http import HTTPMethod, HTTPStatus
from typing import TYPE_CHECKING, Any, Final

import aiohttp
import voluptuous as vol

from . import exceptions as exc
from .const import ERR_MSG_LOOKUP_BASE, HINT_CHECK_NETWORK, HOSTNAME
from .helpers import (
    convert_keys_to_camel_case,
    convert_keys_to_snake_case,
    obscure_secrets,
)

if TYPE_CHECKING:
    from aiohttp.typedefs import StrOrURL


async def _payload(r: aiohttp.ClientResponse | None) -> str | None:
    if r is None:
        return None

    try:
        if r.content_type == "application/json":
            return json.dumps(await r.json())
        if r.content_type == "text/plain":
            return await r.text()
        return await r.text()  # text/html?

    except aiohttp.ClientPayloadError:
        return None
    except aiohttp.ClientError:
        return None


class AbstractAuth(ABC):
    """A class to provide to access the Resideo TCC API."""

    _url_base: StrOrURL

    def __init__(
        self,
        websession: aiohttp.ClientSession,
        /,
        *,
        _hostname: str | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        """A class for interacting with the Resideo TCC API."""

        self.websession: Final = websession

        self._hostname: Final = _hostname or HOSTNAME
        self.logger: Final = logger or logging.getLogger(__name__)

    def __str__(self) -> str:
        """Return a string representation of the object."""
        return f"{self.__class__.__name__}(base='{self.url_base}')"

    @cached_property
    def hostname(self) -> str:
        """Return the hostname used for GET/PUT requests."""
        return self._hostname

    @property
    def url_base(self) -> StrOrURL:
        """Return the URL base used for GET/PUT requests."""
        return self._url_base

    async def get(
        self, url: StrOrURL, /, schema: vol.Schema | None = None
    ) -> dict[str, Any] | list[dict[str, Any]]:
        """Call the vendor's TCC API with a GET.

        Optionally checks the response JSON against the expected schema and logs a
        debug message if it doesn't match.
        """

        response = await self.request(HTTPMethod.GET, url)

        if schema:
            try:
                response = schema(response)
            except vol.Invalid as err:
                self.logger.debug(f"GET {url}: payload may be invalid: {err}")

        return response  # type: ignore[return-value]

    async def put(
        self,
        url: StrOrURL,
        /,
        json: dict[str, Any],
        *,
        schema: vol.Schema | None = None,
    ) -> dict[str, Any] | list[dict[str, Any]]:  # NOTE: not _EvoSchemaT
        """Call the vendor's API with a PUT.

        Optionally checks the payload JSON against the expected schema and logs a
        debug message if it doesn't match.
        """

        if schema:
            try:
                schema(json)
            except vol.Invalid as err:
                self.logger.debug(f"PUT {url}: payload may be invalid: {err}")

        return await self.request(HTTPMethod.PUT, url, json=json)  # type: ignore[return-value]

    async def request(
        self, method: HTTPMethod, url: StrOrURL, /, **kwargs: Any
    ) -> dict[str, Any] | list[dict[str, Any]] | str | None:
        """Make a request to the vendor's TCC RESTful API.

        Converts keys to/from snake_case as required.
        """

        if method == HTTPMethod.PUT and "json" in kwargs:
            kwargs["json"] = convert_keys_to_camel_case(kwargs["json"])

        try:
            response = await self._make_request(method, url, **kwargs)
        except exc.ApiRequestFailedError as err:
            if err.status != HTTPStatus.UNAUTHORIZED:  # 401
                # leave it up to higher layers to handle 401s as they can either be
                # - authentication errors: bad access_token, bad session_id
                # - authorization errors:  bad URL (e.g. no access to that loc_id)
                self.logger.debug(
                    f"The access_token/session_id may be invalid (it shouldn't be): {err}"
                )
            raise

        if self.logger.isEnabledFor(logging.DEBUG):
            self.logger.debug(
                f"{method} {self.url_base}/{url}: {obscure_secrets(response)}"
            )

        if method == HTTPMethod.GET:
            return convert_keys_to_snake_case(response)
        return response

    @abstractmethod
    async def _headers(self, headers: dict[str, str]) -> dict[str, str]:
        """Ensure the authorization header is valid.

        This could take the form of an access token, or a session id.
        """

    async def _make_request(
        self, method: HTTPMethod, url: StrOrURL, /, **kwargs: Any
    ) -> dict[str, Any] | list[dict[str, Any]]:
        """Make a GET/PUT request and return the response (a dict or a list).

        Will raise an exception if the request is not successful.
        """

        rsp: aiohttp.ClientResponse | None = None  # to prevent unbound error

        url = f"{self.url_base}/{url}"
        headers = await self._headers(kwargs.pop("headers", {}))

        try:
            rsp = await self._request(method, url, headers=headers, **kwargs)

            await rsp.read()  # so we can use rsp.json()/rsp.text(), below
            rsp.raise_for_status()

            # can't assert content_length != 0 with aioresponses, so skip that check
            if rsp.content_type != "application/json":  # usu. "text/plain", "text/html"
                raise exc.ApiRequestFailedError(
                    f"{method} {url}: response is not JSON: {await _payload(rsp)}"
                )

            if (response := await rsp.json()) is None:  # an unanticipated edge-case
                raise exc.ApiRequestFailedError(f"{method} {url}: response is null")

        except (aiohttp.ContentTypeError, json.JSONDecodeError) as err:
            raise exc.ApiRequestFailedError(
                f"{method} {url}: response is not valid JSON: {await _payload(rsp)}"
            ) from err

        # An invalid access_token / session_id will cause a 401 and we'd need to
        # re-authenticate; unfortunately, other scenarios cause 401s (e.g. wrong
        # usr_id/loc_id in URL). So leave it up to the consumer to detect/handle
        # such 401s as they can tell if was well-known URL (e.g. without usr_id)

        except aiohttp.ClientResponseError as err:
            if hint := ERR_MSG_LOOKUP_BASE.get(err.status):
                self.logger.error(hint)  # noqa: TRY400

            msg = f"{err.status} {err.message}, response={await _payload(rsp)}"

            raise exc.ApiRequestFailedError(
                f"{method} {url}: {msg}", status=err.status
            ) from err

        except aiohttp.ClientError as err:  # e.g. ClientConnectionError
            self.logger.error(HINT_CHECK_NETWORK)  # noqa: TRY400

            raise exc.ApiRequestFailedError(
                f"{method} {url}: {err}",
            ) from err

        else:
            return response  # type: ignore[no-any-return]

        finally:
            if rsp is not None:
                rsp.release()

    async def _request(  # dev/test wrapper
        self, method: HTTPMethod, url: StrOrURL, /, **kwargs: Any
    ) -> aiohttp.ClientResponse:
        """Wrap the request to the ClientSession (useful for dev/test)."""
        return await self.websession.request(method, url, **kwargs)
