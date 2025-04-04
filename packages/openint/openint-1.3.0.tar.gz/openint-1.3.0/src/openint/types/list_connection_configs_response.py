# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ListConnectionConfigsResponse",
    "ConnectorsAircallConnectorConfig",
    "ConnectorsAircallConnectorConfigConfig",
    "ConnectorsAircallConnectorConfigConfigOAuth",
    "ConnectorsAircallConnectorConfigConnector",
    "ConnectorsAircallConnectorConfigConnectorSchemas",
    "ConnectorsAircallConnectorConfigIntegrations",
    "ConnectorsAirtableConnectorConfig",
    "ConnectorsAirtableConnectorConfigConnector",
    "ConnectorsAirtableConnectorConfigConnectorSchemas",
    "ConnectorsAirtableConnectorConfigIntegrations",
    "ConnectorsApolloConnectorConfig",
    "ConnectorsApolloConnectorConfigConnector",
    "ConnectorsApolloConnectorConfigConnectorSchemas",
    "ConnectorsApolloConnectorConfigIntegrations",
    "ConnectorsBrexConnectorConfig",
    "ConnectorsBrexConnectorConfigConfig",
    "ConnectorsBrexConnectorConfigConfigOAuth",
    "ConnectorsBrexConnectorConfigConnector",
    "ConnectorsBrexConnectorConfigConnectorSchemas",
    "ConnectorsBrexConnectorConfigIntegrations",
    "ConnectorsCodaConnectorConfig",
    "ConnectorsCodaConnectorConfigConnector",
    "ConnectorsCodaConnectorConfigConnectorSchemas",
    "ConnectorsCodaConnectorConfigIntegrations",
    "ConnectorsConfluenceConnectorConfig",
    "ConnectorsConfluenceConnectorConfigConfig",
    "ConnectorsConfluenceConnectorConfigConfigOAuth",
    "ConnectorsConfluenceConnectorConfigConnector",
    "ConnectorsConfluenceConnectorConfigConnectorSchemas",
    "ConnectorsConfluenceConnectorConfigIntegrations",
    "ConnectorsDiscordConnectorConfig",
    "ConnectorsDiscordConnectorConfigConfig",
    "ConnectorsDiscordConnectorConfigConfigOAuth",
    "ConnectorsDiscordConnectorConfigConnector",
    "ConnectorsDiscordConnectorConfigConnectorSchemas",
    "ConnectorsDiscordConnectorConfigIntegrations",
    "ConnectorsFacebookConnectorConfig",
    "ConnectorsFacebookConnectorConfigConfig",
    "ConnectorsFacebookConnectorConfigConfigOAuth",
    "ConnectorsFacebookConnectorConfigConnector",
    "ConnectorsFacebookConnectorConfigConnectorSchemas",
    "ConnectorsFacebookConnectorConfigIntegrations",
    "ConnectorsFinchConnectorConfig",
    "ConnectorsFinchConnectorConfigConfig",
    "ConnectorsFinchConnectorConfigConnector",
    "ConnectorsFinchConnectorConfigConnectorSchemas",
    "ConnectorsFinchConnectorConfigIntegrations",
    "ConnectorsFirebaseConnectorConfig",
    "ConnectorsFirebaseConnectorConfigConnector",
    "ConnectorsFirebaseConnectorConfigConnectorSchemas",
    "ConnectorsFirebaseConnectorConfigIntegrations",
    "ConnectorsForeceiptConnectorConfig",
    "ConnectorsForeceiptConnectorConfigConnector",
    "ConnectorsForeceiptConnectorConfigConnectorSchemas",
    "ConnectorsForeceiptConnectorConfigIntegrations",
    "ConnectorsGitHubConnectorConfig",
    "ConnectorsGitHubConnectorConfigConfig",
    "ConnectorsGitHubConnectorConfigConfigOAuth",
    "ConnectorsGitHubConnectorConfigConnector",
    "ConnectorsGitHubConnectorConfigConnectorSchemas",
    "ConnectorsGitHubConnectorConfigIntegrations",
    "ConnectorsGongConnectorConfig",
    "ConnectorsGongConnectorConfigConfig",
    "ConnectorsGongConnectorConfigConfigOAuth",
    "ConnectorsGongConnectorConfigConnector",
    "ConnectorsGongConnectorConfigConnectorSchemas",
    "ConnectorsGongConnectorConfigIntegrations",
    "ConnectorsGooglecalendarConnectorConfig",
    "ConnectorsGooglecalendarConnectorConfigConfig",
    "ConnectorsGooglecalendarConnectorConfigConfigOAuth",
    "ConnectorsGooglecalendarConnectorConfigConnector",
    "ConnectorsGooglecalendarConnectorConfigConnectorSchemas",
    "ConnectorsGooglecalendarConnectorConfigIntegrations",
    "ConnectorsGoogledocsConnectorConfig",
    "ConnectorsGoogledocsConnectorConfigConfig",
    "ConnectorsGoogledocsConnectorConfigConfigOAuth",
    "ConnectorsGoogledocsConnectorConfigConnector",
    "ConnectorsGoogledocsConnectorConfigConnectorSchemas",
    "ConnectorsGoogledocsConnectorConfigIntegrations",
    "ConnectorsGoogledriveConnectorConfig",
    "ConnectorsGoogledriveConnectorConfigConfig",
    "ConnectorsGoogledriveConnectorConfigConfigOAuth",
    "ConnectorsGoogledriveConnectorConfigConnector",
    "ConnectorsGoogledriveConnectorConfigConnectorSchemas",
    "ConnectorsGoogledriveConnectorConfigIntegrations",
    "ConnectorsGooglemailConnectorConfig",
    "ConnectorsGooglemailConnectorConfigConfig",
    "ConnectorsGooglemailConnectorConfigConfigOAuth",
    "ConnectorsGooglemailConnectorConfigConnector",
    "ConnectorsGooglemailConnectorConfigConnectorSchemas",
    "ConnectorsGooglemailConnectorConfigIntegrations",
    "ConnectorsGooglesheetConnectorConfig",
    "ConnectorsGooglesheetConnectorConfigConfig",
    "ConnectorsGooglesheetConnectorConfigConfigOAuth",
    "ConnectorsGooglesheetConnectorConfigConnector",
    "ConnectorsGooglesheetConnectorConfigConnectorSchemas",
    "ConnectorsGooglesheetConnectorConfigIntegrations",
    "ConnectorsGreenhouseConnectorConfig",
    "ConnectorsGreenhouseConnectorConfigConnector",
    "ConnectorsGreenhouseConnectorConfigConnectorSchemas",
    "ConnectorsGreenhouseConnectorConfigIntegrations",
    "ConnectorsHeronConnectorConfig",
    "ConnectorsHeronConnectorConfigConfig",
    "ConnectorsHeronConnectorConfigConnector",
    "ConnectorsHeronConnectorConfigConnectorSchemas",
    "ConnectorsHeronConnectorConfigIntegrations",
    "ConnectorsHubspotConnectorConfig",
    "ConnectorsHubspotConnectorConfigConfig",
    "ConnectorsHubspotConnectorConfigConfigOAuth",
    "ConnectorsHubspotConnectorConfigConnector",
    "ConnectorsHubspotConnectorConfigConnectorSchemas",
    "ConnectorsHubspotConnectorConfigIntegrations",
    "ConnectorsInstagramConnectorConfig",
    "ConnectorsInstagramConnectorConfigConfig",
    "ConnectorsInstagramConnectorConfigConfigOAuth",
    "ConnectorsInstagramConnectorConfigConnector",
    "ConnectorsInstagramConnectorConfigConnectorSchemas",
    "ConnectorsInstagramConnectorConfigIntegrations",
    "ConnectorsIntercomConnectorConfig",
    "ConnectorsIntercomConnectorConfigConfig",
    "ConnectorsIntercomConnectorConfigConfigOAuth",
    "ConnectorsIntercomConnectorConfigConnector",
    "ConnectorsIntercomConnectorConfigConnectorSchemas",
    "ConnectorsIntercomConnectorConfigIntegrations",
    "ConnectorsJiraConnectorConfig",
    "ConnectorsJiraConnectorConfigConfig",
    "ConnectorsJiraConnectorConfigConfigOAuth",
    "ConnectorsJiraConnectorConfigConnector",
    "ConnectorsJiraConnectorConfigConnectorSchemas",
    "ConnectorsJiraConnectorConfigIntegrations",
    "ConnectorsKustomerConnectorConfig",
    "ConnectorsKustomerConnectorConfigConfig",
    "ConnectorsKustomerConnectorConfigConfigOAuth",
    "ConnectorsKustomerConnectorConfigConnector",
    "ConnectorsKustomerConnectorConfigConnectorSchemas",
    "ConnectorsKustomerConnectorConfigIntegrations",
    "ConnectorsLeverConnectorConfig",
    "ConnectorsLeverConnectorConfigConfig",
    "ConnectorsLeverConnectorConfigConfigOAuth",
    "ConnectorsLeverConnectorConfigConnector",
    "ConnectorsLeverConnectorConfigConnectorSchemas",
    "ConnectorsLeverConnectorConfigIntegrations",
    "ConnectorsLinearConnectorConfig",
    "ConnectorsLinearConnectorConfigConfig",
    "ConnectorsLinearConnectorConfigConfigOAuth",
    "ConnectorsLinearConnectorConfigConnector",
    "ConnectorsLinearConnectorConfigConnectorSchemas",
    "ConnectorsLinearConnectorConfigIntegrations",
    "ConnectorsLinkedinConnectorConfig",
    "ConnectorsLinkedinConnectorConfigConfig",
    "ConnectorsLinkedinConnectorConfigConfigOAuth",
    "ConnectorsLinkedinConnectorConfigConnector",
    "ConnectorsLinkedinConnectorConfigConnectorSchemas",
    "ConnectorsLinkedinConnectorConfigIntegrations",
    "ConnectorsLunchmoneyConnectorConfig",
    "ConnectorsLunchmoneyConnectorConfigConfig",
    "ConnectorsLunchmoneyConnectorConfigConnector",
    "ConnectorsLunchmoneyConnectorConfigConnectorSchemas",
    "ConnectorsLunchmoneyConnectorConfigIntegrations",
    "ConnectorsMercuryConnectorConfig",
    "ConnectorsMercuryConnectorConfigConfig",
    "ConnectorsMercuryConnectorConfigConfigOAuth",
    "ConnectorsMercuryConnectorConfigConnector",
    "ConnectorsMercuryConnectorConfigConnectorSchemas",
    "ConnectorsMercuryConnectorConfigIntegrations",
    "ConnectorsMergeConnectorConfig",
    "ConnectorsMergeConnectorConfigConfig",
    "ConnectorsMergeConnectorConfigConnector",
    "ConnectorsMergeConnectorConfigConnectorSchemas",
    "ConnectorsMergeConnectorConfigIntegrations",
    "ConnectorsMicrosoftConnectorConfig",
    "ConnectorsMicrosoftConnectorConfigConfig",
    "ConnectorsMicrosoftConnectorConfigConfigIntegrations",
    "ConnectorsMicrosoftConnectorConfigConfigIntegrationsOutlook",
    "ConnectorsMicrosoftConnectorConfigConfigIntegrationsSharepoint",
    "ConnectorsMicrosoftConnectorConfigConfigIntegrationsTeams",
    "ConnectorsMicrosoftConnectorConfigConfigOAuth",
    "ConnectorsMicrosoftConnectorConfigConnector",
    "ConnectorsMicrosoftConnectorConfigConnectorSchemas",
    "ConnectorsMicrosoftConnectorConfigIntegrations",
    "ConnectorsMootaConnectorConfig",
    "ConnectorsMootaConnectorConfigConfig",
    "ConnectorsMootaConnectorConfigConnector",
    "ConnectorsMootaConnectorConfigConnectorSchemas",
    "ConnectorsMootaConnectorConfigIntegrations",
    "ConnectorsNotionConnectorConfig",
    "ConnectorsNotionConnectorConfigConfig",
    "ConnectorsNotionConnectorConfigConfigOAuth",
    "ConnectorsNotionConnectorConfigConnector",
    "ConnectorsNotionConnectorConfigConnectorSchemas",
    "ConnectorsNotionConnectorConfigIntegrations",
    "ConnectorsOnebrickConnectorConfig",
    "ConnectorsOnebrickConnectorConfigConfig",
    "ConnectorsOnebrickConnectorConfigConnector",
    "ConnectorsOnebrickConnectorConfigConnectorSchemas",
    "ConnectorsOnebrickConnectorConfigIntegrations",
    "ConnectorsOutreachConnectorConfig",
    "ConnectorsOutreachConnectorConfigConfig",
    "ConnectorsOutreachConnectorConfigConfigOAuth",
    "ConnectorsOutreachConnectorConfigConnector",
    "ConnectorsOutreachConnectorConfigConnectorSchemas",
    "ConnectorsOutreachConnectorConfigIntegrations",
    "ConnectorsPipedriveConnectorConfig",
    "ConnectorsPipedriveConnectorConfigConfig",
    "ConnectorsPipedriveConnectorConfigConfigOAuth",
    "ConnectorsPipedriveConnectorConfigConnector",
    "ConnectorsPipedriveConnectorConfigConnectorSchemas",
    "ConnectorsPipedriveConnectorConfigIntegrations",
    "ConnectorsPlaidConnectorConfig",
    "ConnectorsPlaidConnectorConfigConfig",
    "ConnectorsPlaidConnectorConfigConfigCredentials",
    "ConnectorsPlaidConnectorConfigConnector",
    "ConnectorsPlaidConnectorConfigConnectorSchemas",
    "ConnectorsPlaidConnectorConfigIntegrations",
    "ConnectorsPostgresConnectorConfig",
    "ConnectorsPostgresConnectorConfigConnector",
    "ConnectorsPostgresConnectorConfigConnectorSchemas",
    "ConnectorsPostgresConnectorConfigIntegrations",
    "ConnectorsQuickbooksConnectorConfig",
    "ConnectorsQuickbooksConnectorConfigConfig",
    "ConnectorsQuickbooksConnectorConfigConfigOAuth",
    "ConnectorsQuickbooksConnectorConfigConnector",
    "ConnectorsQuickbooksConnectorConfigConnectorSchemas",
    "ConnectorsQuickbooksConnectorConfigIntegrations",
    "ConnectorsRampConnectorConfig",
    "ConnectorsRampConnectorConfigConfig",
    "ConnectorsRampConnectorConfigConfigOAuth",
    "ConnectorsRampConnectorConfigConnector",
    "ConnectorsRampConnectorConfigConnectorSchemas",
    "ConnectorsRampConnectorConfigIntegrations",
    "ConnectorsRedditConnectorConfig",
    "ConnectorsRedditConnectorConfigConfig",
    "ConnectorsRedditConnectorConfigConfigOAuth",
    "ConnectorsRedditConnectorConfigConnector",
    "ConnectorsRedditConnectorConfigConnectorSchemas",
    "ConnectorsRedditConnectorConfigIntegrations",
    "ConnectorsSalesforceConnectorConfig",
    "ConnectorsSalesforceConnectorConfigConfig",
    "ConnectorsSalesforceConnectorConfigConfigOAuth",
    "ConnectorsSalesforceConnectorConfigConnector",
    "ConnectorsSalesforceConnectorConfigConnectorSchemas",
    "ConnectorsSalesforceConnectorConfigIntegrations",
    "ConnectorsSalesloftConnectorConfig",
    "ConnectorsSalesloftConnectorConfigConfig",
    "ConnectorsSalesloftConnectorConfigConfigOAuth",
    "ConnectorsSalesloftConnectorConfigConnector",
    "ConnectorsSalesloftConnectorConfigConnectorSchemas",
    "ConnectorsSalesloftConnectorConfigIntegrations",
    "ConnectorsSaltedgeConnectorConfig",
    "ConnectorsSaltedgeConnectorConfigConfig",
    "ConnectorsSaltedgeConnectorConfigConnector",
    "ConnectorsSaltedgeConnectorConfigConnectorSchemas",
    "ConnectorsSaltedgeConnectorConfigIntegrations",
    "ConnectorsSharepointonlineConnectorConfig",
    "ConnectorsSharepointonlineConnectorConfigConfig",
    "ConnectorsSharepointonlineConnectorConfigConfigOAuth",
    "ConnectorsSharepointonlineConnectorConfigConnector",
    "ConnectorsSharepointonlineConnectorConfigConnectorSchemas",
    "ConnectorsSharepointonlineConnectorConfigIntegrations",
    "ConnectorsSlackConnectorConfig",
    "ConnectorsSlackConnectorConfigConfig",
    "ConnectorsSlackConnectorConfigConfigOAuth",
    "ConnectorsSlackConnectorConfigConnector",
    "ConnectorsSlackConnectorConfigConnectorSchemas",
    "ConnectorsSlackConnectorConfigIntegrations",
    "ConnectorsSplitwiseConnectorConfig",
    "ConnectorsSplitwiseConnectorConfigConnector",
    "ConnectorsSplitwiseConnectorConfigConnectorSchemas",
    "ConnectorsSplitwiseConnectorConfigIntegrations",
    "ConnectorsStripeConnectorConfig",
    "ConnectorsStripeConnectorConfigConfig",
    "ConnectorsStripeConnectorConfigConfigOAuth",
    "ConnectorsStripeConnectorConfigConnector",
    "ConnectorsStripeConnectorConfigConnectorSchemas",
    "ConnectorsStripeConnectorConfigIntegrations",
    "ConnectorsTellerConnectorConfig",
    "ConnectorsTellerConnectorConfigConfig",
    "ConnectorsTellerConnectorConfigConnector",
    "ConnectorsTellerConnectorConfigConnectorSchemas",
    "ConnectorsTellerConnectorConfigIntegrations",
    "ConnectorsTogglConnectorConfig",
    "ConnectorsTogglConnectorConfigConnector",
    "ConnectorsTogglConnectorConfigConnectorSchemas",
    "ConnectorsTogglConnectorConfigIntegrations",
    "ConnectorsTwentyConnectorConfig",
    "ConnectorsTwentyConnectorConfigConnector",
    "ConnectorsTwentyConnectorConfigConnectorSchemas",
    "ConnectorsTwentyConnectorConfigIntegrations",
    "ConnectorsTwitterConnectorConfig",
    "ConnectorsTwitterConnectorConfigConfig",
    "ConnectorsTwitterConnectorConfigConfigOAuth",
    "ConnectorsTwitterConnectorConfigConnector",
    "ConnectorsTwitterConnectorConfigConnectorSchemas",
    "ConnectorsTwitterConnectorConfigIntegrations",
    "ConnectorsVenmoConnectorConfig",
    "ConnectorsVenmoConnectorConfigConfig",
    "ConnectorsVenmoConnectorConfigConfigProxy",
    "ConnectorsVenmoConnectorConfigConnector",
    "ConnectorsVenmoConnectorConfigConnectorSchemas",
    "ConnectorsVenmoConnectorConfigIntegrations",
    "ConnectorsWiseConnectorConfig",
    "ConnectorsWiseConnectorConfigConnector",
    "ConnectorsWiseConnectorConfigConnectorSchemas",
    "ConnectorsWiseConnectorConfigIntegrations",
    "ConnectorsXeroConnectorConfig",
    "ConnectorsXeroConnectorConfigConfig",
    "ConnectorsXeroConnectorConfigConfigOAuth",
    "ConnectorsXeroConnectorConfigConnector",
    "ConnectorsXeroConnectorConfigConnectorSchemas",
    "ConnectorsXeroConnectorConfigIntegrations",
    "ConnectorsYodleeConnectorConfig",
    "ConnectorsYodleeConnectorConfigConfig",
    "ConnectorsYodleeConnectorConfigConfigProxy",
    "ConnectorsYodleeConnectorConfigConnector",
    "ConnectorsYodleeConnectorConfigConnectorSchemas",
    "ConnectorsYodleeConnectorConfigIntegrations",
    "ConnectorsZohodeskConnectorConfig",
    "ConnectorsZohodeskConnectorConfigConfig",
    "ConnectorsZohodeskConnectorConfigConfigOAuth",
    "ConnectorsZohodeskConnectorConfigConnector",
    "ConnectorsZohodeskConnectorConfigConnectorSchemas",
    "ConnectorsZohodeskConnectorConfigIntegrations",
]


class ConnectorsAircallConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsAircallConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsAircallConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsAircallConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsAircallConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsAircallConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsAircallConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsAircallConnectorConfig(BaseModel):
    config: ConnectorsAircallConnectorConfigConfig

    connector_name: Literal["aircall"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsAircallConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsAircallConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsAirtableConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsAirtableConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsAirtableConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsAirtableConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsAirtableConnectorConfig(BaseModel):
    config: None

    connector_name: Literal["airtable"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsAirtableConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsAirtableConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsApolloConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsApolloConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsApolloConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsApolloConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsApolloConnectorConfig(BaseModel):
    config: None

    connector_name: Literal["apollo"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsApolloConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsApolloConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsBrexConnectorConfigConfigOAuth(BaseModel):
    client_id: str = FieldInfo(alias="clientId")

    client_secret: str = FieldInfo(alias="clientSecret")


class ConnectorsBrexConnectorConfigConfig(BaseModel):
    apikey_auth: Optional[bool] = FieldInfo(alias="apikeyAuth", default=None)
    """API key auth support"""

    oauth: Optional[ConnectorsBrexConnectorConfigConfigOAuth] = None
    """Configure oauth"""


class ConnectorsBrexConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsBrexConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsBrexConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsBrexConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsBrexConnectorConfig(BaseModel):
    config: ConnectorsBrexConnectorConfigConfig

    connector_name: Literal["brex"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsBrexConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsBrexConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsCodaConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsCodaConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsCodaConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsCodaConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsCodaConnectorConfig(BaseModel):
    config: None

    connector_name: Literal["coda"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsCodaConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsCodaConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsConfluenceConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsConfluenceConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsConfluenceConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsConfluenceConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsConfluenceConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsConfluenceConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsConfluenceConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsConfluenceConnectorConfig(BaseModel):
    config: ConnectorsConfluenceConnectorConfigConfig

    connector_name: Literal["confluence"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsConfluenceConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsConfluenceConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsDiscordConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsDiscordConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsDiscordConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsDiscordConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsDiscordConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsDiscordConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsDiscordConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsDiscordConnectorConfig(BaseModel):
    config: ConnectorsDiscordConnectorConfigConfig

    connector_name: Literal["discord"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsDiscordConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsDiscordConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsFacebookConnectorConfigConfigOAuth(BaseModel):
    client_id: str

    client_secret: str

    scopes: Optional[str] = None


class ConnectorsFacebookConnectorConfigConfig(BaseModel):
    oauth: ConnectorsFacebookConnectorConfigConfigOAuth


class ConnectorsFacebookConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsFacebookConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsFacebookConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsFacebookConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsFacebookConnectorConfig(BaseModel):
    config: ConnectorsFacebookConnectorConfigConfig

    connector_name: Literal["facebook"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsFacebookConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsFacebookConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsFinchConnectorConfigConfig(BaseModel):
    client_id: str

    client_secret: str

    products: List[
        Literal["company", "directory", "individual", "ssn", "employment", "payment", "pay_statement", "benefits"]
    ]
    """
    Finch products to access, @see
    https://developer.tryfinch.com/api-reference/development-guides/Permissions
    """

    api_version: Optional[str] = None
    """Finch API version"""


class ConnectorsFinchConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsFinchConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsFinchConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsFinchConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsFinchConnectorConfig(BaseModel):
    config: ConnectorsFinchConnectorConfigConfig

    connector_name: Literal["finch"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsFinchConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsFinchConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsFirebaseConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsFirebaseConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsFirebaseConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsFirebaseConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsFirebaseConnectorConfig(BaseModel):
    config: None

    connector_name: Literal["firebase"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsFirebaseConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsFirebaseConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsForeceiptConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsForeceiptConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsForeceiptConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsForeceiptConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsForeceiptConnectorConfig(BaseModel):
    config: None

    connector_name: Literal["foreceipt"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsForeceiptConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsForeceiptConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsGitHubConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsGitHubConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsGitHubConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsGitHubConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsGitHubConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsGitHubConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsGitHubConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsGitHubConnectorConfig(BaseModel):
    config: ConnectorsGitHubConnectorConfigConfig

    connector_name: Literal["github"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsGitHubConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsGitHubConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsGongConnectorConfigConfigOAuth(BaseModel):
    client_id: str

    client_secret: str

    scopes: Optional[str] = None


class ConnectorsGongConnectorConfigConfig(BaseModel):
    oauth: ConnectorsGongConnectorConfigConfigOAuth


class ConnectorsGongConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsGongConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsGongConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsGongConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsGongConnectorConfig(BaseModel):
    config: ConnectorsGongConnectorConfigConfig

    connector_name: Literal["gong"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsGongConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsGongConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsGooglecalendarConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsGooglecalendarConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsGooglecalendarConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsGooglecalendarConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsGooglecalendarConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsGooglecalendarConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsGooglecalendarConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsGooglecalendarConnectorConfig(BaseModel):
    config: ConnectorsGooglecalendarConnectorConfigConfig

    connector_name: Literal["googlecalendar"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsGooglecalendarConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsGooglecalendarConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsGoogledocsConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsGoogledocsConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsGoogledocsConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsGoogledocsConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsGoogledocsConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsGoogledocsConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsGoogledocsConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsGoogledocsConnectorConfig(BaseModel):
    config: ConnectorsGoogledocsConnectorConfigConfig

    connector_name: Literal["googledocs"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsGoogledocsConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsGoogledocsConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsGoogledriveConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsGoogledriveConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsGoogledriveConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsGoogledriveConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsGoogledriveConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsGoogledriveConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsGoogledriveConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsGoogledriveConnectorConfig(BaseModel):
    config: ConnectorsGoogledriveConnectorConfigConfig

    connector_name: Literal["googledrive"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsGoogledriveConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsGoogledriveConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsGooglemailConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsGooglemailConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsGooglemailConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsGooglemailConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsGooglemailConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsGooglemailConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsGooglemailConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsGooglemailConnectorConfig(BaseModel):
    config: ConnectorsGooglemailConnectorConfigConfig

    connector_name: Literal["googlemail"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsGooglemailConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsGooglemailConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsGooglesheetConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsGooglesheetConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsGooglesheetConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsGooglesheetConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsGooglesheetConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsGooglesheetConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsGooglesheetConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsGooglesheetConnectorConfig(BaseModel):
    config: ConnectorsGooglesheetConnectorConfigConfig

    connector_name: Literal["googlesheet"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsGooglesheetConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsGooglesheetConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsGreenhouseConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsGreenhouseConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsGreenhouseConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsGreenhouseConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsGreenhouseConnectorConfig(BaseModel):
    config: None

    connector_name: Literal["greenhouse"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsGreenhouseConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsGreenhouseConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsHeronConnectorConfigConfig(BaseModel):
    api_key: str = FieldInfo(alias="apiKey")


class ConnectorsHeronConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsHeronConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsHeronConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsHeronConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsHeronConnectorConfig(BaseModel):
    config: ConnectorsHeronConnectorConfigConfig

    connector_name: Literal["heron"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsHeronConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsHeronConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsHubspotConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsHubspotConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsHubspotConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsHubspotConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsHubspotConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsHubspotConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsHubspotConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsHubspotConnectorConfig(BaseModel):
    config: ConnectorsHubspotConnectorConfigConfig

    connector_name: Literal["hubspot"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsHubspotConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsHubspotConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsInstagramConnectorConfigConfigOAuth(BaseModel):
    client_id: str

    client_secret: str

    scopes: Optional[str] = None


class ConnectorsInstagramConnectorConfigConfig(BaseModel):
    oauth: ConnectorsInstagramConnectorConfigConfigOAuth


class ConnectorsInstagramConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsInstagramConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsInstagramConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsInstagramConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsInstagramConnectorConfig(BaseModel):
    config: ConnectorsInstagramConnectorConfigConfig

    connector_name: Literal["instagram"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsInstagramConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsInstagramConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsIntercomConnectorConfigConfigOAuth(BaseModel):
    client_id: str

    client_secret: str

    scopes: Optional[str] = None


class ConnectorsIntercomConnectorConfigConfig(BaseModel):
    oauth: ConnectorsIntercomConnectorConfigConfigOAuth


class ConnectorsIntercomConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsIntercomConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsIntercomConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsIntercomConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsIntercomConnectorConfig(BaseModel):
    config: ConnectorsIntercomConnectorConfigConfig

    connector_name: Literal["intercom"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsIntercomConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsIntercomConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsJiraConnectorConfigConfigOAuth(BaseModel):
    client_id: str

    client_secret: str

    scopes: Optional[str] = None


class ConnectorsJiraConnectorConfigConfig(BaseModel):
    oauth: ConnectorsJiraConnectorConfigConfigOAuth


class ConnectorsJiraConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsJiraConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsJiraConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsJiraConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsJiraConnectorConfig(BaseModel):
    config: ConnectorsJiraConnectorConfigConfig

    connector_name: Literal["jira"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsJiraConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsJiraConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsKustomerConnectorConfigConfigOAuth(BaseModel):
    client_id: str

    client_secret: str

    scopes: Optional[str] = None


class ConnectorsKustomerConnectorConfigConfig(BaseModel):
    oauth: ConnectorsKustomerConnectorConfigConfigOAuth


class ConnectorsKustomerConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsKustomerConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsKustomerConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsKustomerConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsKustomerConnectorConfig(BaseModel):
    config: ConnectorsKustomerConnectorConfigConfig

    connector_name: Literal["kustomer"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsKustomerConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsKustomerConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsLeverConnectorConfigConfigOAuth(BaseModel):
    client_id: str

    client_secret: str

    scopes: Optional[str] = None


class ConnectorsLeverConnectorConfigConfig(BaseModel):
    env_name: Literal["sandbox", "production"] = FieldInfo(alias="envName")

    oauth: ConnectorsLeverConnectorConfigConfigOAuth


class ConnectorsLeverConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsLeverConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsLeverConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsLeverConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsLeverConnectorConfig(BaseModel):
    config: ConnectorsLeverConnectorConfigConfig

    connector_name: Literal["lever"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsLeverConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsLeverConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsLinearConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsLinearConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsLinearConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsLinearConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsLinearConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsLinearConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsLinearConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsLinearConnectorConfig(BaseModel):
    config: ConnectorsLinearConnectorConfigConfig

    connector_name: Literal["linear"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsLinearConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsLinearConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsLinkedinConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsLinkedinConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsLinkedinConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsLinkedinConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsLinkedinConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsLinkedinConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsLinkedinConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsLinkedinConnectorConfig(BaseModel):
    config: ConnectorsLinkedinConnectorConfigConfig

    connector_name: Literal["linkedin"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsLinkedinConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsLinkedinConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsLunchmoneyConnectorConfigConfig(BaseModel):
    access_token: str = FieldInfo(alias="accessToken")


class ConnectorsLunchmoneyConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsLunchmoneyConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsLunchmoneyConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsLunchmoneyConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsLunchmoneyConnectorConfig(BaseModel):
    config: ConnectorsLunchmoneyConnectorConfigConfig

    connector_name: Literal["lunchmoney"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsLunchmoneyConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsLunchmoneyConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsMercuryConnectorConfigConfigOAuth(BaseModel):
    client_id: str = FieldInfo(alias="clientId")

    client_secret: str = FieldInfo(alias="clientSecret")


class ConnectorsMercuryConnectorConfigConfig(BaseModel):
    apikey_auth: Optional[bool] = FieldInfo(alias="apikeyAuth", default=None)
    """API key auth support"""

    oauth: Optional[ConnectorsMercuryConnectorConfigConfigOAuth] = None
    """Configure oauth"""


class ConnectorsMercuryConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsMercuryConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsMercuryConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsMercuryConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsMercuryConnectorConfig(BaseModel):
    config: ConnectorsMercuryConnectorConfigConfig

    connector_name: Literal["mercury"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsMercuryConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsMercuryConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsMergeConnectorConfigConfig(BaseModel):
    api_key: str = FieldInfo(alias="apiKey")


class ConnectorsMergeConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsMergeConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsMergeConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsMergeConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsMergeConnectorConfig(BaseModel):
    config: ConnectorsMergeConnectorConfigConfig

    connector_name: Literal["merge"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsMergeConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsMergeConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsMicrosoftConnectorConfigConfigIntegrationsOutlook(BaseModel):
    enabled: Optional[bool] = None

    scopes: Optional[str] = None
    """outlook specific space separated scopes"""


class ConnectorsMicrosoftConnectorConfigConfigIntegrationsSharepoint(BaseModel):
    enabled: Optional[bool] = None

    scopes: Optional[str] = None
    """sharepoint specific space separated scopes"""


class ConnectorsMicrosoftConnectorConfigConfigIntegrationsTeams(BaseModel):
    enabled: Optional[bool] = None

    scopes: Optional[str] = None
    """teams specific space separated scopes"""


class ConnectorsMicrosoftConnectorConfigConfigIntegrations(BaseModel):
    outlook: Optional[ConnectorsMicrosoftConnectorConfigConfigIntegrationsOutlook] = None

    sharepoint: Optional[ConnectorsMicrosoftConnectorConfigConfigIntegrationsSharepoint] = None

    teams: Optional[ConnectorsMicrosoftConnectorConfigConfigIntegrationsTeams] = None


class ConnectorsMicrosoftConnectorConfigConfigOAuth(BaseModel):
    client_id: str

    client_secret: str

    scopes: Optional[str] = None
    """global microsoft connector space separated scopes"""


class ConnectorsMicrosoftConnectorConfigConfig(BaseModel):
    integrations: ConnectorsMicrosoftConnectorConfigConfigIntegrations

    oauth: ConnectorsMicrosoftConnectorConfigConfigOAuth


class ConnectorsMicrosoftConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsMicrosoftConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsMicrosoftConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsMicrosoftConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsMicrosoftConnectorConfig(BaseModel):
    config: ConnectorsMicrosoftConnectorConfigConfig

    connector_name: Literal["microsoft"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsMicrosoftConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsMicrosoftConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsMootaConnectorConfigConfig(BaseModel):
    token: str


class ConnectorsMootaConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsMootaConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsMootaConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsMootaConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsMootaConnectorConfig(BaseModel):
    config: ConnectorsMootaConnectorConfigConfig

    connector_name: Literal["moota"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsMootaConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsMootaConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsNotionConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsNotionConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsNotionConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsNotionConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsNotionConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsNotionConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsNotionConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsNotionConnectorConfig(BaseModel):
    config: ConnectorsNotionConnectorConfigConfig

    connector_name: Literal["notion"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsNotionConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsNotionConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsOnebrickConnectorConfigConfig(BaseModel):
    client_id: str = FieldInfo(alias="clientId")

    client_secret: str = FieldInfo(alias="clientSecret")

    env_name: Literal["sandbox", "production"] = FieldInfo(alias="envName")

    public_token: str = FieldInfo(alias="publicToken")

    access_token: Optional[str] = FieldInfo(alias="accessToken", default=None)

    redirect_url: Optional[str] = FieldInfo(alias="redirectUrl", default=None)


class ConnectorsOnebrickConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsOnebrickConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsOnebrickConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsOnebrickConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsOnebrickConnectorConfig(BaseModel):
    config: ConnectorsOnebrickConnectorConfigConfig

    connector_name: Literal["onebrick"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsOnebrickConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsOnebrickConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsOutreachConnectorConfigConfigOAuth(BaseModel):
    client_id: str

    client_secret: str

    scopes: Optional[str] = None


class ConnectorsOutreachConnectorConfigConfig(BaseModel):
    oauth: ConnectorsOutreachConnectorConfigConfigOAuth


class ConnectorsOutreachConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsOutreachConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsOutreachConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsOutreachConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsOutreachConnectorConfig(BaseModel):
    config: ConnectorsOutreachConnectorConfigConfig

    connector_name: Literal["outreach"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsOutreachConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsOutreachConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsPipedriveConnectorConfigConfigOAuth(BaseModel):
    client_id: str

    client_secret: str

    scopes: Optional[str] = None


class ConnectorsPipedriveConnectorConfigConfig(BaseModel):
    oauth: ConnectorsPipedriveConnectorConfigConfigOAuth


class ConnectorsPipedriveConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsPipedriveConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsPipedriveConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsPipedriveConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsPipedriveConnectorConfig(BaseModel):
    config: ConnectorsPipedriveConnectorConfigConfig

    connector_name: Literal["pipedrive"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsPipedriveConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsPipedriveConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsPlaidConnectorConfigConfigCredentials(BaseModel):
    client_id: str = FieldInfo(alias="clientId")

    client_secret: str = FieldInfo(alias="clientSecret")


class ConnectorsPlaidConnectorConfigConfig(BaseModel):
    client_name: str = FieldInfo(alias="clientName")
    """
    The name of your application, as it should be displayed in Link. Maximum length
    of 30 characters. If a value longer than 30 characters is provided, Link will
    display "This Application" instead.
    """

    country_codes: List[
        Literal["US", "GB", "ES", "NL", "FR", "IE", "CA", "DE", "IT", "PL", "DK", "NO", "SE", "EE", "LT", "LV"]
    ] = FieldInfo(alias="countryCodes")

    env_name: Literal["sandbox", "development", "production"] = FieldInfo(alias="envName")

    language: Literal["en", "fr", "es", "nl", "de"]

    products: List[
        Literal[
            "assets",
            "auth",
            "balance",
            "identity",
            "investments",
            "liabilities",
            "payment_initiation",
            "identity_verification",
            "transactions",
            "credit_details",
            "income",
            "income_verification",
            "deposit_switch",
            "standing_orders",
            "transfer",
            "employment",
            "recurring_transactions",
        ]
    ]

    credentials: Optional[ConnectorsPlaidConnectorConfigConfigCredentials] = None


class ConnectorsPlaidConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsPlaidConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsPlaidConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsPlaidConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsPlaidConnectorConfig(BaseModel):
    config: ConnectorsPlaidConnectorConfigConfig

    connector_name: Literal["plaid"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsPlaidConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsPlaidConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsPostgresConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsPostgresConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsPostgresConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsPostgresConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsPostgresConnectorConfig(BaseModel):
    config: None

    connector_name: Literal["postgres"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsPostgresConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsPostgresConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsQuickbooksConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsQuickbooksConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsQuickbooksConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsQuickbooksConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsQuickbooksConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsQuickbooksConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsQuickbooksConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsQuickbooksConnectorConfig(BaseModel):
    config: ConnectorsQuickbooksConnectorConfigConfig

    connector_name: Literal["quickbooks"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsQuickbooksConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsQuickbooksConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsRampConnectorConfigConfigOAuth(BaseModel):
    client_id: str = FieldInfo(alias="clientId")

    client_secret: str = FieldInfo(alias="clientSecret")


class ConnectorsRampConnectorConfigConfig(BaseModel):
    oauth: ConnectorsRampConnectorConfigConfigOAuth


class ConnectorsRampConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsRampConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsRampConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsRampConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsRampConnectorConfig(BaseModel):
    config: ConnectorsRampConnectorConfigConfig

    connector_name: Literal["ramp"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsRampConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsRampConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsRedditConnectorConfigConfigOAuth(BaseModel):
    client_id: str

    client_secret: str

    scopes: Optional[str] = None


class ConnectorsRedditConnectorConfigConfig(BaseModel):
    oauth: ConnectorsRedditConnectorConfigConfigOAuth


class ConnectorsRedditConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsRedditConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsRedditConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsRedditConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsRedditConnectorConfig(BaseModel):
    config: ConnectorsRedditConnectorConfigConfig

    connector_name: Literal["reddit"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsRedditConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsRedditConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsSalesforceConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsSalesforceConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsSalesforceConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsSalesforceConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsSalesforceConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsSalesforceConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsSalesforceConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsSalesforceConnectorConfig(BaseModel):
    config: ConnectorsSalesforceConnectorConfigConfig

    connector_name: Literal["salesforce"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsSalesforceConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsSalesforceConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsSalesloftConnectorConfigConfigOAuth(BaseModel):
    client_id: str

    client_secret: str

    scopes: Optional[str] = None


class ConnectorsSalesloftConnectorConfigConfig(BaseModel):
    oauth: ConnectorsSalesloftConnectorConfigConfigOAuth


class ConnectorsSalesloftConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsSalesloftConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsSalesloftConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsSalesloftConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsSalesloftConnectorConfig(BaseModel):
    config: ConnectorsSalesloftConnectorConfigConfig

    connector_name: Literal["salesloft"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsSalesloftConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsSalesloftConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsSaltedgeConnectorConfigConfig(BaseModel):
    app_id: str = FieldInfo(alias="appId")

    secret: str

    url: Optional[str] = None


class ConnectorsSaltedgeConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsSaltedgeConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsSaltedgeConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsSaltedgeConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsSaltedgeConnectorConfig(BaseModel):
    config: ConnectorsSaltedgeConnectorConfigConfig

    connector_name: Literal["saltedge"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsSaltedgeConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsSaltedgeConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsSharepointonlineConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsSharepointonlineConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsSharepointonlineConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsSharepointonlineConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsSharepointonlineConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsSharepointonlineConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsSharepointonlineConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsSharepointonlineConnectorConfig(BaseModel):
    config: ConnectorsSharepointonlineConnectorConfigConfig

    connector_name: Literal["sharepointonline"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsSharepointonlineConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsSharepointonlineConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsSlackConnectorConfigConfigOAuth(BaseModel):
    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    scopes: Optional[List[str]] = None


class ConnectorsSlackConnectorConfigConfig(BaseModel):
    oauth: Optional[ConnectorsSlackConnectorConfigConfigOAuth] = None
    """Base oauth configuration for the connector"""


class ConnectorsSlackConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsSlackConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsSlackConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsSlackConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsSlackConnectorConfig(BaseModel):
    config: ConnectorsSlackConnectorConfigConfig

    connector_name: Literal["slack"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsSlackConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsSlackConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsSplitwiseConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsSplitwiseConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsSplitwiseConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsSplitwiseConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsSplitwiseConnectorConfig(BaseModel):
    config: None

    connector_name: Literal["splitwise"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsSplitwiseConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsSplitwiseConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsStripeConnectorConfigConfigOAuth(BaseModel):
    client_id: str = FieldInfo(alias="clientId")

    client_secret: str = FieldInfo(alias="clientSecret")


class ConnectorsStripeConnectorConfigConfig(BaseModel):
    apikey_auth: Optional[bool] = FieldInfo(alias="apikeyAuth", default=None)
    """API key auth support"""

    oauth: Optional[ConnectorsStripeConnectorConfigConfigOAuth] = None
    """Configure oauth"""


class ConnectorsStripeConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsStripeConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsStripeConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsStripeConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsStripeConnectorConfig(BaseModel):
    config: ConnectorsStripeConnectorConfigConfig

    connector_name: Literal["stripe"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsStripeConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsStripeConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsTellerConnectorConfigConfig(BaseModel):
    application_id: str = FieldInfo(alias="applicationId")

    token: Optional[str] = None


class ConnectorsTellerConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsTellerConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsTellerConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsTellerConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsTellerConnectorConfig(BaseModel):
    config: ConnectorsTellerConnectorConfigConfig

    connector_name: Literal["teller"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsTellerConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsTellerConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsTogglConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsTogglConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsTogglConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsTogglConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsTogglConnectorConfig(BaseModel):
    config: None

    connector_name: Literal["toggl"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsTogglConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsTogglConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsTwentyConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsTwentyConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsTwentyConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsTwentyConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsTwentyConnectorConfig(BaseModel):
    config: None

    connector_name: Literal["twenty"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsTwentyConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsTwentyConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsTwitterConnectorConfigConfigOAuth(BaseModel):
    client_id: str

    client_secret: str

    scopes: Optional[str] = None


class ConnectorsTwitterConnectorConfigConfig(BaseModel):
    oauth: ConnectorsTwitterConnectorConfigConfigOAuth


class ConnectorsTwitterConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsTwitterConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsTwitterConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsTwitterConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsTwitterConnectorConfig(BaseModel):
    config: ConnectorsTwitterConnectorConfigConfig

    connector_name: Literal["twitter"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsTwitterConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsTwitterConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsVenmoConnectorConfigConfigProxy(BaseModel):
    cert: str

    url: str


class ConnectorsVenmoConnectorConfigConfig(BaseModel):
    proxy: Optional[ConnectorsVenmoConnectorConfigConfigProxy] = None

    v1_base_url: Optional[str] = FieldInfo(alias="v1BaseURL", default=None)

    v5_base_url: Optional[str] = FieldInfo(alias="v5BaseURL", default=None)


class ConnectorsVenmoConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsVenmoConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsVenmoConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsVenmoConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsVenmoConnectorConfig(BaseModel):
    config: ConnectorsVenmoConnectorConfigConfig

    connector_name: Literal["venmo"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsVenmoConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsVenmoConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsWiseConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsWiseConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsWiseConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsWiseConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsWiseConnectorConfig(BaseModel):
    config: None

    connector_name: Literal["wise"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsWiseConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsWiseConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsXeroConnectorConfigConfigOAuth(BaseModel):
    client_id: str

    client_secret: str

    scopes: Optional[str] = None


class ConnectorsXeroConnectorConfigConfig(BaseModel):
    oauth: ConnectorsXeroConnectorConfigConfigOAuth


class ConnectorsXeroConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsXeroConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsXeroConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsXeroConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsXeroConnectorConfig(BaseModel):
    config: ConnectorsXeroConnectorConfigConfig

    connector_name: Literal["xero"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsXeroConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsXeroConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsYodleeConnectorConfigConfigProxy(BaseModel):
    cert: str

    url: str


class ConnectorsYodleeConnectorConfigConfig(BaseModel):
    admin_login_name: str = FieldInfo(alias="adminLoginName")

    client_id: str = FieldInfo(alias="clientId")

    client_secret: str = FieldInfo(alias="clientSecret")

    env_name: Literal["sandbox", "development", "production"] = FieldInfo(alias="envName")

    proxy: Optional[ConnectorsYodleeConnectorConfigConfigProxy] = None

    sandbox_login_name: Optional[str] = FieldInfo(alias="sandboxLoginName", default=None)


class ConnectorsYodleeConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsYodleeConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsYodleeConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsYodleeConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsYodleeConnectorConfig(BaseModel):
    config: ConnectorsYodleeConnectorConfigConfig

    connector_name: Literal["yodlee"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsYodleeConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsYodleeConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


class ConnectorsZohodeskConnectorConfigConfigOAuth(BaseModel):
    client_id: str

    client_secret: str

    scopes: Optional[str] = None


class ConnectorsZohodeskConnectorConfigConfig(BaseModel):
    oauth: ConnectorsZohodeskConnectorConfigConfigOAuth


class ConnectorsZohodeskConnectorConfigConnectorSchemas(BaseModel):
    connect_input: Optional[object] = None

    connect_output: Optional[object] = None

    connection_settings: Optional[object] = None

    connector_config: Optional[object] = None

    integration_data: Optional[object] = None

    pre_connect_input: Optional[object] = None

    webhook_input: Optional[object] = None


class ConnectorsZohodeskConnectorConfigConnector(BaseModel):
    name: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop", "local", "cloud"]]] = None

    schemas: Optional[ConnectorsZohodeskConnectorConfigConnectorSchemas] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None


class ConnectorsZohodeskConnectorConfigIntegrations(BaseModel):
    connector_name: str

    name: str

    auth_type: Optional[str] = None

    category: Optional[str] = None

    logo_url: Optional[str] = None

    platforms: Optional[List[Literal["web", "mobile", "desktop"]]] = None

    stage: Optional[Literal["alpha", "beta", "ga"]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ConnectorsZohodeskConnectorConfig(BaseModel):
    config: ConnectorsZohodeskConnectorConfigConfig

    connector_name: Literal["zohodesk"]

    id: Optional[str] = None

    connection_count: Optional[float] = None

    connector: Optional[ConnectorsZohodeskConnectorConfigConnector] = None

    created_at: Optional[str] = None

    disabled: Optional[bool] = None

    display_name: Optional[str] = None

    integrations: Optional[Dict[str, ConnectorsZohodeskConnectorConfigIntegrations]] = None

    org_id: Optional[str] = None

    updated_at: Optional[str] = None


ListConnectionConfigsResponse: TypeAlias = Union[
    ConnectorsAircallConnectorConfig,
    ConnectorsAirtableConnectorConfig,
    ConnectorsApolloConnectorConfig,
    ConnectorsBrexConnectorConfig,
    ConnectorsCodaConnectorConfig,
    ConnectorsConfluenceConnectorConfig,
    ConnectorsDiscordConnectorConfig,
    ConnectorsFacebookConnectorConfig,
    ConnectorsFinchConnectorConfig,
    ConnectorsFirebaseConnectorConfig,
    ConnectorsForeceiptConnectorConfig,
    ConnectorsGitHubConnectorConfig,
    ConnectorsGongConnectorConfig,
    ConnectorsGooglecalendarConnectorConfig,
    ConnectorsGoogledocsConnectorConfig,
    ConnectorsGoogledriveConnectorConfig,
    ConnectorsGooglemailConnectorConfig,
    ConnectorsGooglesheetConnectorConfig,
    ConnectorsGreenhouseConnectorConfig,
    ConnectorsHeronConnectorConfig,
    ConnectorsHubspotConnectorConfig,
    ConnectorsInstagramConnectorConfig,
    ConnectorsIntercomConnectorConfig,
    ConnectorsJiraConnectorConfig,
    ConnectorsKustomerConnectorConfig,
    ConnectorsLeverConnectorConfig,
    ConnectorsLinearConnectorConfig,
    ConnectorsLinkedinConnectorConfig,
    ConnectorsLunchmoneyConnectorConfig,
    ConnectorsMercuryConnectorConfig,
    ConnectorsMergeConnectorConfig,
    ConnectorsMicrosoftConnectorConfig,
    ConnectorsMootaConnectorConfig,
    ConnectorsNotionConnectorConfig,
    ConnectorsOnebrickConnectorConfig,
    ConnectorsOutreachConnectorConfig,
    ConnectorsPipedriveConnectorConfig,
    ConnectorsPlaidConnectorConfig,
    ConnectorsPostgresConnectorConfig,
    ConnectorsQuickbooksConnectorConfig,
    ConnectorsRampConnectorConfig,
    ConnectorsRedditConnectorConfig,
    ConnectorsSalesforceConnectorConfig,
    ConnectorsSalesloftConnectorConfig,
    ConnectorsSaltedgeConnectorConfig,
    ConnectorsSharepointonlineConnectorConfig,
    ConnectorsSlackConnectorConfig,
    ConnectorsSplitwiseConnectorConfig,
    ConnectorsStripeConnectorConfig,
    ConnectorsTellerConnectorConfig,
    ConnectorsTogglConnectorConfig,
    ConnectorsTwentyConnectorConfig,
    ConnectorsTwitterConnectorConfig,
    ConnectorsVenmoConnectorConfig,
    ConnectorsWiseConnectorConfig,
    ConnectorsXeroConnectorConfig,
    ConnectorsYodleeConnectorConfig,
    ConnectorsZohodeskConnectorConfig,
]
