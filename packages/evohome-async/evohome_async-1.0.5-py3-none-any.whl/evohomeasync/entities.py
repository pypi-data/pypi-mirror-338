"""Provides handling of TCC v0 entities.

The entity hierarchy is flattened, similar to: Location(TCS) -> DHW | Zone

But here it is implemented as: Location -> Gateway -> TCS -> DHW | Zone
"""

from __future__ import annotations

import logging
from functools import cached_property
from typing import TYPE_CHECKING, Any, Final

from . import exceptions as exc
from .auth import Auth
from .schemas import (
    SZ_DHW_OFF,
    SZ_DHW_ON,
    SZ_HOLD,
    SZ_MODE,
    SZ_NAME,
    SZ_NEXT_TIME,
    SZ_QUICK_ACTION,
    SZ_QUICK_ACTION_NEXT_TIME,
    SZ_SCHEDULED,
    SZ_STATUS,
    SZ_TEMPORARY,
    SZ_THERMOSTAT,
    SZ_VALUE,
    EvoGwyInfoDictT,
    SystemMode,
)

if TYPE_CHECKING:
    import logging
    from datetime import datetime as dt

    # some methods emulate the v2 API...
    from evohomeasync2.schemas.typedefs import EvoTemperatureStatusResponseT

    from . import EvohomeClient
    from .auth import Auth
    from .schemas import (
        EvoDevInfoDictT,
        EvoLocInfoDictT,
        EvoTcsInfoDictT,
        EvoTimeZoneInfoDictT,
        EvoWeatherDictT,
    )


_TEMP_IS_NA: Final = 128


class _EntityBase:
    """Base class for all entities."""

    _config: EvoDevInfoDictT | EvoGwyInfoDictT | EvoLocInfoDictT | EvoTcsInfoDictT
    _status: EvoDevInfoDictT | EvoGwyInfoDictT | EvoLocInfoDictT | EvoTcsInfoDictT

    def __init__(self, entity_id: int, auth: Auth, logger: logging.Logger) -> None:
        self._id: Final = entity_id

        self._auth = auth
        self._logger = logger

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id='{self._id}')"

    @cached_property
    def id(self) -> str:
        return str(self._id)

    @property
    def config(
        self,
    ) -> EvoDevInfoDictT | EvoGwyInfoDictT | EvoLocInfoDictT | EvoTcsInfoDictT:
        """Return the config of the entity."""
        return self._config

    @property
    def status(
        self,
    ) -> EvoDevInfoDictT | EvoGwyInfoDictT | EvoLocInfoDictT | EvoTcsInfoDictT:
        """Return the latest config of the entity."""
        return self._status


class _DeviceBase(_EntityBase):
    """Base class for all devices."""

    _config: EvoDevInfoDictT | EvoGwyInfoDictT
    _status: EvoDevInfoDictT | EvoGwyInfoDictT

    def __init__(
        self, entity_id: int, config: EvoDevInfoDictT, location: Location
    ) -> None:
        super().__init__(entity_id, location._auth, location._logger)

        self._loc = location  # parent

        self._config = config
        self._status = config  # initial state

    def _update_status(self, status: EvoDevInfoDictT | EvoGwyInfoDictT) -> None:
        """Update the device's status."""
        self._status = status


