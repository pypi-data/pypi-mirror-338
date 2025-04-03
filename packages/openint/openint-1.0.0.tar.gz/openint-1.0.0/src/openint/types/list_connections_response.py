# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ListConnectionsResponse",
    "ConnectorsAircallConnectionSettings",
    "ConnectorsAircallConnectionSettingsSettings",
    "ConnectorsAircallConnectionSettingsSettingsOAuth",
    "ConnectorsAircallConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsAircallConnectionSettingsConnector",
    "ConnectorsAircallConnectionSettingsConnectorSchemas",
    "ConnectorsAirtableConnectionSettings",
    "ConnectorsAirtableConnectionSettingsSettings",
    "ConnectorsAirtableConnectionSettingsConnector",
    "ConnectorsAirtableConnectionSettingsConnectorSchemas",
    "ConnectorsApolloConnectionSettings",
    "ConnectorsApolloConnectionSettingsSettings",
    "ConnectorsApolloConnectionSettingsSettingsOAuth",
    "ConnectorsApolloConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsApolloConnectionSettingsSettingsOAuthCredentialsRaw",
    "ConnectorsApolloConnectionSettingsSettingsOAuthConnectionConfig",
    "ConnectorsApolloConnectionSettingsSettingsError",
    "ConnectorsApolloConnectionSettingsConnector",
    "ConnectorsApolloConnectionSettingsConnectorSchemas",
    "ConnectorsBrexConnectionSettings",
    "ConnectorsBrexConnectionSettingsSettings",
    "ConnectorsBrexConnectionSettingsConnector",
    "ConnectorsBrexConnectionSettingsConnectorSchemas",
    "ConnectorsCodaConnectionSettings",
    "ConnectorsCodaConnectionSettingsSettings",
    "ConnectorsCodaConnectionSettingsConnector",
    "ConnectorsCodaConnectionSettingsConnectorSchemas",
    "ConnectorsConfluenceConnectionSettings",
    "ConnectorsConfluenceConnectionSettingsSettings",
    "ConnectorsConfluenceConnectionSettingsSettingsOAuth",
    "ConnectorsConfluenceConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsConfluenceConnectionSettingsConnector",
    "ConnectorsConfluenceConnectionSettingsConnectorSchemas",
    "ConnectorsDiscordConnectionSettings",
    "ConnectorsDiscordConnectionSettingsSettings",
    "ConnectorsDiscordConnectionSettingsSettingsOAuth",
    "ConnectorsDiscordConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsDiscordConnectionSettingsConnector",
    "ConnectorsDiscordConnectionSettingsConnectorSchemas",
    "ConnectorsFacebookConnectionSettings",
    "ConnectorsFacebookConnectionSettingsSettings",
    "ConnectorsFacebookConnectionSettingsSettingsOAuth",
    "ConnectorsFacebookConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsFacebookConnectionSettingsSettingsOAuthCredentialsRaw",
    "ConnectorsFacebookConnectionSettingsSettingsOAuthConnectionConfig",
    "ConnectorsFacebookConnectionSettingsSettingsError",
    "ConnectorsFacebookConnectionSettingsConnector",
    "ConnectorsFacebookConnectionSettingsConnectorSchemas",
    "ConnectorsFinchConnectionSettings",
    "ConnectorsFinchConnectionSettingsSettings",
    "ConnectorsFinchConnectionSettingsConnector",
    "ConnectorsFinchConnectionSettingsConnectorSchemas",
    "ConnectorsFirebaseConnectionSettings",
    "ConnectorsFirebaseConnectionSettingsSettings",
    "ConnectorsFirebaseConnectionSettingsSettingsUnionMember0",
    "ConnectorsFirebaseConnectionSettingsSettingsUnionMember0ServiceAccount",
    "ConnectorsFirebaseConnectionSettingsSettingsUnionMember1",
    "ConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthData",
    "ConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember0",
    "ConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember0UserJson",
    "ConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember1",
    "ConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember2",
    "ConnectorsFirebaseConnectionSettingsSettingsUnionMember1FirebaseConfig",
    "ConnectorsFirebaseConnectionSettingsConnector",
    "ConnectorsFirebaseConnectionSettingsConnectorSchemas",
    "ConnectorsForeceiptConnectionSettings",
    "ConnectorsForeceiptConnectionSettingsSettings",
    "ConnectorsForeceiptConnectionSettingsConnector",
    "ConnectorsForeceiptConnectionSettingsConnectorSchemas",
    "ConnectorsGitHubConnectionSettings",
    "ConnectorsGitHubConnectionSettingsSettings",
    "ConnectorsGitHubConnectionSettingsSettingsOAuth",
    "ConnectorsGitHubConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsGitHubConnectionSettingsConnector",
    "ConnectorsGitHubConnectionSettingsConnectorSchemas",
    "ConnectorsGongConnectionSettings",
    "ConnectorsGongConnectionSettingsSettings",
    "ConnectorsGongConnectionSettingsSettingsOAuth",
    "ConnectorsGongConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsGongConnectionSettingsSettingsOAuthCredentialsRaw",
    "ConnectorsGongConnectionSettingsSettingsOAuthConnectionConfig",
    "ConnectorsGongConnectionSettingsSettingsError",
    "ConnectorsGongConnectionSettingsConnector",
    "ConnectorsGongConnectionSettingsConnectorSchemas",
    "ConnectorsGooglecalendarConnectionSettings",
    "ConnectorsGooglecalendarConnectionSettingsSettings",
    "ConnectorsGooglecalendarConnectionSettingsSettingsOAuth",
    "ConnectorsGooglecalendarConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsGooglecalendarConnectionSettingsConnector",
    "ConnectorsGooglecalendarConnectionSettingsConnectorSchemas",
    "ConnectorsGoogledocsConnectionSettings",
    "ConnectorsGoogledocsConnectionSettingsSettings",
    "ConnectorsGoogledocsConnectionSettingsSettingsOAuth",
    "ConnectorsGoogledocsConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsGoogledocsConnectionSettingsConnector",
    "ConnectorsGoogledocsConnectionSettingsConnectorSchemas",
    "ConnectorsGoogledriveConnectionSettings",
    "ConnectorsGoogledriveConnectionSettingsSettings",
    "ConnectorsGoogledriveConnectionSettingsSettingsOAuth",
    "ConnectorsGoogledriveConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsGoogledriveConnectionSettingsConnector",
    "ConnectorsGoogledriveConnectionSettingsConnectorSchemas",
    "ConnectorsGooglemailConnectionSettings",
    "ConnectorsGooglemailConnectionSettingsSettings",
    "ConnectorsGooglemailConnectionSettingsSettingsOAuth",
    "ConnectorsGooglemailConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsGooglemailConnectionSettingsConnector",
    "ConnectorsGooglemailConnectionSettingsConnectorSchemas",
    "ConnectorsGooglesheetConnectionSettings",
    "ConnectorsGooglesheetConnectionSettingsSettings",
    "ConnectorsGooglesheetConnectionSettingsSettingsOAuth",
    "ConnectorsGooglesheetConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsGooglesheetConnectionSettingsConnector",
    "ConnectorsGooglesheetConnectionSettingsConnectorSchemas",
    "ConnectorsGreenhouseConnectionSettings",
    "ConnectorsGreenhouseConnectionSettingsSettings",
    "ConnectorsGreenhouseConnectionSettingsConnector",
    "ConnectorsGreenhouseConnectionSettingsConnectorSchemas",
    "ConnectorsHeronConnectionSettings",
    "ConnectorsHeronConnectionSettingsConnector",
    "ConnectorsHeronConnectionSettingsConnectorSchemas",
    "ConnectorsHubspotConnectionSettings",
    "ConnectorsHubspotConnectionSettingsSettings",
    "ConnectorsHubspotConnectionSettingsSettingsOAuth",
    "ConnectorsHubspotConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsHubspotConnectionSettingsConnector",
    "ConnectorsHubspotConnectionSettingsConnectorSchemas",
    "ConnectorsInstagramConnectionSettings",
    "ConnectorsInstagramConnectionSettingsSettings",
    "ConnectorsInstagramConnectionSettingsSettingsOAuth",
    "ConnectorsInstagramConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsInstagramConnectionSettingsSettingsOAuthCredentialsRaw",
    "ConnectorsInstagramConnectionSettingsSettingsOAuthConnectionConfig",
    "ConnectorsInstagramConnectionSettingsSettingsError",
    "ConnectorsInstagramConnectionSettingsConnector",
    "ConnectorsInstagramConnectionSettingsConnectorSchemas",
    "ConnectorsIntercomConnectionSettings",
    "ConnectorsIntercomConnectionSettingsSettings",
    "ConnectorsIntercomConnectionSettingsSettingsOAuth",
    "ConnectorsIntercomConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsIntercomConnectionSettingsSettingsOAuthCredentialsRaw",
    "ConnectorsIntercomConnectionSettingsSettingsOAuthConnectionConfig",
    "ConnectorsIntercomConnectionSettingsSettingsError",
    "ConnectorsIntercomConnectionSettingsConnector",
    "ConnectorsIntercomConnectionSettingsConnectorSchemas",
    "ConnectorsJiraConnectionSettings",
    "ConnectorsJiraConnectionSettingsSettings",
    "ConnectorsJiraConnectionSettingsSettingsOAuth",
    "ConnectorsJiraConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsJiraConnectionSettingsSettingsOAuthCredentialsRaw",
    "ConnectorsJiraConnectionSettingsSettingsOAuthConnectionConfig",
    "ConnectorsJiraConnectionSettingsSettingsError",
    "ConnectorsJiraConnectionSettingsConnector",
    "ConnectorsJiraConnectionSettingsConnectorSchemas",
    "ConnectorsKustomerConnectionSettings",
    "ConnectorsKustomerConnectionSettingsSettings",
    "ConnectorsKustomerConnectionSettingsSettingsOAuth",
    "ConnectorsKustomerConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsKustomerConnectionSettingsSettingsOAuthCredentialsRaw",
    "ConnectorsKustomerConnectionSettingsSettingsOAuthConnectionConfig",
    "ConnectorsKustomerConnectionSettingsSettingsError",
    "ConnectorsKustomerConnectionSettingsConnector",
    "ConnectorsKustomerConnectionSettingsConnectorSchemas",
    "ConnectorsLeverConnectionSettings",
    "ConnectorsLeverConnectionSettingsSettings",
    "ConnectorsLeverConnectionSettingsSettingsOAuth",
    "ConnectorsLeverConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsLeverConnectionSettingsSettingsOAuthCredentialsRaw",
    "ConnectorsLeverConnectionSettingsSettingsOAuthConnectionConfig",
    "ConnectorsLeverConnectionSettingsSettingsError",
    "ConnectorsLeverConnectionSettingsConnector",
    "ConnectorsLeverConnectionSettingsConnectorSchemas",
    "ConnectorsLinearConnectionSettings",
    "ConnectorsLinearConnectionSettingsSettings",
    "ConnectorsLinearConnectionSettingsSettingsOAuth",
    "ConnectorsLinearConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsLinearConnectionSettingsConnector",
    "ConnectorsLinearConnectionSettingsConnectorSchemas",
    "ConnectorsLinkedinConnectionSettings",
    "ConnectorsLinkedinConnectionSettingsSettings",
    "ConnectorsLinkedinConnectionSettingsSettingsOAuth",
    "ConnectorsLinkedinConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsLinkedinConnectionSettingsConnector",
    "ConnectorsLinkedinConnectionSettingsConnectorSchemas",
    "ConnectorsLunchmoneyConnectionSettings",
    "ConnectorsLunchmoneyConnectionSettingsConnector",
    "ConnectorsLunchmoneyConnectionSettingsConnectorSchemas",
    "ConnectorsMercuryConnectionSettings",
    "ConnectorsMercuryConnectionSettingsConnector",
    "ConnectorsMercuryConnectionSettingsConnectorSchemas",
    "ConnectorsMergeConnectionSettings",
    "ConnectorsMergeConnectionSettingsSettings",
    "ConnectorsMergeConnectionSettingsConnector",
    "ConnectorsMergeConnectionSettingsConnectorSchemas",
    "ConnectorsMicrosoftConnectionSettings",
    "ConnectorsMicrosoftConnectionSettingsSettings",
    "ConnectorsMicrosoftConnectionSettingsSettingsOAuth",
    "ConnectorsMicrosoftConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsMicrosoftConnectionSettingsSettingsOAuthCredentialsRaw",
    "ConnectorsMicrosoftConnectionSettingsSettingsOAuthConnectionConfig",
    "ConnectorsMicrosoftConnectionSettingsSettingsError",
    "ConnectorsMicrosoftConnectionSettingsConnector",
    "ConnectorsMicrosoftConnectionSettingsConnectorSchemas",
    "ConnectorsMootaConnectionSettings",
    "ConnectorsMootaConnectionSettingsConnector",
    "ConnectorsMootaConnectionSettingsConnectorSchemas",
    "ConnectorsNotionConnectionSettings",
    "ConnectorsNotionConnectionSettingsSettings",
    "ConnectorsNotionConnectionSettingsSettingsOAuth",
    "ConnectorsNotionConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsNotionConnectionSettingsConnector",
    "ConnectorsNotionConnectionSettingsConnectorSchemas",
    "ConnectorsOnebrickConnectionSettings",
    "ConnectorsOnebrickConnectionSettingsSettings",
    "ConnectorsOnebrickConnectionSettingsConnector",
    "ConnectorsOnebrickConnectionSettingsConnectorSchemas",
    "ConnectorsOutreachConnectionSettings",
    "ConnectorsOutreachConnectionSettingsSettings",
    "ConnectorsOutreachConnectionSettingsSettingsOAuth",
    "ConnectorsOutreachConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsOutreachConnectionSettingsSettingsOAuthCredentialsRaw",
    "ConnectorsOutreachConnectionSettingsSettingsOAuthConnectionConfig",
    "ConnectorsOutreachConnectionSettingsSettingsError",
    "ConnectorsOutreachConnectionSettingsConnector",
    "ConnectorsOutreachConnectionSettingsConnectorSchemas",
    "ConnectorsPipedriveConnectionSettings",
    "ConnectorsPipedriveConnectionSettingsSettings",
    "ConnectorsPipedriveConnectionSettingsSettingsOAuth",
    "ConnectorsPipedriveConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsPipedriveConnectionSettingsSettingsOAuthCredentialsRaw",
    "ConnectorsPipedriveConnectionSettingsSettingsOAuthConnectionConfig",
    "ConnectorsPipedriveConnectionSettingsSettingsError",
    "ConnectorsPipedriveConnectionSettingsConnector",
    "ConnectorsPipedriveConnectionSettingsConnectorSchemas",
    "ConnectorsPlaidConnectionSettings",
    "ConnectorsPlaidConnectionSettingsSettings",
    "ConnectorsPlaidConnectionSettingsConnector",
    "ConnectorsPlaidConnectionSettingsConnectorSchemas",
    "ConnectorsPostgresConnectionSettings",
    "ConnectorsPostgresConnectionSettingsSettings",
    "ConnectorsPostgresConnectionSettingsSettingsSourceQueries",
    "ConnectorsPostgresConnectionSettingsConnector",
    "ConnectorsPostgresConnectionSettingsConnectorSchemas",
    "ConnectorsQuickbooksConnectionSettings",
    "ConnectorsQuickbooksConnectionSettingsSettings",
    "ConnectorsQuickbooksConnectionSettingsSettingsOAuth",
    "ConnectorsQuickbooksConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsQuickbooksConnectionSettingsConnector",
    "ConnectorsQuickbooksConnectionSettingsConnectorSchemas",
    "ConnectorsRampConnectionSettings",
    "ConnectorsRampConnectionSettingsSettings",
    "ConnectorsRampConnectionSettingsConnector",
    "ConnectorsRampConnectionSettingsConnectorSchemas",
    "ConnectorsRedditConnectionSettings",
    "ConnectorsRedditConnectionSettingsSettings",
    "ConnectorsRedditConnectionSettingsSettingsOAuth",
    "ConnectorsRedditConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsRedditConnectionSettingsSettingsOAuthCredentialsRaw",
    "ConnectorsRedditConnectionSettingsSettingsOAuthConnectionConfig",
    "ConnectorsRedditConnectionSettingsSettingsError",
    "ConnectorsRedditConnectionSettingsConnector",
    "ConnectorsRedditConnectionSettingsConnectorSchemas",
    "ConnectorsSalesforceConnectionSettings",
    "ConnectorsSalesforceConnectionSettingsSettings",
    "ConnectorsSalesforceConnectionSettingsSettingsOAuth",
    "ConnectorsSalesforceConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsSalesforceConnectionSettingsConnector",
    "ConnectorsSalesforceConnectionSettingsConnectorSchemas",
    "ConnectorsSalesloftConnectionSettings",
    "ConnectorsSalesloftConnectionSettingsSettings",
    "ConnectorsSalesloftConnectionSettingsSettingsOAuth",
    "ConnectorsSalesloftConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsSalesloftConnectionSettingsSettingsOAuthCredentialsRaw",
    "ConnectorsSalesloftConnectionSettingsSettingsOAuthConnectionConfig",
    "ConnectorsSalesloftConnectionSettingsSettingsError",
    "ConnectorsSalesloftConnectionSettingsConnector",
    "ConnectorsSalesloftConnectionSettingsConnectorSchemas",
    "ConnectorsSaltedgeConnectionSettings",
    "ConnectorsSaltedgeConnectionSettingsConnector",
    "ConnectorsSaltedgeConnectionSettingsConnectorSchemas",
    "ConnectorsSharepointonlineConnectionSettings",
    "ConnectorsSharepointonlineConnectionSettingsSettings",
    "ConnectorsSharepointonlineConnectionSettingsSettingsOAuth",
    "ConnectorsSharepointonlineConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsSharepointonlineConnectionSettingsConnector",
    "ConnectorsSharepointonlineConnectionSettingsConnectorSchemas",
    "ConnectorsSlackConnectionSettings",
    "ConnectorsSlackConnectionSettingsSettings",
    "ConnectorsSlackConnectionSettingsSettingsOAuth",
    "ConnectorsSlackConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsSlackConnectionSettingsConnector",
    "ConnectorsSlackConnectionSettingsConnectorSchemas",
    "ConnectorsSplitwiseConnectionSettings",
    "ConnectorsSplitwiseConnectionSettingsSettings",
    "ConnectorsSplitwiseConnectionSettingsSettingsCurrentUser",
    "ConnectorsSplitwiseConnectionSettingsSettingsCurrentUserNotifications",
    "ConnectorsSplitwiseConnectionSettingsSettingsCurrentUserPicture",
    "ConnectorsSplitwiseConnectionSettingsConnector",
    "ConnectorsSplitwiseConnectionSettingsConnectorSchemas",
    "ConnectorsStripeConnectionSettings",
    "ConnectorsStripeConnectionSettingsSettings",
    "ConnectorsStripeConnectionSettingsConnector",
    "ConnectorsStripeConnectionSettingsConnectorSchemas",
    "ConnectorsTellerConnectionSettings",
    "ConnectorsTellerConnectionSettingsSettings",
    "ConnectorsTellerConnectionSettingsConnector",
    "ConnectorsTellerConnectionSettingsConnectorSchemas",
    "ConnectorsTogglConnectionSettings",
    "ConnectorsTogglConnectionSettingsSettings",
    "ConnectorsTogglConnectionSettingsConnector",
    "ConnectorsTogglConnectionSettingsConnectorSchemas",
    "ConnectorsTwentyConnectionSettings",
    "ConnectorsTwentyConnectionSettingsSettings",
    "ConnectorsTwentyConnectionSettingsConnector",
    "ConnectorsTwentyConnectionSettingsConnectorSchemas",
    "ConnectorsTwitterConnectionSettings",
    "ConnectorsTwitterConnectionSettingsSettings",
    "ConnectorsTwitterConnectionSettingsSettingsOAuth",
    "ConnectorsTwitterConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsTwitterConnectionSettingsSettingsOAuthCredentialsRaw",
    "ConnectorsTwitterConnectionSettingsSettingsOAuthConnectionConfig",
    "ConnectorsTwitterConnectionSettingsSettingsError",
    "ConnectorsTwitterConnectionSettingsConnector",
    "ConnectorsTwitterConnectionSettingsConnectorSchemas",
    "ConnectorsVenmoConnectionSettings",
    "ConnectorsVenmoConnectionSettingsSettings",
    "ConnectorsVenmoConnectionSettingsConnector",
    "ConnectorsVenmoConnectionSettingsConnectorSchemas",
    "ConnectorsWiseConnectionSettings",
    "ConnectorsWiseConnectionSettingsSettings",
    "ConnectorsWiseConnectionSettingsConnector",
    "ConnectorsWiseConnectionSettingsConnectorSchemas",
    "ConnectorsXeroConnectionSettings",
    "ConnectorsXeroConnectionSettingsSettings",
    "ConnectorsXeroConnectionSettingsSettingsOAuth",
    "ConnectorsXeroConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsXeroConnectionSettingsSettingsOAuthCredentialsRaw",
    "ConnectorsXeroConnectionSettingsSettingsOAuthConnectionConfig",
    "ConnectorsXeroConnectionSettingsSettingsError",
    "ConnectorsXeroConnectionSettingsConnector",
    "ConnectorsXeroConnectionSettingsConnectorSchemas",
    "ConnectorsYodleeConnectionSettings",
    "ConnectorsYodleeConnectionSettingsSettings",
    "ConnectorsYodleeConnectionSettingsSettingsAccessToken",
    "ConnectorsYodleeConnectionSettingsSettingsProviderAccount",
    "ConnectorsYodleeConnectionSettingsConnector",
    "ConnectorsYodleeConnectionSettingsConnectorSchemas",
    "ConnectorsZohodeskConnectionSettings",
    "ConnectorsZohodeskConnectionSettingsSettings",
    "ConnectorsZohodeskConnectionSettingsSettingsOAuth",
    "ConnectorsZohodeskConnectionSettingsSettingsOAuthCredentials",
    "ConnectorsZohodeskConnectionSettingsSettingsOAuthCredentialsRaw",
    "ConnectorsZohodeskConnectionSettingsSettingsOAuthConnectionConfig",
    "ConnectorsZohodeskConnectionSettingsSettingsError",
    "ConnectorsZohodeskConnectionSettingsConnector",
    "ConnectorsZohodeskConnectionSettingsConnectorSchemas",
]


class ConnectorsAircallConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsAircallConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsAircallConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsAircallConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsAircallConnectionSettingsSettingsOAuth


class ConnectorsAircallConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsAircallConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsAircallConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsAircallConnectionSettings(BaseModel):
    connector_name: Literal["aircall"]

    settings: ConnectorsAircallConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsAircallConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsAirtableConnectionSettingsSettings(BaseModel):
    airtable_base: str = FieldInfo(alias="airtableBase")

    api_key: str = FieldInfo(alias="apiKey")


class ConnectorsAirtableConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsAirtableConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsAirtableConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsAirtableConnectionSettings(BaseModel):
    connector_name: Literal["airtable"]

    settings: ConnectorsAirtableConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsAirtableConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsApolloConnectionSettingsSettingsOAuthCredentialsRaw(BaseModel):
    access_token: str

    expires_at: Optional[datetime] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_in: Optional[float] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsApolloConnectionSettingsSettingsOAuthCredentials(BaseModel):
    raw: ConnectorsApolloConnectionSettingsSettingsOAuthCredentialsRaw

    type: Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]

    access_token: Optional[str] = None

    api_key: Optional[str] = None

    expires_at: Optional[datetime] = None

    refresh_token: Optional[str] = None


class ConnectorsApolloConnectionSettingsSettingsOAuthConnectionConfig(BaseModel):
    instance_url: Optional[str] = None

    portal_id: Optional[float] = FieldInfo(alias="portalId", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsApolloConnectionSettingsSettingsOAuth(BaseModel):
    credentials: ConnectorsApolloConnectionSettingsSettingsOAuthCredentials

    metadata: Optional[Dict[str, object]] = None

    connection_config: Optional[ConnectorsApolloConnectionSettingsSettingsOAuthConnectionConfig] = None


class ConnectorsApolloConnectionSettingsSettingsError(BaseModel):
    code: Union[Literal["refresh_token_external_error"], str]

    message: Optional[str] = None


class ConnectorsApolloConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsApolloConnectionSettingsSettingsOAuth

    error: Optional[ConnectorsApolloConnectionSettingsSettingsError] = None


class ConnectorsApolloConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsApolloConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsApolloConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsApolloConnectionSettings(BaseModel):
    connector_name: Literal["apollo"]

    settings: ConnectorsApolloConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsApolloConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsBrexConnectionSettingsSettings(BaseModel):
    access_token: str = FieldInfo(alias="accessToken")


class ConnectorsBrexConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsBrexConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsBrexConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsBrexConnectionSettings(BaseModel):
    connector_name: Literal["brex"]

    settings: ConnectorsBrexConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsBrexConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsCodaConnectionSettingsSettings(BaseModel):
    api_key: str = FieldInfo(alias="apiKey")


class ConnectorsCodaConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsCodaConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsCodaConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsCodaConnectionSettings(BaseModel):
    connector_name: Literal["coda"]

    settings: ConnectorsCodaConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsCodaConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsConfluenceConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsConfluenceConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsConfluenceConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsConfluenceConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsConfluenceConnectionSettingsSettingsOAuth


class ConnectorsConfluenceConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsConfluenceConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsConfluenceConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsConfluenceConnectionSettings(BaseModel):
    connector_name: Literal["confluence"]

    settings: ConnectorsConfluenceConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsConfluenceConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsDiscordConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsDiscordConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsDiscordConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsDiscordConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsDiscordConnectionSettingsSettingsOAuth


class ConnectorsDiscordConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsDiscordConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsDiscordConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsDiscordConnectionSettings(BaseModel):
    connector_name: Literal["discord"]

    settings: ConnectorsDiscordConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsDiscordConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsFacebookConnectionSettingsSettingsOAuthCredentialsRaw(BaseModel):
    access_token: str

    expires_at: Optional[datetime] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_in: Optional[float] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsFacebookConnectionSettingsSettingsOAuthCredentials(BaseModel):
    raw: ConnectorsFacebookConnectionSettingsSettingsOAuthCredentialsRaw

    type: Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]

    access_token: Optional[str] = None

    api_key: Optional[str] = None

    expires_at: Optional[datetime] = None

    refresh_token: Optional[str] = None


