import pytest
import pytest_asyncio
from unittest.mock import AsyncMock, MagicMock
from actronair_api.api import ActronAirApi
from actronair_api.auth import AbstractAuth
from actronair_api.exceptions import ApiException, AuthException
from actronair_api.model import ACSystem, CommandResponse, SystemStatus
from testValues import SYSTEM_STATUS_RESPONSE
from actronair_api.const import (
    ACP_BASE_URL,
    ACP_GET_AC_SYSTEMS_URL,
    ACP_GET_AC_SYSTEM_STATUS_URL,
    ACP_POST_CMD_URL,
)

@pytest_asyncio.fixture
async def mock_auth():
    auth = AsyncMock(spec=AbstractAuth)
    return auth

@pytest.mark.asyncio
async def test_async_getACSystems_success(mock_auth):
    mock_auth.request.return_value.status = 200
    mock_auth.request.return_value.json = AsyncMock(return_value={"systems": []})
    api = ActronAirApi(auth=mock_auth)
    
    result = await api.async_getACSystems()
    
    assert result == ACSystem.extract_ac_systems({"systems": []})
    mock_auth.request.assert_called_once_with("get", ACP_BASE_URL + ACP_GET_AC_SYSTEMS_URL)

@pytest.mark.asyncio
async def test_async_getACSystems_auth_exception(mock_auth):
    mock_auth.request.return_value.status = 401
    api = ActronAirApi(auth=mock_auth)
    
    with pytest.raises(AuthException):
        await api.async_getACSystems()

@pytest.mark.asyncio
async def test_async_getACSystems_api_exception(mock_auth):
    mock_auth.request.return_value.status = 500
    api = ActronAirApi(auth=mock_auth)
    
    with pytest.raises(ApiException):
        await api.async_getACSystems()

@pytest.mark.asyncio
async def test_async_getACSystemStatus_success(mock_auth):
    mock_auth.request.return_value.status = 200
    mock_auth.request.return_value.json = AsyncMock(return_value={"status": SYSTEM_STATUS_RESPONSE})
    api = ActronAirApi(auth=mock_auth)
    
    result = await api.async_getACSystemStatus("serial")
    
    assert result == SystemStatus.extract_system_status({"status": SYSTEM_STATUS_RESPONSE})
    mock_auth.request.assert_called_once_with("get", ACP_BASE_URL + ACP_GET_AC_SYSTEM_STATUS_URL.format(WCSerial="serial"))

@pytest.mark.asyncio
async def test_async_sendCommand_success(mock_auth):
    mock_auth.request.return_value.status = 200
    mock_auth.request.return_value.json = AsyncMock(return_value={"response": {}})
    api = ActronAirApi(auth=mock_auth)
    
    result = await api.async_sendCommand("serial", "command")
    
    assert result == CommandResponse.extract_command_response({"response": {}})
    mock_auth.request.assert_called_once_with("post", ACP_BASE_URL + ACP_POST_CMD_URL.format(WCSerial="serial"), json="command")