class HotWater(_DeviceBase):  # Hotwater version of a Device
    """Instance of a location's DHW zone."""

    _config: Final[EvoDevInfoDictT]  # type: ignore[misc]
    _status: EvoDevInfoDictT

    # Config attrs...

    @property
    def name(self) -> str:
        return "Domestic Hot Water"

    @property
    def idx(self) -> str:
        return "HW"

    # Status (state) attrs & methods...

    @property  # emulate the v2 API...
    def temperature_status(self) -> EvoTemperatureStatusResponseT:
        """Expose the temperature_status as per the v2 API."""

        if self._status is None:
            raise exc.InvalidStatusError(f"{self} has no state, has it been fetched?")

        temp = self._status[SZ_THERMOSTAT]["indoor_temperature"]
        temp_status = self._status[SZ_THERMOSTAT]["indoor_temperature_status"]

        return {
            "is_available": temp_status == "Measured",
        } | ({} if temp == _TEMP_IS_NA else {"temperature": temp})  # type: ignore[return-value]

    @property
    def temperature(self) -> float | None:
        if not (status := self.temperature_status) or not status["is_available"]:
            return None
        return status["temperature"]

    async def _set_dhw(
        self,
        status: str,  # "Scheduled" | "Hold"
        mode: str | None = None,  # "DHWOn" | "DHWOff"
        next_time: dt | None = None,  # "%Y-%m-%dT%H:%M:%SZ"
    ) -> None:
        """Set DHW to Auto, or On/Off, either indefinitely, or until a set time."""

        data = {
            SZ_STATUS: status,
            SZ_MODE: mode,
            # SZ_NEXT_TIME: None,
            # SZ_SPECIAL_TIMES: None,
            # SZ_HEAT_SETPOINT: None,
            # SZ_COOL_SETPOINT: None,
        }
        if next_time:
            data |= {SZ_NEXT_TIME: next_time.strftime("%Y-%m-%dT%H:%M:%SZ")}

        url = f"devices/{self.id}/thermostat/changeableValues"
        await self._auth.put(url, json=data)

    async def set_dhw_on(self, until: dt | None = None) -> None:
        """Set DHW to On, either indefinitely, or until a specified time.

        When On, the DHW controller will work to keep its target temperature at/above
        its target temperature.  After the specified time, it will revert to its
        scheduled behaviour.
        """

        await self._set_dhw(status=SZ_HOLD, mode=SZ_DHW_ON, next_time=until)

    async def set_dhw_off(self, until: dt | None = None) -> None:
        """Set DHW to Off, either indefinitely, or until a specified time.

        When Off, the DHW controller will ignore its target temperature. After the
        specified time, it will revert to its scheduled behaviour.
        """

        await self._set_dhw(status=SZ_HOLD, mode=SZ_DHW_OFF, next_time=until)

    async def set_dhw_auto(self) -> None:
        """Allow DHW to switch between On and Off, according to its schedule."""
        await self._set_dhw(status=SZ_SCHEDULED)


class Zone(_DeviceBase):  # Zone version of a Device
    """Instance of a location's heating zone."""

    _config: Final[EvoDevInfoDictT]  # type: ignore[misc]
    _status: EvoDevInfoDictT

    # Config attrs...

    @property
    def name(self) -> str:
        return self._config[SZ_NAME]

    @property  # appears to be the zone idx (not in evohomeclientv2)
    def idx(self) -> str:
        return f"{self._config['instance']:02X}"

    @property
    def max_heat_setpoint(self) -> float:
        return self._status[SZ_THERMOSTAT]["min_heat_setpoint"]

    @property
    def min_heat_setpoint(self) -> float:
        return self._status[SZ_THERMOSTAT]["min_heat_setpoint"]

    async def allowed_modes(self) -> tuple[str, ...]:
        """Return the set of modes the zone can be assigned."""
        return tuple(self._config["thermostat"]["allowed_modes"])

    # Status (state) attrs & methods...

    @property  # emulate the v2 API...
    def temperature_status(self) -> EvoTemperatureStatusResponseT:
        """Expose the temperature_status as per the v2 API."""

        if self._status is None:
            raise exc.InvalidStatusError(f"{self} has no state, has it been fetched?")

        temp = self._status[SZ_THERMOSTAT]["indoor_temperature"]
        temp_status = self._status[SZ_THERMOSTAT]["indoor_temperature_status"]

        return {
            "is_available": temp_status == "Measured",
        } | ({} if temp == _TEMP_IS_NA else {"temperature": temp})  # type: ignore[return-value]

    @property
    def temperature(self) -> float | None:
        if not (status := self.temperature_status) or not status["is_available"]:
            return None
        return status["temperature"]

    async def _set_heat_setpoint(
        self,
        status: str,  # "Scheduled" | "Temporary" | "Hold
        value: float | None = None,
        next_time: dt | None = None,  # "%Y-%m-%dT%H:%M:%SZ"
    ) -> None:
        """Set zone setpoint, either indefinitely, or until a set time."""

        if next_time is None:
            data = {SZ_STATUS: SZ_HOLD, SZ_VALUE: value}
        else:
            data = {
                SZ_STATUS: status,
                SZ_VALUE: value,
                SZ_NEXT_TIME: next_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            }

        url = f"devices/{self.id}/thermostat/changeableValues/heatSetpoint"
        await self._auth.put(url, json=data)

    async def set_temperature(
        self, temperature: float, until: dt | None = None
    ) -> None:
        """Override the setpoint of a zone, for a period of time, or indefinitely."""

        if until:
            await self._set_heat_setpoint(
                SZ_TEMPORARY, value=temperature, next_time=until
            )
        else:
            await self._set_heat_setpoint(SZ_HOLD, value=temperature)

    async def set_zone_auto(self) -> None:
        """Set a zone to follow its schedule."""
        await self._set_heat_setpoint(status=SZ_SCHEDULED)


