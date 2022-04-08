"""The swatch integration."""
from __future__ import annotations

from .api import SwatchApiClient

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    ATTR_MODEL,
    CONF_URL,
    Platform,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.entity import Entity
from homeassistant.loader import async_get_integration

from .const import ATTR_CLIENT, DOMAIN

# TODO List the platforms that you want to support.
# For your initial PR, limit it to 1 platform.
PLATFORMS: list[Platform] = [Platform.BINARY_SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up swatch from a config entry."""
    # TODO Store an API object for your platforms to access
    # hass.data[DOMAIN][entry.entry_id] = MyApi(...)

    client = SwatchApiClient(entry.data.get(CONF_URL), async_get_clientsession(hass))
    model = f"{(await async_get_integration(hass, DOMAIN)).version}/1.0.0"

    hass.data[DOMAIN][entry.entry_id] = {
        ATTR_CLIENT: client,
        ATTR_MODEL: model,
    }

    hass.config_entries.async_setup_platforms(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok

class SwatchEntity(Entity):  # type: ignore[misc]
    """Base class for Frigate entities."""

    def __init__(self, config_entry: ConfigEntry):
        """Construct a FrigateEntity."""
        Entity.__init__(self)

        self._config_entry = config_entry
        self._available = True

    @property
    def available(self) -> bool:
        """Return the availability of the entity."""
        return self._available

    def _get_model(self) -> str:
        """Get the Frigate device model string."""
        return str(self.hass.data[DOMAIN][self._config_entry.entry_id][ATTR_MODEL])
