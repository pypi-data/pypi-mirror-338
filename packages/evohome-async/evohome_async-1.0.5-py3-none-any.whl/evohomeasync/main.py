"""evohomeasync provides an async client for the v0 Resideo TCC API."""

from __future__ import annotations

import logging
from http import HTTPStatus
from typing import TYPE_CHECKING, Final

from evohome.helpers import camel_to_snake

from . import exceptions as exc
from .auth import AbstractSessionManager, Auth
from .entities import Location
from .schemas import factory_location_response_list, factory_user_account_info_response

if TYPE_CHECKING:
    import aiohttp

    from .schemas import EvoTcsInfoDictT, EvoUserAccountDictT

SCH_GET_ACCOUNT_INFO: Final = factory_user_account_info_response(camel_to_snake)
SCH_GET_ACCOUNT_LOCS: Final = factory_location_response_list(camel_to_snake)

_LOGGER = logging.getLogger(__name__.rpartition(".")[0])


class EvohomeClient:
    """Provide a client to access the Resideo TCC API."""

    _user_info: EvoUserAccountDictT | None = None
    _user_locs: list[EvoTcsInfoDictT] | None = None  # all locations of the user

    def __init__(
        self,
        session_manager: AbstractSessionManager,
        /,
        *,
        websession: aiohttp.ClientSession | None = None,
        debug: bool = False,
    ) -> None:
        """Construct the v0 EvohomeClient object."""

        self.logger = _LOGGER
        if debug:
            self.logger.setLevel(logging.DEBUG)
            self.logger.debug("Debug mode explicitly enabled via kwarg.")

        self._session_manager = session_manager
        self.auth = Auth(session_manager, websession or session_manager.websession)

        # self.devices: dict[_ZoneIdT, _DeviceDictT] = {}  # dhw or zone by id
        # self.named_devices: dict[_ZoneNameT, _DeviceDictT] = {}  # zone by name

        self._locations: list[Location] | None = None  # to preserve the order
        self._location_by_id: dict[str, Location] | None = None

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(auth='{self.auth}')"

    async def update(
        self,
        /,
        *,
        dont_update_status: bool = False,
        _reset_config: bool = False,  # for use by test suite
    ) -> list[EvoTcsInfoDictT]:
        """Retrieve the latest state of the user's locations.

        If required (or when `_reset_config` was true), first retrieves the user
        information & the configuration of all their locations.

        There is one API call for the user info, and a second for the config/status of
        all the user's locations.

        If `disable_status_update` is true, does not update the status of each location
        hierarchy (note: may have already retrieved the latest version of that data).
        """

        if _reset_config:
            self._user_info = None
            self._user_locs = None

            self._locations = None
            self._location_by_id = None

        if not dont_update_status:
            self._user_locs = None

        if self._user_locs is None:
            await self._get_config()

        assert self._user_locs is not None  # mypy

        if not dont_update_status:  # don't update status of location hierarchy
            assert self._location_by_id
            for loc_entry in self._user_locs:  # each entry is both config & status
                loc_id = str(loc_entry["location_id"])
                self._location_by_id[loc_id]._update_status(loc_entry)

        return self._user_locs

    async def _get_config(self) -> list[EvoTcsInfoDictT]:
        """Ensures the config of the user and their locations.

        If required, first retrieves the user information & installation configuration.
        """

        if self._user_info is None:  # will handle session_id rejection
            url = "accountInfo"
            try:
                self._user_info = await self.auth.get(url, schema=SCH_GET_ACCOUNT_INFO)  # type: ignore[assignment]

            except exc.ApiRequestFailedError as err:  # check if 401 - bad session_id
                if err.status != HTTPStatus.UNAUTHORIZED:  # 401
                    raise

                # as the accountInfo URL is open to all authenticated users, any 401 is
                # due the (albeit valid) session_id being rejected by the server

                self.logger.warning(
                    f"The session_id has been rejected (will re-authenticate): {err}"
                )

                self._session_manager._clear_session_id()
                self._user_info = await self.auth.get(url, schema=SCH_GET_ACCOUNT_INFO)  # type: ignore[assignment]

            assert self._user_info is not None  # mypy

        if self._user_locs is None:
            try:
                user_id = self._user_info["user_id"]
            except (KeyError, TypeError) as err:
                raise exc.BadApiResponseError(
                    f"No user_id in user_info dict. Received: {self._user_info}"
                ) from err

            self._user_locs = await self.auth.get(
                f"locations?userId={user_id}&allData=True", schema=SCH_GET_ACCOUNT_LOCS
            )  # type: ignore[assignment]

            assert self._user_locs is not None  # mypy

        if self._locations is None:
            self._locations = []
            self._location_by_id = {}

            for loc_entry in self._user_locs:  # each entry is both config & status
                loc = Location(loc_entry["location_id"], loc_entry, self)
                self._locations.append(loc)
                self._location_by_id[loc.id] = loc

            #
            #

        return self._user_locs

    @property
    def user_account(self) -> EvoUserAccountDictT:
        """Return the information of the user account."""

        if self._user_info is None:
            raise exc.InvalidConfigError(
                "The account information is not (yet) available"
            )

        return self._user_info

    @property
    def locations(self) -> list[Location]:
        """Return the list of locations."""

        if self._user_locs is None:
            raise exc.InvalidConfigError(
                "The installation information is not (yet) available"
            )

        return self._locations  # type: ignore[return-value]

    @property
    def location_by_id(self) -> dict[str, Location]:
        """Return the list of locations."""

        if self._user_locs is None:
            raise exc.InvalidConfigError(
                "The installation information is not (yet) available"
            )

        return self._location_by_id  # type: ignore[return-value]

    # A significant majority of users will have exactly one TCS, thus for convenience...
    @property
    def tcs(self) -> Location:
        """If there is a single location/TCS, return it, or raise an exception.

        The majority of users will have only one location/TCS.
        """

        if not (locs := self.locations) or len(locs) != 1:
            raise exc.NoSingleTcsError(
                "There is not a single location (only) for this account"
            )

        return locs[0]
