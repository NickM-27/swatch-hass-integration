"""Swatch API Client."""

import asyncio
import logging
import socket
from typing import Any, Dict, List, cast

import aiohttp
import async_timeout
from yarl import URL

TIMEOUT = 10

_LOGGER: logging.Logger = logging.getLogger(__name__)

HEADERS = {"Content-type": "application/json; charset=UTF-8"}

class SwatchApiClient:
    """Swatch API client."""

    def __init__(self, host: str, session: aiohttp.ClientSession) -> None:
        """Construct API Client."""
        self._host = host
        self._session = session

    async def async_get_version(self) -> str:
        """Get data from the API."""
        return cast(
            str,
            await self.api_wrapper(
                "get", str(URL(self._host) / "api/version"), decode_json=False
            ),
        )

    async def async_get_config(self) -> dict[str, Any]:
        """Get data from the API."""
        return cast(
            Dict[str, Any],
            await self.api_wrapper("get", str(URL(self._host) / "api/config")),
        )

    async def async_detect_camera(self, camera_name, image_url) -> dict[str, Any]:
        """Get data from the API."""
        return cast(
            Dict[str, Any],
            await self.api_wrapper("get", str(URL(self._host) / f"api/{camera_name}")),
        )