class ControlSystem(_EntityBase):  # TCS portion of a Location
    """Instance of a TCS (a portion of a location)."""

    _cli: EvohomeClient  # proxy for parent

    _config: Final[EvoTcsInfoDictT]  # type: ignore[misc]
    _status: EvoTcsInfoDictT

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.hotwater: HotWater | None = None
        self.zones: list[Zone] = []

        self.zone_by_id: dict[str, Zone] = {}  # id is fixed to zone
        self.zone_by_idx: dict[str, Zone] = {}  #  not sure if fixed, or attr like name

    @property
    def zone_by_name(self) -> dict[str, Zone]:
        """Return the zones by name (names are not fixed attrs)."""
        return {zone.name: zone for zone in self.zones}

    # Status (state) attrs & methods...

    @property
    def one_touch_actions_suspended(self) -> bool:
        return bool(self._status["one_touch_actions_suspended"])

    @property
    def one_touch_buttons(self) -> tuple[str, ...]:
        return tuple(self._status["one_touch_buttons"])

    async def _set_mode(self, mode: dict[str, str]) -> None:
        """Set the TCS mode."""

        await self._auth.put(f"evoTouchSystems?locationId={self.id}", json=mode)

    async def reset(self) -> None:
        """Set the TCS to auto mode (and DHW/all zones to FollowSchedule mode)."""

        raise NotImplementedError

    async def set_mode(self, mode: SystemMode, /, *, until: dt | None = None) -> None:
        """Set the TCS to a mode, either indefinitely, or for a set time."""

        request: dict[str, str] = {SZ_QUICK_ACTION: mode}
        if until:
            request |= {SZ_QUICK_ACTION_NEXT_TIME: until.strftime("%Y-%m-%dT%H:%M:%SZ")}

        await self._set_mode(request)

    async def set_auto(self) -> None:
        """Set the TCS to normal mode."""
        await self.set_mode(SystemMode.AUTO)

    async def set_away(self, /, *, until: dt | None = None) -> None:
        """Set the TCS to away mode."""
        await self.set_mode(SystemMode.AWAY, until=until)

    async def set_custom(self, /, *, until: dt | None = None) -> None:
        """Set the TCS to custom mode."""
        await self.set_mode(SystemMode.CUSTOM, until=until)

    async def set_dayoff(self, /, *, until: dt | None = None) -> None:
        """Set the TCS to dayoff mode."""
        await self.set_mode(SystemMode.DAY_OFF, until=until)

    async def set_eco(self, /, *, until: dt | None = None) -> None:
        """Set the TCS to economy mode."""
        await self.set_mode(SystemMode.AUTO_WITH_ECO, until=until)

    async def set_heatingoff(self, /, *, until: dt | None = None) -> None:
        """Set the system to heating off mode."""
        await self.set_mode(SystemMode.HEATING_OFF, until=until)

    def _get_zone(self, zon_id: int | str) -> Zone:
        """Return the TCS's zone by its id, idx or name."""

        if isinstance(zon_id, int):
            zon_id = str(zon_id)

        dev = self.zone_by_id.get(zon_id)

        if dev is None:
            dev = self.zone_by_idx.get(zon_id)

        if dev is None:
            dev = self.zone_by_name.get(zon_id)

        if dev is None:
            raise exc.ConfigError(f"no zone {zon_id} in {self}")

        return dev

    def _get_dhw(self) -> HotWater:
        """Return the TCS's DHW, if there is one."""

        dev = self.zone_by_id.get("HW")

        if dev is None:
            raise exc.ConfigError(f"no DHW in {self}")

        return dev  # type: ignore[return-value]

    async def get_temperatures(
        self,
        /,
        *,
        dont_update_status: bool = False,
    ) -> dict[str, float | None]:
        """A convenience function to obtain the high-precision temperatures."""

        if not dont_update_status:
            await self._cli.update()

        return {z.id: z.temperature for z in self.zones}