class ConnectorsFacebookConnectionSettingsSettingsOAuthConnectionConfig(BaseModel):
    instance_url: Optional[str] = None

    portal_id: Optional[float] = FieldInfo(alias="portalId", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsFacebookConnectionSettingsSettingsOAuth(BaseModel):
    credentials: ConnectorsFacebookConnectionSettingsSettingsOAuthCredentials

    metadata: Optional[Dict[str, object]] = None

    connection_config: Optional[ConnectorsFacebookConnectionSettingsSettingsOAuthConnectionConfig] = None


class ConnectorsFacebookConnectionSettingsSettingsError(BaseModel):
    code: Union[Literal["refresh_token_external_error"], str]

    message: Optional[str] = None


class ConnectorsFacebookConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsFacebookConnectionSettingsSettingsOAuth

    error: Optional[ConnectorsFacebookConnectionSettingsSettingsError] = None


class ConnectorsFacebookConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsFacebookConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsFacebookConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsFacebookConnectionSettings(BaseModel):
    connector_name: Literal["facebook"]

    settings: ConnectorsFacebookConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsFacebookConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsFinchConnectionSettingsSettings(BaseModel):
    access_token: str


class ConnectorsFinchConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsFinchConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsFinchConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsFinchConnectionSettings(BaseModel):
    connector_name: Literal["finch"]

    settings: ConnectorsFinchConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsFinchConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsFirebaseConnectionSettingsSettingsUnionMember0ServiceAccount(BaseModel):
    project_id: str

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsFirebaseConnectionSettingsSettingsUnionMember0(BaseModel):
    role: Literal["admin"]

    service_account: ConnectorsFirebaseConnectionSettingsSettingsUnionMember0ServiceAccount = FieldInfo(
        alias="serviceAccount"
    )


class ConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember0UserJson(BaseModel):
    app_name: str = FieldInfo(alias="appName")

    sts_token_manager: Dict[str, object] = FieldInfo(alias="stsTokenManager")

    uid: str

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember0(BaseModel):
    method: Literal["userJson"]

    user_json: ConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember0UserJson = FieldInfo(
        alias="userJson"
    )


class ConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember1(BaseModel):
    custom_token: str = FieldInfo(alias="customToken")

    method: Literal["customToken"]


class ConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember2(BaseModel):
    email: str

    method: Literal["emailPassword"]

    password: str


ConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthData: TypeAlias = Union[
    ConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember0,
    ConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember1,
    ConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember2,
]


class ConnectorsFirebaseConnectionSettingsSettingsUnionMember1FirebaseConfig(BaseModel):
    api_key: str = FieldInfo(alias="apiKey")

    app_id: str = FieldInfo(alias="appId")

    auth_domain: str = FieldInfo(alias="authDomain")

    database_url: str = FieldInfo(alias="databaseURL")

    project_id: str = FieldInfo(alias="projectId")

    measurement_id: Optional[str] = FieldInfo(alias="measurementId", default=None)

    messaging_sender_id: Optional[str] = FieldInfo(alias="messagingSenderId", default=None)

    storage_bucket: Optional[str] = FieldInfo(alias="storageBucket", default=None)


class ConnectorsFirebaseConnectionSettingsSettingsUnionMember1(BaseModel):
    auth_data: ConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthData = FieldInfo(alias="authData")

    firebase_config: ConnectorsFirebaseConnectionSettingsSettingsUnionMember1FirebaseConfig = FieldInfo(
        alias="firebaseConfig"
    )

    role: Literal["user"]


ConnectorsFirebaseConnectionSettingsSettings: TypeAlias = Union[
    ConnectorsFirebaseConnectionSettingsSettingsUnionMember0, ConnectorsFirebaseConnectionSettingsSettingsUnionMember1
]


class ConnectorsFirebaseConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsFirebaseConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsFirebaseConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsFirebaseConnectionSettings(BaseModel):
    connector_name: Literal["firebase"]

    settings: ConnectorsFirebaseConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsFirebaseConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsForeceiptConnectionSettingsSettings(BaseModel):
    env_name: Literal["staging", "production"] = FieldInfo(alias="envName")

    api_id: Optional[object] = FieldInfo(alias="_id", default=None)

    credentials: Optional[object] = None


class ConnectorsForeceiptConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsForeceiptConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsForeceiptConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsForeceiptConnectionSettings(BaseModel):
    connector_name: Literal["foreceipt"]

    settings: ConnectorsForeceiptConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsForeceiptConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsGitHubConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsGitHubConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsGitHubConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsGitHubConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsGitHubConnectionSettingsSettingsOAuth


class ConnectorsGitHubConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsGitHubConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsGitHubConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsGitHubConnectionSettings(BaseModel):
    connector_name: Literal["github"]

    settings: ConnectorsGitHubConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsGitHubConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsGongConnectionSettingsSettingsOAuthCredentialsRaw(BaseModel):
    access_token: str

    expires_at: Optional[datetime] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_in: Optional[float] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsGongConnectionSettingsSettingsOAuthCredentials(BaseModel):
    raw: ConnectorsGongConnectionSettingsSettingsOAuthCredentialsRaw

    type: Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]

    access_token: Optional[str] = None

    api_key: Optional[str] = None

    expires_at: Optional[datetime] = None

    refresh_token: Optional[str] = None


