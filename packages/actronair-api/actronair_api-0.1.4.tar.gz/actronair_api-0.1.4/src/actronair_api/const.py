"""Constants for the Actron Air package"""

"""Actron Cloud Platform URLS."""
ACP_BASE_URL = "https://nimbus.actronair.com.au"
ACP_GET_AC_SYSTEMS_URL = "/api/v0/client/ac-systems?includeNeo=true"
ACP_GET_AC_SYSTEM_STATUS_URL = (
    "/api/v0/client/ac-systems/status/latest?serial={WCSerial}"
)
ACP_POST_CMD_URL = "/api/v0/client/ac-systems/cmds/send?serial={WCSerial}"
ACP_OAUTH2_AUTHORIZE_URL = "/authorize"
ACP_OAUTH2_TOKEN_URL = "/api/v0/oauth/token"

AUTHORIZATION_HEADER = "Authorization"
