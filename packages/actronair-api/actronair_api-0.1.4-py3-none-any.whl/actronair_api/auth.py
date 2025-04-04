"""abstract auth implementation for Actron Air."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Mapping
import logging
from typing import Any

from aiohttp import ClientError, ClientResponse, ClientSession

from .const import ACP_BASE_URL, AUTHORIZATION_HEADER
from .exceptions import AuthException

_LOGGER = logging.getLogger(__name__)


class AbstractAuth(ABC):
    """Abstract class to make authenticated requests."""

    def __init__(self, websession: ClientSession, host: str) -> None:
        """Initialize the auth."""
        self._websession = websession
        self._host = host if host is not None else ACP_BASE_URL

    @abstractmethod
    async def async_get_access_token(self) -> str:
        """Return a valid access token."""

    async def request(
        self, method: str, url: str, **actronArgs: Mapping[str, Any] | None
    ) -> ClientResponse:
        """Make a request."""
        try:
            access_token = await self.async_get_access_token()
        except ClientError as err:
            raise AuthException(f"Access token failure: {err}") from err
        headers = {AUTHORIZATION_HEADER: f"Bearer {access_token}"}
        if not (url.startswith("https://")):
            url = f"{self._host}{url}"
        _LOGGER.debug("request[%s]=%s %s", method, url, actronArgs.get("params"))
        if method == "post" and "json" in actronArgs:
            _LOGGER.debug("request[post json]=%s", actronArgs["json"])
        return await self._websession.request(
            method, url, **actronArgs, headers=headers
        )