class Gateway(_DeviceBase):  # Gateway portion of a Device
    """Instance of a location's gateway."""

    _config: Final[EvoGwyInfoDictT]  # type: ignore[misc]
    _status: EvoGwyInfoDictT  # initial state

    # list(EvoGwyInfoDictT.__annotations__.keys())

    # Config attrs...

    @property
    def config(self) -> EvoGwyInfoDictT:
        """Return the config of the entity."""
        return {
            k: v
            for k, v in self._config.items()
            if k in list(EvoGwyInfoDictT.__annotations__.keys())
        }  # type: ignore[return-value]

    @property
    def status(self) -> EvoGwyInfoDictT:
        """Return the latest config of the entity."""
        return {
            k: v
            for k, v in self._config.items()
            if k in list(EvoGwyInfoDictT.__annotations__.keys())
        }  # type: ignore[return-value]

    @cached_property
    def mac_address(self) -> str:
        return self._config["mac_id"]


class Location(ControlSystem, _EntityBase):  # assumes 1 TCS per Location
    """Instance of an account's location/TCS."""

    def __init__(
        self, entity_id: int, config: EvoTcsInfoDictT, client: EvohomeClient
    ) -> None:
        super().__init__(entity_id, client.auth, client.logger)

        self._cli = client  # proxy for parent

        self._config: Final[EvoTcsInfoDictT] = config  # type: ignore[misc]
        self._status: EvoTcsInfoDictT = config  # initial state

        self.gateways: list[Gateway] = []
        self.gateway_by_id: dict[str, Gateway] = {}

        # process config["devices"]...
        for dev_config in config["devices"]:
            if str(dev_config["gateway_id"]) not in self.gateway_by_id:
                gwy = Gateway(dev_config["gateway_id"], dev_config, self)

                self.gateways.append(gwy)
                self.gateway_by_id[gwy.id] = gwy

            if (type_ := dev_config["thermostat_model_type"]) == "DOMESTIC_HOT_WATER":
                self.hotwater = HotWater(dev_config["device_id"], dev_config, self)

            # check is string to handle edge-case of Honeywell TH9320WF3003
            elif isinstance(type_, str) and type_.startswith("EMEA_"):
                self._add_zone(Zone(dev_config["device_id"], dev_config, self))

            else:  # assume everything else is a zone
                self._logger.warning(
                    f"{self}: Unknown device type, assuming is a zone: {type_}"
                )
                self._add_zone(Zone(dev_config["device_id"], dev_config, self))

    def _add_zone(self, zone: Zone) -> None:
        self.zones.append(zone)

        self.zone_by_id[zone.id] = zone
        self.zone_by_idx[zone.idx] = zone

    # Config attrs...

    @property
    def country(self) -> str:
        # "GB", "NL"
        return self._config["country"]

    @property
    def name(self) -> str:
        return self._config[SZ_NAME]

    @property
    def dst_enabled(self) -> bool:
        """Return True if the location uses daylight saving time."""
        return self._config["daylight_saving_time_enabled"]

    @property
    def time_zone_info(self) -> EvoTimeZoneInfoDictT:
        return self._config["time_zone"]

    # Status (state) attrs & methods...

    # async def update(self, *args: Any, **kwargs: Any) -> Any:
    #     """Get the latest state of the location and update its status attrs."""
    #     raise NotImplementedError("Use EvohomeClient.update() instead.")

    @property
    def weather(self) -> EvoWeatherDictT:
        return self._config["weather"]

    def _update_status(self, status: EvoTcsInfoDictT) -> None:
        """Update the LOC's status and cascade to its descendants."""

        self._status = status

        for dev_status in status["devices"]:
            if (gwy_id := str(dev_status["gateway_id"])) in self.gateway_by_id:
                self.gateway_by_id[gwy_id]._update_status(dev_status)

            else:
                self._logger.warning(
                    f"{self}: Ignoring gateway_id={gwy_id}"
                    ", (has the location configuration changed?)"
                )
                continue

            if (dev_id := str(dev_status["device_id"])) in self.zone_by_id:
                self.zone_by_id[dev_id]._update_status(dev_status)

            elif self.hotwater and self.hotwater.id == dev_id:
                self.hotwater._update_status(dev_status)

            else:
                self._logger.warning(
                    f"{self}: Ignoring device_id={dev_id}"
                    ", (has the location configuration changed?)"
                )
                continue
