"""All Actron Air Cloud API wrappers in python."""

from .auth import AbstractAuth
from .const import (
    ACP_BASE_URL,
    ACP_GET_AC_SYSTEM_STATUS_URL,
    ACP_GET_AC_SYSTEMS_URL,
    ACP_OAUTH2_AUTHORIZE_URL,
    ACP_OAUTH2_TOKEN_URL,
    ACP_POST_CMD_URL,
)
from .exceptions import ApiException, AuthException
from .model import ACSystem, CommandResponse, SystemStatus


def check_status(status) -> any:
    if status == 401:
        raise AuthException(f"Authorization failed: {status}")
    if status != 200:
        raise ApiException(f"Error request failed: {status}")


class ActronAirApi:
    """ActronAir Cloud Platfrom Connection."""

    def __init__(self, auth: AbstractAuth, retryCount: int = 3):
        self.auth = auth
        self.retryCount = retryCount

    async def async_getACSystems(self) -> list[ACSystem]:
        """ActronAir API to fetch all the AC systems linked to the user account."""
        acSystemsDict = {}
        attemptCounter = 0
        error = None
        while attemptCounter < self.retryCount:
            try:
                attemptCounter += 1
                resp = await self.auth.request(
                    "get", ACP_BASE_URL + ACP_GET_AC_SYSTEMS_URL
                )
                check_status(resp.status)
                acSystemsDict = await resp.json(content_type=None)
                return ACSystem.extract_ac_systems(acSystemsDict)
            except () as excep:
                error = excep
        raise ApiException(
            f"Attempt - {attemptCounter}. Failed to fetch AC Systems due to - {error}"
        )

    async def async_getACSystemStatus(self, serial: str) -> any:
        """Actron Air API to fetch AC system status."""
        attemptCounter = 0
        error = None
        while attemptCounter < self.retryCount:
            try:
                attemptCounter += 1
                resp = await self.auth.request(
                    "get",
                    ACP_BASE_URL + ACP_GET_AC_SYSTEM_STATUS_URL.format(WCSerial=serial),
                )
                check_status(resp.status)
                return SystemStatus.extract_system_status(
                    await resp.json(content_type=None)
                )
            except () as excep:
                error = excep
        raise ApiException(
            f"Attempt - {attemptCounter}. Failed to fetch AC System status due to - {error}"
        )

    async def async_sendCommand(self, serial: str, command: str) -> any:
        """Actron Air API to send command to the AC System/Wall Controller."""
        attemptCounter = 0
        error = None
        while attemptCounter < self.retryCount:
            try:
                attemptCounter += 1
                resp = await self.auth.request(
                    "post",
                    ACP_BASE_URL + ACP_POST_CMD_URL.format(WCSerial=serial),
                    json=command,
                )
                check_status(resp.status)
                return CommandResponse.extract_command_response(
                    await resp.json(content_type=None)
                )
            except () as excep:
                error = excep
        raise ApiException(
            f"Attempt - {attemptCounter}. Failed to send command to the AC System due to - {error}"
        )
