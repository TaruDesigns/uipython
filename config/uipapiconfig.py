from .settings import settings
from loguru import logger
from UIPathAPI import Configuration, ApiClient
import UIPathAPI
from authlib.integrations.requests_client import OAuth2Session


oauth2_session = OAuth2Session(
    client_id=settings.UIP_CLIENT_ID, client_secret=settings.UIP_CLIENT_SECRET, scope=settings.UIP_SCOPE
)

uipclient_config = Configuration()
uipclient_config.host = settings.get_host()


def FetchUIPathToken(uipclient_config=uipclient_config):
    """Fetch UIPath Access Token.
    Helper function to fetch token and update the "config" setting

    Returns:
        UIPathTokenResponse: Pydantic model with all the parameters from repsonse (access token, expiration)
    """
    logger.info("Refreshing token")
    response = oauth2_session.fetch_token(url=settings.get_auth_url(), grant_type=settings.UIP_GRANT_TYPE)
    tokenresponse = response.get("access_token")
    logger.debug(response)
    # We update the UIPConfig variable
    if uipclient_config is not None:
        uipclient_config.access_token = tokenresponse
    logger.info("Token Updated")
    #return tokenresponse.access_token
    return response

# On application startup, we'll get a new token and add it to uipath api configuration to get everything ready
FetchUIPathToken()




uipclient_folders = UIPathAPI.FoldersApi(ApiClient(uipclient_config))
uipclient_jobs = UIPathAPI.JobsApi(ApiClient(uipclient_config))
uipclient_queueuitems = UIPathAPI.QueueItemsApi(ApiClient(uipclient_config))
uipclient_queueuitemevents = UIPathAPI.QueueItemEventsApi(ApiClient(uipclient_config))
uipclient_queuedefinitions = UIPathAPI.QueueDefinitionsApi(ApiClient(uipclient_config))
uipclient_processes = UIPathAPI.ReleasesApi(ApiClient(uipclient_config))
uipclient_sessions = UIPathAPI.SessionsApi(ApiClient(uipclient_config))