class ConnectorsGongConnectionSettingsSettingsOAuthConnectionConfig(BaseModel):
    instance_url: Optional[str] = None

    portal_id: Optional[float] = FieldInfo(alias="portalId", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsGongConnectionSettingsSettingsOAuth(BaseModel):
    credentials: ConnectorsGongConnectionSettingsSettingsOAuthCredentials

    metadata: Optional[Dict[str, object]] = None

    connection_config: Optional[ConnectorsGongConnectionSettingsSettingsOAuthConnectionConfig] = None


class ConnectorsGongConnectionSettingsSettingsError(BaseModel):
    code: Union[Literal["refresh_token_external_error"], str]

    message: Optional[str] = None


class ConnectorsGongConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsGongConnectionSettingsSettingsOAuth

    error: Optional[ConnectorsGongConnectionSettingsSettingsError] = None


class ConnectorsGongConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsGongConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsGongConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsGongConnectionSettings(BaseModel):
    connector_name: Literal["gong"]

    settings: ConnectorsGongConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsGongConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsGooglecalendarConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsGooglecalendarConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsGooglecalendarConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsGooglecalendarConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsGooglecalendarConnectionSettingsSettingsOAuth


class ConnectorsGooglecalendarConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsGooglecalendarConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsGooglecalendarConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsGooglecalendarConnectionSettings(BaseModel):
    connector_name: Literal["googlecalendar"]

    settings: ConnectorsGooglecalendarConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsGooglecalendarConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsGoogledocsConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsGoogledocsConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsGoogledocsConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsGoogledocsConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsGoogledocsConnectionSettingsSettingsOAuth


class ConnectorsGoogledocsConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsGoogledocsConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsGoogledocsConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsGoogledocsConnectionSettings(BaseModel):
    connector_name: Literal["googledocs"]

    settings: ConnectorsGoogledocsConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsGoogledocsConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsGoogledriveConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsGoogledriveConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsGoogledriveConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsGoogledriveConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsGoogledriveConnectionSettingsSettingsOAuth


class ConnectorsGoogledriveConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsGoogledriveConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsGoogledriveConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsGoogledriveConnectionSettings(BaseModel):
    connector_name: Literal["googledrive"]

    settings: ConnectorsGoogledriveConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsGoogledriveConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsGooglemailConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsGooglemailConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsGooglemailConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsGooglemailConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsGooglemailConnectionSettingsSettingsOAuth


class ConnectorsGooglemailConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsGooglemailConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsGooglemailConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsGooglemailConnectionSettings(BaseModel):
    connector_name: Literal["googlemail"]

    settings: ConnectorsGooglemailConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsGooglemailConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsGooglesheetConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsGooglesheetConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsGooglesheetConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsGooglesheetConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsGooglesheetConnectionSettingsSettingsOAuth


class ConnectorsGooglesheetConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsGooglesheetConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsGooglesheetConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsGooglesheetConnectionSettings(BaseModel):
    connector_name: Literal["googlesheet"]

    settings: ConnectorsGooglesheetConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsGooglesheetConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsGreenhouseConnectionSettingsSettings(BaseModel):
    api_key: str = FieldInfo(alias="apiKey")


class ConnectorsGreenhouseConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsGreenhouseConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsGreenhouseConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsGreenhouseConnectionSettings(BaseModel):
    connector_name: Literal["greenhouse"]

    settings: ConnectorsGreenhouseConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsGreenhouseConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsHeronConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsHeronConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsHeronConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsHeronConnectionSettings(BaseModel):
    connector_name: Literal["heron"]

    settings: None

    id: Optional[str] = None

    connector: Optional[ConnectorsHeronConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsHubspotConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsHubspotConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsHubspotConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsHubspotConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsHubspotConnectionSettingsSettingsOAuth


class ConnectorsHubspotConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsHubspotConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsHubspotConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsHubspotConnectionSettings(BaseModel):
    connector_name: Literal["hubspot"]

    settings: ConnectorsHubspotConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsHubspotConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsInstagramConnectionSettingsSettingsOAuthCredentialsRaw(BaseModel):
    access_token: str

    expires_at: Optional[datetime] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_in: Optional[float] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsInstagramConnectionSettingsSettingsOAuthCredentials(BaseModel):
    raw: ConnectorsInstagramConnectionSettingsSettingsOAuthCredentialsRaw

    type: Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]

    access_token: Optional[str] = None

    api_key: Optional[str] = None

    expires_at: Optional[datetime] = None

    refresh_token: Optional[str] = None


class ConnectorsInstagramConnectionSettingsSettingsOAuthConnectionConfig(BaseModel):
    instance_url: Optional[str] = None

    portal_id: Optional[float] = FieldInfo(alias="portalId", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsInstagramConnectionSettingsSettingsOAuth(BaseModel):
    credentials: ConnectorsInstagramConnectionSettingsSettingsOAuthCredentials

    metadata: Optional[Dict[str, object]] = None

    connection_config: Optional[ConnectorsInstagramConnectionSettingsSettingsOAuthConnectionConfig] = None


class ConnectorsInstagramConnectionSettingsSettingsError(BaseModel):
    code: Union[Literal["refresh_token_external_error"], str]

    message: Optional[str] = None


class ConnectorsInstagramConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsInstagramConnectionSettingsSettingsOAuth

    error: Optional[ConnectorsInstagramConnectionSettingsSettingsError] = None


class ConnectorsInstagramConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsInstagramConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsInstagramConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsInstagramConnectionSettings(BaseModel):
    connector_name: Literal["instagram"]

    settings: ConnectorsInstagramConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsInstagramConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsIntercomConnectionSettingsSettingsOAuthCredentialsRaw(BaseModel):
    access_token: str

    expires_at: Optional[datetime] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_in: Optional[float] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsIntercomConnectionSettingsSettingsOAuthCredentials(BaseModel):
    raw: ConnectorsIntercomConnectionSettingsSettingsOAuthCredentialsRaw

    type: Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]

    access_token: Optional[str] = None

    api_key: Optional[str] = None

    expires_at: Optional[datetime] = None

    refresh_token: Optional[str] = None


class ConnectorsIntercomConnectionSettingsSettingsOAuthConnectionConfig(BaseModel):
    instance_url: Optional[str] = None

    portal_id: Optional[float] = FieldInfo(alias="portalId", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsIntercomConnectionSettingsSettingsOAuth(BaseModel):
    credentials: ConnectorsIntercomConnectionSettingsSettingsOAuthCredentials

    metadata: Optional[Dict[str, object]] = None

    connection_config: Optional[ConnectorsIntercomConnectionSettingsSettingsOAuthConnectionConfig] = None


class ConnectorsIntercomConnectionSettingsSettingsError(BaseModel):
    code: Union[Literal["refresh_token_external_error"], str]

    message: Optional[str] = None


class ConnectorsIntercomConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsIntercomConnectionSettingsSettingsOAuth

    error: Optional[ConnectorsIntercomConnectionSettingsSettingsError] = None


class ConnectorsIntercomConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsIntercomConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsIntercomConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsIntercomConnectionSettings(BaseModel):
    connector_name: Literal["intercom"]

    settings: ConnectorsIntercomConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsIntercomConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsJiraConnectionSettingsSettingsOAuthCredentialsRaw(BaseModel):
    access_token: str

    expires_at: Optional[datetime] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_in: Optional[float] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsJiraConnectionSettingsSettingsOAuthCredentials(BaseModel):
    raw: ConnectorsJiraConnectionSettingsSettingsOAuthCredentialsRaw

    type: Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]

    access_token: Optional[str] = None

    api_key: Optional[str] = None

    expires_at: Optional[datetime] = None

    refresh_token: Optional[str] = None


class ConnectorsJiraConnectionSettingsSettingsOAuthConnectionConfig(BaseModel):
    instance_url: Optional[str] = None

    portal_id: Optional[float] = FieldInfo(alias="portalId", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsJiraConnectionSettingsSettingsOAuth(BaseModel):
    credentials: ConnectorsJiraConnectionSettingsSettingsOAuthCredentials

    metadata: Optional[Dict[str, object]] = None

    connection_config: Optional[ConnectorsJiraConnectionSettingsSettingsOAuthConnectionConfig] = None


class ConnectorsJiraConnectionSettingsSettingsError(BaseModel):
    code: Union[Literal["refresh_token_external_error"], str]

    message: Optional[str] = None


class ConnectorsJiraConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsJiraConnectionSettingsSettingsOAuth

    error: Optional[ConnectorsJiraConnectionSettingsSettingsError] = None


class ConnectorsJiraConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsJiraConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsJiraConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsJiraConnectionSettings(BaseModel):
    connector_name: Literal["jira"]

    settings: ConnectorsJiraConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsJiraConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsKustomerConnectionSettingsSettingsOAuthCredentialsRaw(BaseModel):
    access_token: str

    expires_at: Optional[datetime] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_in: Optional[float] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsKustomerConnectionSettingsSettingsOAuthCredentials(BaseModel):
    raw: ConnectorsKustomerConnectionSettingsSettingsOAuthCredentialsRaw

    type: Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]

    access_token: Optional[str] = None

    api_key: Optional[str] = None

    expires_at: Optional[datetime] = None

    refresh_token: Optional[str] = None


class ConnectorsKustomerConnectionSettingsSettingsOAuthConnectionConfig(BaseModel):
    instance_url: Optional[str] = None

    portal_id: Optional[float] = FieldInfo(alias="portalId", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsKustomerConnectionSettingsSettingsOAuth(BaseModel):
    credentials: ConnectorsKustomerConnectionSettingsSettingsOAuthCredentials

    metadata: Optional[Dict[str, object]] = None

    connection_config: Optional[ConnectorsKustomerConnectionSettingsSettingsOAuthConnectionConfig] = None


class ConnectorsKustomerConnectionSettingsSettingsError(BaseModel):
    code: Union[Literal["refresh_token_external_error"], str]

    message: Optional[str] = None


class ConnectorsKustomerConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsKustomerConnectionSettingsSettingsOAuth

    error: Optional[ConnectorsKustomerConnectionSettingsSettingsError] = None


class ConnectorsKustomerConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsKustomerConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsKustomerConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsKustomerConnectionSettings(BaseModel):
    connector_name: Literal["kustomer"]

    settings: ConnectorsKustomerConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsKustomerConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsLeverConnectionSettingsSettingsOAuthCredentialsRaw(BaseModel):
    access_token: str

    expires_at: Optional[datetime] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_in: Optional[float] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsLeverConnectionSettingsSettingsOAuthCredentials(BaseModel):
    raw: ConnectorsLeverConnectionSettingsSettingsOAuthCredentialsRaw

    type: Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]

    access_token: Optional[str] = None

    api_key: Optional[str] = None

    expires_at: Optional[datetime] = None

    refresh_token: Optional[str] = None


class ConnectorsLeverConnectionSettingsSettingsOAuthConnectionConfig(BaseModel):
    instance_url: Optional[str] = None

    portal_id: Optional[float] = FieldInfo(alias="portalId", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsLeverConnectionSettingsSettingsOAuth(BaseModel):
    credentials: ConnectorsLeverConnectionSettingsSettingsOAuthCredentials

    metadata: Optional[Dict[str, object]] = None

    connection_config: Optional[ConnectorsLeverConnectionSettingsSettingsOAuthConnectionConfig] = None


class ConnectorsLeverConnectionSettingsSettingsError(BaseModel):
    code: Union[Literal["refresh_token_external_error"], str]

    message: Optional[str] = None


class ConnectorsLeverConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsLeverConnectionSettingsSettingsOAuth

    error: Optional[ConnectorsLeverConnectionSettingsSettingsError] = None


class ConnectorsLeverConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsLeverConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsLeverConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsLeverConnectionSettings(BaseModel):
    connector_name: Literal["lever"]

    settings: ConnectorsLeverConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsLeverConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsLinearConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsLinearConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsLinearConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsLinearConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsLinearConnectionSettingsSettingsOAuth


class ConnectorsLinearConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsLinearConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsLinearConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsLinearConnectionSettings(BaseModel):
    connector_name: Literal["linear"]

    settings: ConnectorsLinearConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsLinearConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsLinkedinConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsLinkedinConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsLinkedinConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsLinkedinConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsLinkedinConnectionSettingsSettingsOAuth


class ConnectorsLinkedinConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsLinkedinConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsLinkedinConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsLinkedinConnectionSettings(BaseModel):
    connector_name: Literal["linkedin"]

    settings: ConnectorsLinkedinConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsLinkedinConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsLunchmoneyConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsLunchmoneyConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsLunchmoneyConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsLunchmoneyConnectionSettings(BaseModel):
    connector_name: Literal["lunchmoney"]

    settings: None

    id: Optional[str] = None

    connector: Optional[ConnectorsLunchmoneyConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsMercuryConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsMercuryConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsMercuryConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsMercuryConnectionSettings(BaseModel):
    connector_name: Literal["mercury"]

    settings: None

    id: Optional[str] = None

    connector: Optional[ConnectorsMercuryConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsMergeConnectionSettingsSettings(BaseModel):
    account_token: str = FieldInfo(alias="accountToken")

    account_details: Optional[object] = FieldInfo(alias="accountDetails", default=None)


class ConnectorsMergeConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsMergeConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsMergeConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsMergeConnectionSettings(BaseModel):
    connector_name: Literal["merge"]

    settings: ConnectorsMergeConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsMergeConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsMicrosoftConnectionSettingsSettingsOAuthCredentialsRaw(BaseModel):
    access_token: str

    expires_at: Optional[datetime] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_in: Optional[float] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsMicrosoftConnectionSettingsSettingsOAuthCredentials(BaseModel):
    raw: ConnectorsMicrosoftConnectionSettingsSettingsOAuthCredentialsRaw

    type: Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]

    access_token: Optional[str] = None

    api_key: Optional[str] = None

    expires_at: Optional[datetime] = None

    refresh_token: Optional[str] = None


class ConnectorsMicrosoftConnectionSettingsSettingsOAuthConnectionConfig(BaseModel):
    instance_url: Optional[str] = None

    portal_id: Optional[float] = FieldInfo(alias="portalId", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsMicrosoftConnectionSettingsSettingsOAuth(BaseModel):
    credentials: ConnectorsMicrosoftConnectionSettingsSettingsOAuthCredentials

    metadata: Optional[Dict[str, object]] = None

    connection_config: Optional[ConnectorsMicrosoftConnectionSettingsSettingsOAuthConnectionConfig] = None


class ConnectorsMicrosoftConnectionSettingsSettingsError(BaseModel):
    code: Union[Literal["refresh_token_external_error"], str]

    message: Optional[str] = None


class ConnectorsMicrosoftConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsMicrosoftConnectionSettingsSettingsOAuth

    client_id: Optional[str] = None

    error: Optional[ConnectorsMicrosoftConnectionSettingsSettingsError] = None


class ConnectorsMicrosoftConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsMicrosoftConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsMicrosoftConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsMicrosoftConnectionSettings(BaseModel):
    connector_name: Literal["microsoft"]

    settings: ConnectorsMicrosoftConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsMicrosoftConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsMootaConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsMootaConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsMootaConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsMootaConnectionSettings(BaseModel):
    connector_name: Literal["moota"]

    settings: None

    id: Optional[str] = None

    connector: Optional[ConnectorsMootaConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsNotionConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsNotionConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsNotionConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsNotionConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsNotionConnectionSettingsSettingsOAuth


class ConnectorsNotionConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsNotionConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsNotionConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsNotionConnectionSettings(BaseModel):
    connector_name: Literal["notion"]

    settings: ConnectorsNotionConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsNotionConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsOnebrickConnectionSettingsSettings(BaseModel):
    access_token: str = FieldInfo(alias="accessToken")


class ConnectorsOnebrickConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsOnebrickConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsOnebrickConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsOnebrickConnectionSettings(BaseModel):
    connector_name: Literal["onebrick"]

    settings: ConnectorsOnebrickConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsOnebrickConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsOutreachConnectionSettingsSettingsOAuthCredentialsRaw(BaseModel):
    access_token: str

    expires_at: Optional[datetime] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_in: Optional[float] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsOutreachConnectionSettingsSettingsOAuthCredentials(BaseModel):
    raw: ConnectorsOutreachConnectionSettingsSettingsOAuthCredentialsRaw

    type: Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]

    access_token: Optional[str] = None

    api_key: Optional[str] = None

    expires_at: Optional[datetime] = None

    refresh_token: Optional[str] = None


class ConnectorsOutreachConnectionSettingsSettingsOAuthConnectionConfig(BaseModel):
    instance_url: Optional[str] = None

    portal_id: Optional[float] = FieldInfo(alias="portalId", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsOutreachConnectionSettingsSettingsOAuth(BaseModel):
    credentials: ConnectorsOutreachConnectionSettingsSettingsOAuthCredentials

    metadata: Optional[Dict[str, object]] = None

    connection_config: Optional[ConnectorsOutreachConnectionSettingsSettingsOAuthConnectionConfig] = None


class ConnectorsOutreachConnectionSettingsSettingsError(BaseModel):
    code: Union[Literal["refresh_token_external_error"], str]

    message: Optional[str] = None


class ConnectorsOutreachConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsOutreachConnectionSettingsSettingsOAuth

    error: Optional[ConnectorsOutreachConnectionSettingsSettingsError] = None


class ConnectorsOutreachConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsOutreachConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsOutreachConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsOutreachConnectionSettings(BaseModel):
    connector_name: Literal["outreach"]

    settings: ConnectorsOutreachConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsOutreachConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsPipedriveConnectionSettingsSettingsOAuthCredentialsRaw(BaseModel):
    access_token: str

    expires_at: Optional[datetime] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_in: Optional[float] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsPipedriveConnectionSettingsSettingsOAuthCredentials(BaseModel):
    raw: ConnectorsPipedriveConnectionSettingsSettingsOAuthCredentialsRaw

    type: Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]

    access_token: Optional[str] = None

    api_key: Optional[str] = None

    expires_at: Optional[datetime] = None

    refresh_token: Optional[str] = None


class ConnectorsPipedriveConnectionSettingsSettingsOAuthConnectionConfig(BaseModel):
    instance_url: Optional[str] = None

    portal_id: Optional[float] = FieldInfo(alias="portalId", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsPipedriveConnectionSettingsSettingsOAuth(BaseModel):
    credentials: ConnectorsPipedriveConnectionSettingsSettingsOAuthCredentials

    metadata: Optional[Dict[str, object]] = None

    connection_config: Optional[ConnectorsPipedriveConnectionSettingsSettingsOAuthConnectionConfig] = None


class ConnectorsPipedriveConnectionSettingsSettingsError(BaseModel):
    code: Union[Literal["refresh_token_external_error"], str]

    message: Optional[str] = None


class ConnectorsPipedriveConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsPipedriveConnectionSettingsSettingsOAuth

    error: Optional[ConnectorsPipedriveConnectionSettingsSettingsError] = None


class ConnectorsPipedriveConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsPipedriveConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsPipedriveConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsPipedriveConnectionSettings(BaseModel):
    connector_name: Literal["pipedrive"]

    settings: ConnectorsPipedriveConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsPipedriveConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsPlaidConnectionSettingsSettings(BaseModel):
    access_token: str = FieldInfo(alias="accessToken")

    institution: Optional[object] = None

    item: Optional[object] = None

    item_id: Optional[str] = FieldInfo(alias="itemId", default=None)

    status: Optional[object] = None

    webhook_item_error: None = FieldInfo(alias="webhookItemError", default=None)


class ConnectorsPlaidConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsPlaidConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsPlaidConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsPlaidConnectionSettings(BaseModel):
    connector_name: Literal["plaid"]

    settings: ConnectorsPlaidConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsPlaidConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsPostgresConnectionSettingsSettingsSourceQueries(BaseModel):
    invoice: Optional[str] = None
    """Should order by lastModifiedAt and id descending"""


class ConnectorsPostgresConnectionSettingsSettings(BaseModel):
    database_url: str = FieldInfo(alias="databaseUrl")

    source_queries: Optional[ConnectorsPostgresConnectionSettingsSettingsSourceQueries] = FieldInfo(
        alias="sourceQueries", default=None
    )


class ConnectorsPostgresConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsPostgresConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsPostgresConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsPostgresConnectionSettings(BaseModel):
    connector_name: Literal["postgres"]

    settings: ConnectorsPostgresConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsPostgresConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsQuickbooksConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsQuickbooksConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsQuickbooksConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsQuickbooksConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsQuickbooksConnectionSettingsSettingsOAuth

    realm_id: str = FieldInfo(alias="realmId")
    """The realmId of your quickbooks company (e.g., 9341453474484455)"""


class ConnectorsQuickbooksConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsQuickbooksConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsQuickbooksConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsQuickbooksConnectionSettings(BaseModel):
    connector_name: Literal["quickbooks"]

    settings: ConnectorsQuickbooksConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsQuickbooksConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsRampConnectionSettingsSettings(BaseModel):
    access_token: Optional[str] = FieldInfo(alias="accessToken", default=None)

    start_after_transaction_id: Optional[str] = FieldInfo(alias="startAfterTransactionId", default=None)


class ConnectorsRampConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsRampConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsRampConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsRampConnectionSettings(BaseModel):
    connector_name: Literal["ramp"]

    settings: ConnectorsRampConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsRampConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsRedditConnectionSettingsSettingsOAuthCredentialsRaw(BaseModel):
    access_token: str

    expires_at: Optional[datetime] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_in: Optional[float] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsRedditConnectionSettingsSettingsOAuthCredentials(BaseModel):
    raw: ConnectorsRedditConnectionSettingsSettingsOAuthCredentialsRaw

    type: Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]

    access_token: Optional[str] = None

    api_key: Optional[str] = None

    expires_at: Optional[datetime] = None

    refresh_token: Optional[str] = None


class ConnectorsRedditConnectionSettingsSettingsOAuthConnectionConfig(BaseModel):
    instance_url: Optional[str] = None

    portal_id: Optional[float] = FieldInfo(alias="portalId", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsRedditConnectionSettingsSettingsOAuth(BaseModel):
    credentials: ConnectorsRedditConnectionSettingsSettingsOAuthCredentials

    metadata: Optional[Dict[str, object]] = None

    connection_config: Optional[ConnectorsRedditConnectionSettingsSettingsOAuthConnectionConfig] = None


class ConnectorsRedditConnectionSettingsSettingsError(BaseModel):
    code: Union[Literal["refresh_token_external_error"], str]

    message: Optional[str] = None


class ConnectorsRedditConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsRedditConnectionSettingsSettingsOAuth

    error: Optional[ConnectorsRedditConnectionSettingsSettingsError] = None


class ConnectorsRedditConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsRedditConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsRedditConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsRedditConnectionSettings(BaseModel):
    connector_name: Literal["reddit"]

    settings: ConnectorsRedditConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsRedditConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsSalesforceConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsSalesforceConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsSalesforceConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsSalesforceConnectionSettingsSettings(BaseModel):
    instance_url: str
    """The instance URL of your Salesforce account (e.g., example)"""

    oauth: ConnectorsSalesforceConnectionSettingsSettingsOAuth


class ConnectorsSalesforceConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsSalesforceConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsSalesforceConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsSalesforceConnectionSettings(BaseModel):
    connector_name: Literal["salesforce"]

    settings: ConnectorsSalesforceConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsSalesforceConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsSalesloftConnectionSettingsSettingsOAuthCredentialsRaw(BaseModel):
    access_token: str

    expires_at: Optional[datetime] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_in: Optional[float] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsSalesloftConnectionSettingsSettingsOAuthCredentials(BaseModel):
    raw: ConnectorsSalesloftConnectionSettingsSettingsOAuthCredentialsRaw

    type: Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]

    access_token: Optional[str] = None

    api_key: Optional[str] = None

    expires_at: Optional[datetime] = None

    refresh_token: Optional[str] = None


class ConnectorsSalesloftConnectionSettingsSettingsOAuthConnectionConfig(BaseModel):
    instance_url: Optional[str] = None

    portal_id: Optional[float] = FieldInfo(alias="portalId", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsSalesloftConnectionSettingsSettingsOAuth(BaseModel):
    credentials: ConnectorsSalesloftConnectionSettingsSettingsOAuthCredentials

    metadata: Optional[Dict[str, object]] = None

    connection_config: Optional[ConnectorsSalesloftConnectionSettingsSettingsOAuthConnectionConfig] = None


class ConnectorsSalesloftConnectionSettingsSettingsError(BaseModel):
    code: Union[Literal["refresh_token_external_error"], str]

    message: Optional[str] = None


class ConnectorsSalesloftConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsSalesloftConnectionSettingsSettingsOAuth

    error: Optional[ConnectorsSalesloftConnectionSettingsSettingsError] = None


class ConnectorsSalesloftConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsSalesloftConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsSalesloftConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsSalesloftConnectionSettings(BaseModel):
    connector_name: Literal["salesloft"]

    settings: ConnectorsSalesloftConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsSalesloftConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsSaltedgeConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsSaltedgeConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsSaltedgeConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsSaltedgeConnectionSettings(BaseModel):
    connector_name: Literal["saltedge"]

    id: Optional[str] = None

    connector: Optional[ConnectorsSaltedgeConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    settings: Optional[object] = None

    updated_at: Optional[str] = None


class ConnectorsSharepointonlineConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsSharepointonlineConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsSharepointonlineConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsSharepointonlineConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsSharepointonlineConnectionSettingsSettingsOAuth


class ConnectorsSharepointonlineConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsSharepointonlineConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsSharepointonlineConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsSharepointonlineConnectionSettings(BaseModel):
    connector_name: Literal["sharepointonline"]

    settings: ConnectorsSharepointonlineConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsSharepointonlineConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsSlackConnectionSettingsSettingsOAuthCredentials(BaseModel):
    access_token: str

    client_id: str

    raw: Dict[str, object]

    scope: str

    expires_at: Optional[str] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None


class ConnectorsSlackConnectionSettingsSettingsOAuth(BaseModel):
    created_at: str

    last_fetched_at: str

    metadata: Optional[Dict[str, object]] = None

    updated_at: str

    credentials: Optional[ConnectorsSlackConnectionSettingsSettingsOAuthCredentials] = None
    """Output of the postConnect hook for oauth2 connectors"""


class ConnectorsSlackConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsSlackConnectionSettingsSettingsOAuth


class ConnectorsSlackConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsSlackConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsSlackConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsSlackConnectionSettings(BaseModel):
    connector_name: Literal["slack"]

    settings: ConnectorsSlackConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsSlackConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsSplitwiseConnectionSettingsSettingsCurrentUserNotifications(BaseModel):
    added_as_friend: bool

    added_to_group: bool

    announcements: bool

    bills: bool

    expense_added: bool

    expense_updated: bool

    monthly_summary: bool

    payments: bool


class ConnectorsSplitwiseConnectionSettingsSettingsCurrentUserPicture(BaseModel):
    large: Optional[str] = None

    medium: Optional[str] = None

    original: Optional[str] = None

    small: Optional[str] = None

    xlarge: Optional[str] = None

    xxlarge: Optional[str] = None


class ConnectorsSplitwiseConnectionSettingsSettingsCurrentUser(BaseModel):
    id: float

    country_code: str

    custom_picture: bool

    date_format: str

    default_currency: str

    default_group_id: float

    email: str

    first_name: str

    force_refresh_at: str

    last_name: str

    locale: str

    notifications: ConnectorsSplitwiseConnectionSettingsSettingsCurrentUserNotifications

    notifications_count: float

    notifications_read: str

    picture: ConnectorsSplitwiseConnectionSettingsSettingsCurrentUserPicture

    registration_status: str


class ConnectorsSplitwiseConnectionSettingsSettings(BaseModel):
    access_token: str = FieldInfo(alias="accessToken")

    current_user: Optional[ConnectorsSplitwiseConnectionSettingsSettingsCurrentUser] = FieldInfo(
        alias="currentUser", default=None
    )


class ConnectorsSplitwiseConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsSplitwiseConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsSplitwiseConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsSplitwiseConnectionSettings(BaseModel):
    connector_name: Literal["splitwise"]

    settings: ConnectorsSplitwiseConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsSplitwiseConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsStripeConnectionSettingsSettings(BaseModel):
    secret_key: str = FieldInfo(alias="secretKey")


class ConnectorsStripeConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsStripeConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsStripeConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsStripeConnectionSettings(BaseModel):
    connector_name: Literal["stripe"]

    settings: ConnectorsStripeConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsStripeConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsTellerConnectionSettingsSettings(BaseModel):
    token: str


class ConnectorsTellerConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsTellerConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsTellerConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsTellerConnectionSettings(BaseModel):
    connector_name: Literal["teller"]

    settings: ConnectorsTellerConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsTellerConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsTogglConnectionSettingsSettings(BaseModel):
    api_token: str = FieldInfo(alias="apiToken")

    email: Optional[str] = None

    password: Optional[str] = None


class ConnectorsTogglConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsTogglConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsTogglConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsTogglConnectionSettings(BaseModel):
    connector_name: Literal["toggl"]

    settings: ConnectorsTogglConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsTogglConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsTwentyConnectionSettingsSettings(BaseModel):
    access_token: str


class ConnectorsTwentyConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsTwentyConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsTwentyConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsTwentyConnectionSettings(BaseModel):
    connector_name: Literal["twenty"]

    settings: ConnectorsTwentyConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsTwentyConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsTwitterConnectionSettingsSettingsOAuthCredentialsRaw(BaseModel):
    access_token: str

    expires_at: Optional[datetime] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_in: Optional[float] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsTwitterConnectionSettingsSettingsOAuthCredentials(BaseModel):
    raw: ConnectorsTwitterConnectionSettingsSettingsOAuthCredentialsRaw

    type: Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]

    access_token: Optional[str] = None

    api_key: Optional[str] = None

    expires_at: Optional[datetime] = None

    refresh_token: Optional[str] = None


class ConnectorsTwitterConnectionSettingsSettingsOAuthConnectionConfig(BaseModel):
    instance_url: Optional[str] = None

    portal_id: Optional[float] = FieldInfo(alias="portalId", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsTwitterConnectionSettingsSettingsOAuth(BaseModel):
    credentials: ConnectorsTwitterConnectionSettingsSettingsOAuthCredentials

    metadata: Optional[Dict[str, object]] = None

    connection_config: Optional[ConnectorsTwitterConnectionSettingsSettingsOAuthConnectionConfig] = None


class ConnectorsTwitterConnectionSettingsSettingsError(BaseModel):
    code: Union[Literal["refresh_token_external_error"], str]

    message: Optional[str] = None


class ConnectorsTwitterConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsTwitterConnectionSettingsSettingsOAuth

    error: Optional[ConnectorsTwitterConnectionSettingsSettingsError] = None


class ConnectorsTwitterConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsTwitterConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsTwitterConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsTwitterConnectionSettings(BaseModel):
    connector_name: Literal["twitter"]

    settings: ConnectorsTwitterConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsTwitterConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsVenmoConnectionSettingsSettings(BaseModel):
    credentials: Optional[object] = None

    me: Optional[object] = None


class ConnectorsVenmoConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsVenmoConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsVenmoConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsVenmoConnectionSettings(BaseModel):
    connector_name: Literal["venmo"]

    settings: ConnectorsVenmoConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsVenmoConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsWiseConnectionSettingsSettings(BaseModel):
    env_name: Literal["sandbox", "live"] = FieldInfo(alias="envName")

    api_token: Optional[str] = FieldInfo(alias="apiToken", default=None)


class ConnectorsWiseConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsWiseConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsWiseConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsWiseConnectionSettings(BaseModel):
    connector_name: Literal["wise"]

    settings: ConnectorsWiseConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsWiseConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsXeroConnectionSettingsSettingsOAuthCredentialsRaw(BaseModel):
    access_token: str

    expires_at: Optional[datetime] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_in: Optional[float] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsXeroConnectionSettingsSettingsOAuthCredentials(BaseModel):
    raw: ConnectorsXeroConnectionSettingsSettingsOAuthCredentialsRaw

    type: Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]

    access_token: Optional[str] = None

    api_key: Optional[str] = None

    expires_at: Optional[datetime] = None

    refresh_token: Optional[str] = None


class ConnectorsXeroConnectionSettingsSettingsOAuthConnectionConfig(BaseModel):
    instance_url: Optional[str] = None

    portal_id: Optional[float] = FieldInfo(alias="portalId", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsXeroConnectionSettingsSettingsOAuth(BaseModel):
    credentials: ConnectorsXeroConnectionSettingsSettingsOAuthCredentials

    metadata: Optional[Dict[str, object]] = None

    connection_config: Optional[ConnectorsXeroConnectionSettingsSettingsOAuthConnectionConfig] = None


class ConnectorsXeroConnectionSettingsSettingsError(BaseModel):
    code: Union[Literal["refresh_token_external_error"], str]

    message: Optional[str] = None


class ConnectorsXeroConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsXeroConnectionSettingsSettingsOAuth

    error: Optional[ConnectorsXeroConnectionSettingsSettingsError] = None


class ConnectorsXeroConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsXeroConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsXeroConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsXeroConnectionSettings(BaseModel):
    connector_name: Literal["xero"]

    settings: ConnectorsXeroConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsXeroConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsYodleeConnectionSettingsSettingsAccessToken(BaseModel):
    access_token: str = FieldInfo(alias="accessToken")

    expires_in: float = FieldInfo(alias="expiresIn")

    issued_at: str = FieldInfo(alias="issuedAt")


class ConnectorsYodleeConnectionSettingsSettingsProviderAccount(BaseModel):
    id: float

    aggregation_source: str = FieldInfo(alias="aggregationSource")

    created_date: str = FieldInfo(alias="createdDate")

    dataset: List[object]

    is_manual: bool = FieldInfo(alias="isManual")

    provider_id: float = FieldInfo(alias="providerId")

    status: Literal["LOGIN_IN_PROGRESS", "USER_INPUT_REQUIRED", "IN_PROGRESS", "PARTIAL_SUCCESS", "SUCCESS", "FAILED"]

    is_deleted: Optional[bool] = FieldInfo(alias="isDeleted", default=None)


class ConnectorsYodleeConnectionSettingsSettings(BaseModel):
    login_name: str = FieldInfo(alias="loginName")

    provider_account_id: Union[float, str] = FieldInfo(alias="providerAccountId")

    access_token: Optional[ConnectorsYodleeConnectionSettingsSettingsAccessToken] = FieldInfo(
        alias="accessToken", default=None
    )

    provider: None = None

    provider_account: Optional[ConnectorsYodleeConnectionSettingsSettingsProviderAccount] = FieldInfo(
        alias="providerAccount", default=None
    )

    user: None = None


class ConnectorsYodleeConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsYodleeConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsYodleeConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsYodleeConnectionSettings(BaseModel):
    connector_name: Literal["yodlee"]

    settings: ConnectorsYodleeConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsYodleeConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


class ConnectorsZohodeskConnectionSettingsSettingsOAuthCredentialsRaw(BaseModel):
    access_token: str

    expires_at: Optional[datetime] = None

    expires_in: Optional[float] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_in: Optional[float] = None

    scope: Optional[str] = None

    token_type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsZohodeskConnectionSettingsSettingsOAuthCredentials(BaseModel):
    raw: ConnectorsZohodeskConnectionSettingsSettingsOAuthCredentialsRaw

    type: Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]

    access_token: Optional[str] = None

    api_key: Optional[str] = None

    expires_at: Optional[datetime] = None

    refresh_token: Optional[str] = None


class ConnectorsZohodeskConnectionSettingsSettingsOAuthConnectionConfig(BaseModel):
    instance_url: Optional[str] = None

    portal_id: Optional[float] = FieldInfo(alias="portalId", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsZohodeskConnectionSettingsSettingsOAuth(BaseModel):
    credentials: ConnectorsZohodeskConnectionSettingsSettingsOAuthCredentials

    metadata: Optional[Dict[str, object]] = None

    connection_config: Optional[ConnectorsZohodeskConnectionSettingsSettingsOAuthConnectionConfig] = None


class ConnectorsZohodeskConnectionSettingsSettingsError(BaseModel):
    code: Union[Literal["refresh_token_external_error"], str]

    message: Optional[str] = None


class ConnectorsZohodeskConnectionSettingsSettings(BaseModel):
    oauth: ConnectorsZohodeskConnectionSettingsSettingsOAuth

    error: Optional[ConnectorsZohodeskConnectionSettingsSettingsError] = None


class ConnectorsZohodeskConnectionSettingsConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsZohodeskConnectionSettingsConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsZohodeskConnectionSettingsConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsZohodeskConnectionSettings(BaseModel):
    connector_name: Literal["zohodesk"]

    settings: ConnectorsZohodeskConnectionSettingsSettings

    id: Optional[str] = None

    connector: Optional[ConnectorsZohodeskConnectionSettingsConnector] = None

    connector_config_id: Optional[str] = None

    created_at: Optional[str] = None

    customer_id: Optional[str] = None

    integration_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None


ListConnectionsResponse: TypeAlias = Union[
    ConnectorsAircallConnectionSettings,
    ConnectorsAirtableConnectionSettings,
    ConnectorsApolloConnectionSettings,
    ConnectorsBrexConnectionSettings,
    ConnectorsCodaConnectionSettings,
    ConnectorsConfluenceConnectionSettings,
    ConnectorsDiscordConnectionSettings,
    ConnectorsFacebookConnectionSettings,
    ConnectorsFinchConnectionSettings,
    ConnectorsFirebaseConnectionSettings,
    ConnectorsForeceiptConnectionSettings,
    ConnectorsGitHubConnectionSettings,
    ConnectorsGongConnectionSettings,
    ConnectorsGooglecalendarConnectionSettings,
    ConnectorsGoogledocsConnectionSettings,
    ConnectorsGoogledriveConnectionSettings,
    ConnectorsGooglemailConnectionSettings,
    ConnectorsGooglesheetConnectionSettings,
    ConnectorsGreenhouseConnectionSettings,
    ConnectorsHeronConnectionSettings,
    ConnectorsHubspotConnectionSettings,
    ConnectorsInstagramConnectionSettings,
    ConnectorsIntercomConnectionSettings,
    ConnectorsJiraConnectionSettings,
    ConnectorsKustomerConnectionSettings,
    ConnectorsLeverConnectionSettings,
    ConnectorsLinearConnectionSettings,
    ConnectorsLinkedinConnectionSettings,
    ConnectorsLunchmoneyConnectionSettings,
    ConnectorsMercuryConnectionSettings,
    ConnectorsMergeConnectionSettings,
    ConnectorsMicrosoftConnectionSettings,
    ConnectorsMootaConnectionSettings,
    ConnectorsNotionConnectionSettings,
    ConnectorsOnebrickConnectionSettings,
    ConnectorsOutreachConnectionSettings,
    ConnectorsPipedriveConnectionSettings,
    ConnectorsPlaidConnectionSettings,
    ConnectorsPostgresConnectionSettings,
    ConnectorsQuickbooksConnectionSettings,
    ConnectorsRampConnectionSettings,
    ConnectorsRedditConnectionSettings,
    ConnectorsSalesforceConnectionSettings,
    ConnectorsSalesloftConnectionSettings,
    ConnectorsSaltedgeConnectionSettings,
    ConnectorsSharepointonlineConnectionSettings,
    ConnectorsSlackConnectionSettings,
    ConnectorsSplitwiseConnectionSettings,
    ConnectorsStripeConnectionSettings,
    ConnectorsTellerConnectionSettings,
    ConnectorsTogglConnectionSettings,
    ConnectorsTwentyConnectionSettings,
    ConnectorsTwitterConnectionSettings,
    ConnectorsVenmoConnectionSettings,
    ConnectorsWiseConnectionSettings,
    ConnectorsXeroConnectionSettings,
    ConnectorsYodleeConnectionSettings,
    ConnectorsZohodeskConnectionSettings,
]
