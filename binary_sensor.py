"""Binary sensor platform for Swatch."""
from __future__ import annotations

import logging
from typing import Any, cast

from homeassistant.components.binary_sensor import (
    DEVICE_CLASS_PRESENCE,
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_URL
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import (
    SwatchEntity,
    get_zones_and_objects,
    get_friendly_name,
    get_swatch_device_identifier,
    get_swatch_entity_unique_id,
)
from .const import ATTR_CONFIG, DOMAIN, NAME

_LOGGER: logging.Logger = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Binary sensor entry setup."""
    swatch_config = hass.data[DOMAIN][entry.entry_id][ATTR_CONFIG]
    async_add_entities(
        [
            SwatchObjectSensor(entry, swatch_config, cam_name, obj)
            for cam_name, obj in get_zones_and_objects(swatch_config)
        ]
    )


class SwatchObjectSensor(SwatchEntity, BinarySensorEntity):  # type: ignore[misc]
    """Swatch Object Sensor class."""

    def __init__(
        self,
        config_entry: ConfigEntry,
        swatch_config: dict[str, Any],
        zone_name: str,
        obj_name: str,
    ) -> None:
        """Construct a new SwatchObjectSensor."""
        self._zone_name = zone_name
        self._obj_name = obj_name
        self._is_on = False
        self._swatch_config = swatch_config

        super().__init__(config_entry)

    @property
    def unique_id(self) -> str:
        """Return a unique ID for this entity."""
        return get_swatch_entity_unique_id(
            self._config_entry.entry_id,
            "object_sensor",
            f"{self._cam_name}_{self._obj_name}",
        )

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device information."""
        return {
            "identifiers": {
                get_swatch_device_identifier(self._config_entry, self._zone_name)
            },
            "via_device": get_swatch_device_identifier(self._config_entry),
            "name": get_friendly_name(self._zone_name),
            "model": self._get_model(),
            "manufacturer": NAME,
        }

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return f"{get_friendly_name(self._zone_name)} {self._obj_name}".title()

    @property
    def is_on(self) -> bool:
        """Return true if the binary sensor is on."""
        return self._is_on

    @property
    def device_class(self) -> str:
        """Return the device class."""
        return cast(str, DEVICE_CLASS_PRESENCE)