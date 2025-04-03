# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ClientCreateConnectionParams",
    "Data",
    "DataConnectorsAircallConnectionSettings",
    "DataConnectorsAircallConnectionSettingsSettings",
    "DataConnectorsAircallConnectionSettingsSettingsOAuth",
    "DataConnectorsAircallConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsAirtableConnectionSettings",
    "DataConnectorsAirtableConnectionSettingsSettings",
    "DataConnectorsApolloConnectionSettings",
    "DataConnectorsApolloConnectionSettingsSettings",
    "DataConnectorsApolloConnectionSettingsSettingsOAuth",
    "DataConnectorsApolloConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsApolloConnectionSettingsSettingsOAuthCredentialsRaw",
    "DataConnectorsApolloConnectionSettingsSettingsOAuthConnectionConfig",
    "DataConnectorsApolloConnectionSettingsSettingsError",
    "DataConnectorsBrexConnectionSettings",
    "DataConnectorsBrexConnectionSettingsSettings",
    "DataConnectorsCodaConnectionSettings",
    "DataConnectorsCodaConnectionSettingsSettings",
    "DataConnectorsConfluenceConnectionSettings",
    "DataConnectorsConfluenceConnectionSettingsSettings",
    "DataConnectorsConfluenceConnectionSettingsSettingsOAuth",
    "DataConnectorsConfluenceConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsDiscordConnectionSettings",
    "DataConnectorsDiscordConnectionSettingsSettings",
    "DataConnectorsDiscordConnectionSettingsSettingsOAuth",
    "DataConnectorsDiscordConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsFacebookConnectionSettings",
    "DataConnectorsFacebookConnectionSettingsSettings",
    "DataConnectorsFacebookConnectionSettingsSettingsOAuth",
    "DataConnectorsFacebookConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsFacebookConnectionSettingsSettingsOAuthCredentialsRaw",
    "DataConnectorsFacebookConnectionSettingsSettingsOAuthConnectionConfig",
    "DataConnectorsFacebookConnectionSettingsSettingsError",
    "DataConnectorsFinchConnectionSettings",
    "DataConnectorsFinchConnectionSettingsSettings",
    "DataConnectorsFirebaseConnectionSettings",
    "DataConnectorsFirebaseConnectionSettingsSettings",
    "DataConnectorsFirebaseConnectionSettingsSettingsUnionMember0",
    "DataConnectorsFirebaseConnectionSettingsSettingsUnionMember0ServiceAccount",
    "DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1",
    "DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthData",
    "DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember0",
    "DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember0UserJson",
    "DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember1",
    "DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember2",
    "DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1FirebaseConfig",
    "DataConnectorsForeceiptConnectionSettings",
    "DataConnectorsForeceiptConnectionSettingsSettings",
    "DataConnectorsGitHubConnectionSettings",
    "DataConnectorsGitHubConnectionSettingsSettings",
    "DataConnectorsGitHubConnectionSettingsSettingsOAuth",
    "DataConnectorsGitHubConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsGongConnectionSettings",
    "DataConnectorsGongConnectionSettingsSettings",
    "DataConnectorsGongConnectionSettingsSettingsOAuth",
    "DataConnectorsGongConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsGongConnectionSettingsSettingsOAuthCredentialsRaw",
    "DataConnectorsGongConnectionSettingsSettingsOAuthConnectionConfig",
    "DataConnectorsGongConnectionSettingsSettingsError",
    "DataConnectorsGooglecalendarConnectionSettings",
    "DataConnectorsGooglecalendarConnectionSettingsSettings",
    "DataConnectorsGooglecalendarConnectionSettingsSettingsOAuth",
    "DataConnectorsGooglecalendarConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsGoogledocsConnectionSettings",
    "DataConnectorsGoogledocsConnectionSettingsSettings",
    "DataConnectorsGoogledocsConnectionSettingsSettingsOAuth",
    "DataConnectorsGoogledocsConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsGoogledriveConnectionSettings",
    "DataConnectorsGoogledriveConnectionSettingsSettings",
    "DataConnectorsGoogledriveConnectionSettingsSettingsOAuth",
    "DataConnectorsGoogledriveConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsGooglemailConnectionSettings",
    "DataConnectorsGooglemailConnectionSettingsSettings",
    "DataConnectorsGooglemailConnectionSettingsSettingsOAuth",
    "DataConnectorsGooglemailConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsGooglesheetConnectionSettings",
    "DataConnectorsGooglesheetConnectionSettingsSettings",
    "DataConnectorsGooglesheetConnectionSettingsSettingsOAuth",
    "DataConnectorsGooglesheetConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsGreenhouseConnectionSettings",
    "DataConnectorsGreenhouseConnectionSettingsSettings",
    "DataConnectorsHeronConnectionSettings",
    "DataConnectorsHubspotConnectionSettings",
    "DataConnectorsHubspotConnectionSettingsSettings",
    "DataConnectorsHubspotConnectionSettingsSettingsOAuth",
    "DataConnectorsHubspotConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsInstagramConnectionSettings",
    "DataConnectorsInstagramConnectionSettingsSettings",
    "DataConnectorsInstagramConnectionSettingsSettingsOAuth",
    "DataConnectorsInstagramConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsInstagramConnectionSettingsSettingsOAuthCredentialsRaw",
    "DataConnectorsInstagramConnectionSettingsSettingsOAuthConnectionConfig",
    "DataConnectorsInstagramConnectionSettingsSettingsError",
    "DataConnectorsIntercomConnectionSettings",
    "DataConnectorsIntercomConnectionSettingsSettings",
    "DataConnectorsIntercomConnectionSettingsSettingsOAuth",
    "DataConnectorsIntercomConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsIntercomConnectionSettingsSettingsOAuthCredentialsRaw",
    "DataConnectorsIntercomConnectionSettingsSettingsOAuthConnectionConfig",
    "DataConnectorsIntercomConnectionSettingsSettingsError",
    "DataConnectorsJiraConnectionSettings",
    "DataConnectorsJiraConnectionSettingsSettings",
    "DataConnectorsJiraConnectionSettingsSettingsOAuth",
    "DataConnectorsJiraConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsJiraConnectionSettingsSettingsOAuthCredentialsRaw",
    "DataConnectorsJiraConnectionSettingsSettingsOAuthConnectionConfig",
    "DataConnectorsJiraConnectionSettingsSettingsError",
    "DataConnectorsKustomerConnectionSettings",
    "DataConnectorsKustomerConnectionSettingsSettings",
    "DataConnectorsKustomerConnectionSettingsSettingsOAuth",
    "DataConnectorsKustomerConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsKustomerConnectionSettingsSettingsOAuthCredentialsRaw",
    "DataConnectorsKustomerConnectionSettingsSettingsOAuthConnectionConfig",
    "DataConnectorsKustomerConnectionSettingsSettingsError",
    "DataConnectorsLeverConnectionSettings",
    "DataConnectorsLeverConnectionSettingsSettings",
    "DataConnectorsLeverConnectionSettingsSettingsOAuth",
    "DataConnectorsLeverConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsLeverConnectionSettingsSettingsOAuthCredentialsRaw",
    "DataConnectorsLeverConnectionSettingsSettingsOAuthConnectionConfig",
    "DataConnectorsLeverConnectionSettingsSettingsError",
    "DataConnectorsLinearConnectionSettings",
    "DataConnectorsLinearConnectionSettingsSettings",
    "DataConnectorsLinearConnectionSettingsSettingsOAuth",
    "DataConnectorsLinearConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsLinkedinConnectionSettings",
    "DataConnectorsLinkedinConnectionSettingsSettings",
    "DataConnectorsLinkedinConnectionSettingsSettingsOAuth",
    "DataConnectorsLinkedinConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsLunchmoneyConnectionSettings",
    "DataConnectorsMercuryConnectionSettings",
    "DataConnectorsMergeConnectionSettings",
    "DataConnectorsMergeConnectionSettingsSettings",
    "DataConnectorsMicrosoftConnectionSettings",
    "DataConnectorsMicrosoftConnectionSettingsSettings",
    "DataConnectorsMicrosoftConnectionSettingsSettingsOAuth",
    "DataConnectorsMicrosoftConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsMicrosoftConnectionSettingsSettingsOAuthCredentialsRaw",
    "DataConnectorsMicrosoftConnectionSettingsSettingsOAuthConnectionConfig",
    "DataConnectorsMicrosoftConnectionSettingsSettingsError",
    "DataConnectorsMootaConnectionSettings",
    "DataConnectorsNotionConnectionSettings",
    "DataConnectorsNotionConnectionSettingsSettings",
    "DataConnectorsNotionConnectionSettingsSettingsOAuth",
    "DataConnectorsNotionConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsOnebrickConnectionSettings",
    "DataConnectorsOnebrickConnectionSettingsSettings",
    "DataConnectorsOutreachConnectionSettings",
    "DataConnectorsOutreachConnectionSettingsSettings",
    "DataConnectorsOutreachConnectionSettingsSettingsOAuth",
    "DataConnectorsOutreachConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsOutreachConnectionSettingsSettingsOAuthCredentialsRaw",
    "DataConnectorsOutreachConnectionSettingsSettingsOAuthConnectionConfig",
    "DataConnectorsOutreachConnectionSettingsSettingsError",
    "DataConnectorsPipedriveConnectionSettings",
    "DataConnectorsPipedriveConnectionSettingsSettings",
    "DataConnectorsPipedriveConnectionSettingsSettingsOAuth",
    "DataConnectorsPipedriveConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsPipedriveConnectionSettingsSettingsOAuthCredentialsRaw",
    "DataConnectorsPipedriveConnectionSettingsSettingsOAuthConnectionConfig",
    "DataConnectorsPipedriveConnectionSettingsSettingsError",
    "DataConnectorsPlaidConnectionSettings",
    "DataConnectorsPlaidConnectionSettingsSettings",
    "DataConnectorsPostgresConnectionSettings",
    "DataConnectorsPostgresConnectionSettingsSettings",
    "DataConnectorsPostgresConnectionSettingsSettingsSourceQueries",
    "DataConnectorsQuickbooksConnectionSettings",
    "DataConnectorsQuickbooksConnectionSettingsSettings",
    "DataConnectorsQuickbooksConnectionSettingsSettingsOAuth",
    "DataConnectorsQuickbooksConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsRampConnectionSettings",
    "DataConnectorsRampConnectionSettingsSettings",
    "DataConnectorsRedditConnectionSettings",
    "DataConnectorsRedditConnectionSettingsSettings",
    "DataConnectorsRedditConnectionSettingsSettingsOAuth",
    "DataConnectorsRedditConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsRedditConnectionSettingsSettingsOAuthCredentialsRaw",
    "DataConnectorsRedditConnectionSettingsSettingsOAuthConnectionConfig",
    "DataConnectorsRedditConnectionSettingsSettingsError",
    "DataConnectorsSalesforceConnectionSettings",
    "DataConnectorsSalesforceConnectionSettingsSettings",
    "DataConnectorsSalesforceConnectionSettingsSettingsOAuth",
    "DataConnectorsSalesforceConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsSalesloftConnectionSettings",
    "DataConnectorsSalesloftConnectionSettingsSettings",
    "DataConnectorsSalesloftConnectionSettingsSettingsOAuth",
    "DataConnectorsSalesloftConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsSalesloftConnectionSettingsSettingsOAuthCredentialsRaw",
    "DataConnectorsSalesloftConnectionSettingsSettingsOAuthConnectionConfig",
    "DataConnectorsSalesloftConnectionSettingsSettingsError",
    "DataConnectorsSaltedgeConnectionSettings",
    "DataConnectorsSharepointonlineConnectionSettings",
    "DataConnectorsSharepointonlineConnectionSettingsSettings",
    "DataConnectorsSharepointonlineConnectionSettingsSettingsOAuth",
    "DataConnectorsSharepointonlineConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsSlackConnectionSettings",
    "DataConnectorsSlackConnectionSettingsSettings",
    "DataConnectorsSlackConnectionSettingsSettingsOAuth",
    "DataConnectorsSlackConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsSplitwiseConnectionSettings",
    "DataConnectorsSplitwiseConnectionSettingsSettings",
    "DataConnectorsSplitwiseConnectionSettingsSettingsCurrentUser",
    "DataConnectorsSplitwiseConnectionSettingsSettingsCurrentUserNotifications",
    "DataConnectorsSplitwiseConnectionSettingsSettingsCurrentUserPicture",
    "DataConnectorsStripeConnectionSettings",
    "DataConnectorsStripeConnectionSettingsSettings",
    "DataConnectorsTellerConnectionSettings",
    "DataConnectorsTellerConnectionSettingsSettings",
    "DataConnectorsTogglConnectionSettings",
    "DataConnectorsTogglConnectionSettingsSettings",
    "DataConnectorsTwentyConnectionSettings",
    "DataConnectorsTwentyConnectionSettingsSettings",
    "DataConnectorsTwitterConnectionSettings",
    "DataConnectorsTwitterConnectionSettingsSettings",
    "DataConnectorsTwitterConnectionSettingsSettingsOAuth",
    "DataConnectorsTwitterConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsTwitterConnectionSettingsSettingsOAuthCredentialsRaw",
    "DataConnectorsTwitterConnectionSettingsSettingsOAuthConnectionConfig",
    "DataConnectorsTwitterConnectionSettingsSettingsError",
    "DataConnectorsVenmoConnectionSettings",
    "DataConnectorsVenmoConnectionSettingsSettings",
    "DataConnectorsWiseConnectionSettings",
    "DataConnectorsWiseConnectionSettingsSettings",
    "DataConnectorsXeroConnectionSettings",
    "DataConnectorsXeroConnectionSettingsSettings",
    "DataConnectorsXeroConnectionSettingsSettingsOAuth",
    "DataConnectorsXeroConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsXeroConnectionSettingsSettingsOAuthCredentialsRaw",
    "DataConnectorsXeroConnectionSettingsSettingsOAuthConnectionConfig",
    "DataConnectorsXeroConnectionSettingsSettingsError",
    "DataConnectorsYodleeConnectionSettings",
    "DataConnectorsYodleeConnectionSettingsSettings",
    "DataConnectorsYodleeConnectionSettingsSettingsAccessToken",
    "DataConnectorsYodleeConnectionSettingsSettingsProviderAccount",
    "DataConnectorsZohodeskConnectionSettings",
    "DataConnectorsZohodeskConnectionSettingsSettings",
    "DataConnectorsZohodeskConnectionSettingsSettingsOAuth",
    "DataConnectorsZohodeskConnectionSettingsSettingsOAuthCredentials",
    "DataConnectorsZohodeskConnectionSettingsSettingsOAuthCredentialsRaw",
    "DataConnectorsZohodeskConnectionSettingsSettingsOAuthConnectionConfig",
    "DataConnectorsZohodeskConnectionSettingsSettingsError",
]


class ClientCreateConnectionParams(TypedDict, total=False):
    connector_config_id: Required[str]
    """The id of the connector config, starts with `ccfg_`"""

    customer_id: Required[str]
    """The id of the customer in your application.

    Ensure it is unique for that customer.
    """

    data: Required[Data]
    """Connector specific data"""

    metadata: Dict[str, object]


class DataConnectorsAircallConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsAircallConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsAircallConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsAircallConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsAircallConnectionSettingsSettingsOAuth]


class DataConnectorsAircallConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["aircall"]]

    settings: Required[DataConnectorsAircallConnectionSettingsSettings]


class DataConnectorsAirtableConnectionSettingsSettings(TypedDict, total=False):
    airtable_base: Required[Annotated[str, PropertyInfo(alias="airtableBase")]]

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]


class DataConnectorsAirtableConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["airtable"]]

    settings: Required[DataConnectorsAirtableConnectionSettingsSettings]


class DataConnectorsApolloConnectionSettingsSettingsOAuthCredentialsRawTyped(TypedDict, total=False):
    access_token: Required[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    expires_in: float

    refresh_token: Optional[str]

    refresh_token_expires_in: Optional[float]

    scope: str

    token_type: Optional[str]


DataConnectorsApolloConnectionSettingsSettingsOAuthCredentialsRaw: TypeAlias = Union[
    DataConnectorsApolloConnectionSettingsSettingsOAuthCredentialsRawTyped, Dict[str, object]
]


class DataConnectorsApolloConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    raw: Required[DataConnectorsApolloConnectionSettingsSettingsOAuthCredentialsRaw]

    type: Required[Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]]

    access_token: str

    api_key: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    refresh_token: str


class DataConnectorsApolloConnectionSettingsSettingsOAuthConnectionConfigTyped(TypedDict, total=False):
    instance_url: Optional[str]

    portal_id: Annotated[Optional[float], PropertyInfo(alias="portalId")]


DataConnectorsApolloConnectionSettingsSettingsOAuthConnectionConfig: TypeAlias = Union[
    DataConnectorsApolloConnectionSettingsSettingsOAuthConnectionConfigTyped, Dict[str, object]
]


class DataConnectorsApolloConnectionSettingsSettingsOAuth(TypedDict, total=False):
    credentials: Required[DataConnectorsApolloConnectionSettingsSettingsOAuthCredentials]

    metadata: Required[Optional[Dict[str, object]]]

    connection_config: Optional[DataConnectorsApolloConnectionSettingsSettingsOAuthConnectionConfig]


class DataConnectorsApolloConnectionSettingsSettingsError(TypedDict, total=False):
    code: Required[Union[Literal["refresh_token_external_error"], str]]

    message: Optional[str]


class DataConnectorsApolloConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsApolloConnectionSettingsSettingsOAuth]

    error: Optional[DataConnectorsApolloConnectionSettingsSettingsError]


class DataConnectorsApolloConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["apollo"]]

    settings: Required[DataConnectorsApolloConnectionSettingsSettings]


class DataConnectorsBrexConnectionSettingsSettings(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="accessToken")]]


class DataConnectorsBrexConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["brex"]]

    settings: Required[DataConnectorsBrexConnectionSettingsSettings]


class DataConnectorsCodaConnectionSettingsSettings(TypedDict, total=False):
    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]


class DataConnectorsCodaConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["coda"]]

    settings: Required[DataConnectorsCodaConnectionSettingsSettings]


class DataConnectorsConfluenceConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsConfluenceConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsConfluenceConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsConfluenceConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsConfluenceConnectionSettingsSettingsOAuth]


class DataConnectorsConfluenceConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["confluence"]]

    settings: Required[DataConnectorsConfluenceConnectionSettingsSettings]


class DataConnectorsDiscordConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsDiscordConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsDiscordConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsDiscordConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsDiscordConnectionSettingsSettingsOAuth]


class DataConnectorsDiscordConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["discord"]]

    settings: Required[DataConnectorsDiscordConnectionSettingsSettings]


class DataConnectorsFacebookConnectionSettingsSettingsOAuthCredentialsRawTyped(TypedDict, total=False):
    access_token: Required[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    expires_in: float

    refresh_token: Optional[str]

    refresh_token_expires_in: Optional[float]

    scope: str

    token_type: Optional[str]


DataConnectorsFacebookConnectionSettingsSettingsOAuthCredentialsRaw: TypeAlias = Union[
    DataConnectorsFacebookConnectionSettingsSettingsOAuthCredentialsRawTyped, Dict[str, object]
]


class DataConnectorsFacebookConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    raw: Required[DataConnectorsFacebookConnectionSettingsSettingsOAuthCredentialsRaw]

    type: Required[Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]]

    access_token: str

    api_key: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    refresh_token: str


class DataConnectorsFacebookConnectionSettingsSettingsOAuthConnectionConfigTyped(TypedDict, total=False):
    instance_url: Optional[str]

    portal_id: Annotated[Optional[float], PropertyInfo(alias="portalId")]


DataConnectorsFacebookConnectionSettingsSettingsOAuthConnectionConfig: TypeAlias = Union[
    DataConnectorsFacebookConnectionSettingsSettingsOAuthConnectionConfigTyped, Dict[str, object]
]


class DataConnectorsFacebookConnectionSettingsSettingsOAuth(TypedDict, total=False):
    credentials: Required[DataConnectorsFacebookConnectionSettingsSettingsOAuthCredentials]

    metadata: Required[Optional[Dict[str, object]]]

    connection_config: Optional[DataConnectorsFacebookConnectionSettingsSettingsOAuthConnectionConfig]


class DataConnectorsFacebookConnectionSettingsSettingsError(TypedDict, total=False):
    code: Required[Union[Literal["refresh_token_external_error"], str]]

    message: Optional[str]


class DataConnectorsFacebookConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsFacebookConnectionSettingsSettingsOAuth]

    error: Optional[DataConnectorsFacebookConnectionSettingsSettingsError]


class DataConnectorsFacebookConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["facebook"]]

    settings: Required[DataConnectorsFacebookConnectionSettingsSettings]


class DataConnectorsFinchConnectionSettingsSettings(TypedDict, total=False):
    access_token: Required[str]


class DataConnectorsFinchConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["finch"]]

    settings: Required[DataConnectorsFinchConnectionSettingsSettings]


class DataConnectorsFirebaseConnectionSettingsSettingsUnionMember0ServiceAccountTyped(TypedDict, total=False):
    project_id: Required[str]


DataConnectorsFirebaseConnectionSettingsSettingsUnionMember0ServiceAccount: TypeAlias = Union[
    DataConnectorsFirebaseConnectionSettingsSettingsUnionMember0ServiceAccountTyped, Dict[str, object]
]


class DataConnectorsFirebaseConnectionSettingsSettingsUnionMember0(TypedDict, total=False):
    role: Required[Literal["admin"]]

    service_account: Required[
        Annotated[
            DataConnectorsFirebaseConnectionSettingsSettingsUnionMember0ServiceAccount,
            PropertyInfo(alias="serviceAccount"),
        ]
    ]


class DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember0UserJsonTyped(
    TypedDict, total=False
):
    app_name: Required[Annotated[str, PropertyInfo(alias="appName")]]

    sts_token_manager: Required[Annotated[Dict[str, object], PropertyInfo(alias="stsTokenManager")]]

    uid: Required[str]


DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember0UserJson: TypeAlias = Union[
    DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember0UserJsonTyped, Dict[str, object]
]


class DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember0(TypedDict, total=False):
    method: Required[Literal["userJson"]]

    user_json: Required[
        Annotated[
            DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember0UserJson,
            PropertyInfo(alias="userJson"),
        ]
    ]


class DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember1(TypedDict, total=False):
    custom_token: Required[Annotated[str, PropertyInfo(alias="customToken")]]

    method: Required[Literal["customToken"]]


class DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember2(TypedDict, total=False):
    email: Required[str]

    method: Required[Literal["emailPassword"]]

    password: Required[str]


DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthData: TypeAlias = Union[
    DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember0,
    DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember1,
    DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthDataUnionMember2,
]


class DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1FirebaseConfig(TypedDict, total=False):
    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]

    app_id: Required[Annotated[str, PropertyInfo(alias="appId")]]

    auth_domain: Required[Annotated[str, PropertyInfo(alias="authDomain")]]

    database_url: Required[Annotated[str, PropertyInfo(alias="databaseURL")]]

    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    measurement_id: Annotated[str, PropertyInfo(alias="measurementId")]

    messaging_sender_id: Annotated[str, PropertyInfo(alias="messagingSenderId")]

    storage_bucket: Annotated[str, PropertyInfo(alias="storageBucket")]


class DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1(TypedDict, total=False):
    auth_data: Required[
        Annotated[DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1AuthData, PropertyInfo(alias="authData")]
    ]

    firebase_config: Required[
        Annotated[
            DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1FirebaseConfig,
            PropertyInfo(alias="firebaseConfig"),
        ]
    ]

    role: Required[Literal["user"]]


DataConnectorsFirebaseConnectionSettingsSettings: TypeAlias = Union[
    DataConnectorsFirebaseConnectionSettingsSettingsUnionMember0,
    DataConnectorsFirebaseConnectionSettingsSettingsUnionMember1,
]


class DataConnectorsFirebaseConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["firebase"]]

    settings: Required[DataConnectorsFirebaseConnectionSettingsSettings]


class DataConnectorsForeceiptConnectionSettingsSettings(TypedDict, total=False):
    env_name: Required[Annotated[Literal["staging", "production"], PropertyInfo(alias="envName")]]

    _id: object

    credentials: object


class DataConnectorsForeceiptConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["foreceipt"]]

    settings: Required[DataConnectorsForeceiptConnectionSettingsSettings]


class DataConnectorsGitHubConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsGitHubConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsGitHubConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsGitHubConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsGitHubConnectionSettingsSettingsOAuth]


class DataConnectorsGitHubConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["github"]]

    settings: Required[DataConnectorsGitHubConnectionSettingsSettings]


class DataConnectorsGongConnectionSettingsSettingsOAuthCredentialsRawTyped(TypedDict, total=False):
    access_token: Required[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    expires_in: float

    refresh_token: Optional[str]

    refresh_token_expires_in: Optional[float]

    scope: str

    token_type: Optional[str]


DataConnectorsGongConnectionSettingsSettingsOAuthCredentialsRaw: TypeAlias = Union[
    DataConnectorsGongConnectionSettingsSettingsOAuthCredentialsRawTyped, Dict[str, object]
]


class DataConnectorsGongConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    raw: Required[DataConnectorsGongConnectionSettingsSettingsOAuthCredentialsRaw]

    type: Required[Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]]

    access_token: str

    api_key: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    refresh_token: str


class DataConnectorsGongConnectionSettingsSettingsOAuthConnectionConfigTyped(TypedDict, total=False):
    instance_url: Optional[str]

    portal_id: Annotated[Optional[float], PropertyInfo(alias="portalId")]


DataConnectorsGongConnectionSettingsSettingsOAuthConnectionConfig: TypeAlias = Union[
    DataConnectorsGongConnectionSettingsSettingsOAuthConnectionConfigTyped, Dict[str, object]
]


class DataConnectorsGongConnectionSettingsSettingsOAuth(TypedDict, total=False):
    credentials: Required[DataConnectorsGongConnectionSettingsSettingsOAuthCredentials]

    metadata: Required[Optional[Dict[str, object]]]

    connection_config: Optional[DataConnectorsGongConnectionSettingsSettingsOAuthConnectionConfig]


class DataConnectorsGongConnectionSettingsSettingsError(TypedDict, total=False):
    code: Required[Union[Literal["refresh_token_external_error"], str]]

    message: Optional[str]


class DataConnectorsGongConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsGongConnectionSettingsSettingsOAuth]

    error: Optional[DataConnectorsGongConnectionSettingsSettingsError]


class DataConnectorsGongConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["gong"]]

    settings: Required[DataConnectorsGongConnectionSettingsSettings]


class DataConnectorsGooglecalendarConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsGooglecalendarConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsGooglecalendarConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsGooglecalendarConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsGooglecalendarConnectionSettingsSettingsOAuth]


class DataConnectorsGooglecalendarConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["googlecalendar"]]

    settings: Required[DataConnectorsGooglecalendarConnectionSettingsSettings]


class DataConnectorsGoogledocsConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsGoogledocsConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsGoogledocsConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsGoogledocsConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsGoogledocsConnectionSettingsSettingsOAuth]


class DataConnectorsGoogledocsConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["googledocs"]]

    settings: Required[DataConnectorsGoogledocsConnectionSettingsSettings]


class DataConnectorsGoogledriveConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsGoogledriveConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsGoogledriveConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsGoogledriveConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsGoogledriveConnectionSettingsSettingsOAuth]


class DataConnectorsGoogledriveConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["googledrive"]]

    settings: Required[DataConnectorsGoogledriveConnectionSettingsSettings]


class DataConnectorsGooglemailConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsGooglemailConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsGooglemailConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsGooglemailConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsGooglemailConnectionSettingsSettingsOAuth]


class DataConnectorsGooglemailConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["googlemail"]]

    settings: Required[DataConnectorsGooglemailConnectionSettingsSettings]


class DataConnectorsGooglesheetConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsGooglesheetConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsGooglesheetConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsGooglesheetConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsGooglesheetConnectionSettingsSettingsOAuth]


class DataConnectorsGooglesheetConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["googlesheet"]]

    settings: Required[DataConnectorsGooglesheetConnectionSettingsSettings]


class DataConnectorsGreenhouseConnectionSettingsSettings(TypedDict, total=False):
    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]


class DataConnectorsGreenhouseConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["greenhouse"]]

    settings: Required[DataConnectorsGreenhouseConnectionSettingsSettings]


class DataConnectorsHeronConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["heron"]]

    settings: Required[None]


class DataConnectorsHubspotConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsHubspotConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsHubspotConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsHubspotConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsHubspotConnectionSettingsSettingsOAuth]


class DataConnectorsHubspotConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["hubspot"]]

    settings: Required[DataConnectorsHubspotConnectionSettingsSettings]


class DataConnectorsInstagramConnectionSettingsSettingsOAuthCredentialsRawTyped(TypedDict, total=False):
    access_token: Required[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    expires_in: float

    refresh_token: Optional[str]

    refresh_token_expires_in: Optional[float]

    scope: str

    token_type: Optional[str]


DataConnectorsInstagramConnectionSettingsSettingsOAuthCredentialsRaw: TypeAlias = Union[
    DataConnectorsInstagramConnectionSettingsSettingsOAuthCredentialsRawTyped, Dict[str, object]
]


class DataConnectorsInstagramConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    raw: Required[DataConnectorsInstagramConnectionSettingsSettingsOAuthCredentialsRaw]

    type: Required[Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]]

    access_token: str

    api_key: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    refresh_token: str


class DataConnectorsInstagramConnectionSettingsSettingsOAuthConnectionConfigTyped(TypedDict, total=False):
    instance_url: Optional[str]

    portal_id: Annotated[Optional[float], PropertyInfo(alias="portalId")]


DataConnectorsInstagramConnectionSettingsSettingsOAuthConnectionConfig: TypeAlias = Union[
    DataConnectorsInstagramConnectionSettingsSettingsOAuthConnectionConfigTyped, Dict[str, object]
]


class DataConnectorsInstagramConnectionSettingsSettingsOAuth(TypedDict, total=False):
    credentials: Required[DataConnectorsInstagramConnectionSettingsSettingsOAuthCredentials]

    metadata: Required[Optional[Dict[str, object]]]

    connection_config: Optional[DataConnectorsInstagramConnectionSettingsSettingsOAuthConnectionConfig]


class DataConnectorsInstagramConnectionSettingsSettingsError(TypedDict, total=False):
    code: Required[Union[Literal["refresh_token_external_error"], str]]

    message: Optional[str]


class DataConnectorsInstagramConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsInstagramConnectionSettingsSettingsOAuth]

    error: Optional[DataConnectorsInstagramConnectionSettingsSettingsError]


class DataConnectorsInstagramConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["instagram"]]

    settings: Required[DataConnectorsInstagramConnectionSettingsSettings]


class DataConnectorsIntercomConnectionSettingsSettingsOAuthCredentialsRawTyped(TypedDict, total=False):
    access_token: Required[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    expires_in: float

    refresh_token: Optional[str]

    refresh_token_expires_in: Optional[float]

    scope: str

    token_type: Optional[str]


DataConnectorsIntercomConnectionSettingsSettingsOAuthCredentialsRaw: TypeAlias = Union[
    DataConnectorsIntercomConnectionSettingsSettingsOAuthCredentialsRawTyped, Dict[str, object]
]


class DataConnectorsIntercomConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    raw: Required[DataConnectorsIntercomConnectionSettingsSettingsOAuthCredentialsRaw]

    type: Required[Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]]

    access_token: str

    api_key: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    refresh_token: str


class DataConnectorsIntercomConnectionSettingsSettingsOAuthConnectionConfigTyped(TypedDict, total=False):
    instance_url: Optional[str]

    portal_id: Annotated[Optional[float], PropertyInfo(alias="portalId")]


DataConnectorsIntercomConnectionSettingsSettingsOAuthConnectionConfig: TypeAlias = Union[
    DataConnectorsIntercomConnectionSettingsSettingsOAuthConnectionConfigTyped, Dict[str, object]
]


class DataConnectorsIntercomConnectionSettingsSettingsOAuth(TypedDict, total=False):
    credentials: Required[DataConnectorsIntercomConnectionSettingsSettingsOAuthCredentials]

    metadata: Required[Optional[Dict[str, object]]]

    connection_config: Optional[DataConnectorsIntercomConnectionSettingsSettingsOAuthConnectionConfig]


class DataConnectorsIntercomConnectionSettingsSettingsError(TypedDict, total=False):
    code: Required[Union[Literal["refresh_token_external_error"], str]]

    message: Optional[str]


class DataConnectorsIntercomConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsIntercomConnectionSettingsSettingsOAuth]

    error: Optional[DataConnectorsIntercomConnectionSettingsSettingsError]


class DataConnectorsIntercomConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["intercom"]]

    settings: Required[DataConnectorsIntercomConnectionSettingsSettings]


class DataConnectorsJiraConnectionSettingsSettingsOAuthCredentialsRawTyped(TypedDict, total=False):
    access_token: Required[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    expires_in: float

    refresh_token: Optional[str]

    refresh_token_expires_in: Optional[float]

    scope: str

    token_type: Optional[str]


DataConnectorsJiraConnectionSettingsSettingsOAuthCredentialsRaw: TypeAlias = Union[
    DataConnectorsJiraConnectionSettingsSettingsOAuthCredentialsRawTyped, Dict[str, object]
]


class DataConnectorsJiraConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    raw: Required[DataConnectorsJiraConnectionSettingsSettingsOAuthCredentialsRaw]

    type: Required[Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]]

    access_token: str

    api_key: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    refresh_token: str


class DataConnectorsJiraConnectionSettingsSettingsOAuthConnectionConfigTyped(TypedDict, total=False):
    instance_url: Optional[str]

    portal_id: Annotated[Optional[float], PropertyInfo(alias="portalId")]


DataConnectorsJiraConnectionSettingsSettingsOAuthConnectionConfig: TypeAlias = Union[
    DataConnectorsJiraConnectionSettingsSettingsOAuthConnectionConfigTyped, Dict[str, object]
]


class DataConnectorsJiraConnectionSettingsSettingsOAuth(TypedDict, total=False):
    credentials: Required[DataConnectorsJiraConnectionSettingsSettingsOAuthCredentials]

    metadata: Required[Optional[Dict[str, object]]]

    connection_config: Optional[DataConnectorsJiraConnectionSettingsSettingsOAuthConnectionConfig]


class DataConnectorsJiraConnectionSettingsSettingsError(TypedDict, total=False):
    code: Required[Union[Literal["refresh_token_external_error"], str]]

    message: Optional[str]


class DataConnectorsJiraConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsJiraConnectionSettingsSettingsOAuth]

    error: Optional[DataConnectorsJiraConnectionSettingsSettingsError]


class DataConnectorsJiraConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["jira"]]

    settings: Required[DataConnectorsJiraConnectionSettingsSettings]


class DataConnectorsKustomerConnectionSettingsSettingsOAuthCredentialsRawTyped(TypedDict, total=False):
    access_token: Required[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    expires_in: float

    refresh_token: Optional[str]

    refresh_token_expires_in: Optional[float]

    scope: str

    token_type: Optional[str]


DataConnectorsKustomerConnectionSettingsSettingsOAuthCredentialsRaw: TypeAlias = Union[
    DataConnectorsKustomerConnectionSettingsSettingsOAuthCredentialsRawTyped, Dict[str, object]
]


class DataConnectorsKustomerConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    raw: Required[DataConnectorsKustomerConnectionSettingsSettingsOAuthCredentialsRaw]

    type: Required[Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]]

    access_token: str

    api_key: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    refresh_token: str


class DataConnectorsKustomerConnectionSettingsSettingsOAuthConnectionConfigTyped(TypedDict, total=False):
    instance_url: Optional[str]

    portal_id: Annotated[Optional[float], PropertyInfo(alias="portalId")]


DataConnectorsKustomerConnectionSettingsSettingsOAuthConnectionConfig: TypeAlias = Union[
    DataConnectorsKustomerConnectionSettingsSettingsOAuthConnectionConfigTyped, Dict[str, object]
]


class DataConnectorsKustomerConnectionSettingsSettingsOAuth(TypedDict, total=False):
    credentials: Required[DataConnectorsKustomerConnectionSettingsSettingsOAuthCredentials]

    metadata: Required[Optional[Dict[str, object]]]

    connection_config: Optional[DataConnectorsKustomerConnectionSettingsSettingsOAuthConnectionConfig]


class DataConnectorsKustomerConnectionSettingsSettingsError(TypedDict, total=False):
    code: Required[Union[Literal["refresh_token_external_error"], str]]

    message: Optional[str]


class DataConnectorsKustomerConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsKustomerConnectionSettingsSettingsOAuth]

    error: Optional[DataConnectorsKustomerConnectionSettingsSettingsError]


class DataConnectorsKustomerConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["kustomer"]]

    settings: Required[DataConnectorsKustomerConnectionSettingsSettings]


class DataConnectorsLeverConnectionSettingsSettingsOAuthCredentialsRawTyped(TypedDict, total=False):
    access_token: Required[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    expires_in: float

    refresh_token: Optional[str]

    refresh_token_expires_in: Optional[float]

    scope: str

    token_type: Optional[str]


DataConnectorsLeverConnectionSettingsSettingsOAuthCredentialsRaw: TypeAlias = Union[
    DataConnectorsLeverConnectionSettingsSettingsOAuthCredentialsRawTyped, Dict[str, object]
]


class DataConnectorsLeverConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    raw: Required[DataConnectorsLeverConnectionSettingsSettingsOAuthCredentialsRaw]

    type: Required[Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]]

    access_token: str

    api_key: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    refresh_token: str


class DataConnectorsLeverConnectionSettingsSettingsOAuthConnectionConfigTyped(TypedDict, total=False):
    instance_url: Optional[str]

    portal_id: Annotated[Optional[float], PropertyInfo(alias="portalId")]


DataConnectorsLeverConnectionSettingsSettingsOAuthConnectionConfig: TypeAlias = Union[
    DataConnectorsLeverConnectionSettingsSettingsOAuthConnectionConfigTyped, Dict[str, object]
]


class DataConnectorsLeverConnectionSettingsSettingsOAuth(TypedDict, total=False):
    credentials: Required[DataConnectorsLeverConnectionSettingsSettingsOAuthCredentials]

    metadata: Required[Optional[Dict[str, object]]]

    connection_config: Optional[DataConnectorsLeverConnectionSettingsSettingsOAuthConnectionConfig]


class DataConnectorsLeverConnectionSettingsSettingsError(TypedDict, total=False):
    code: Required[Union[Literal["refresh_token_external_error"], str]]

    message: Optional[str]


class DataConnectorsLeverConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsLeverConnectionSettingsSettingsOAuth]

    error: Optional[DataConnectorsLeverConnectionSettingsSettingsError]


class DataConnectorsLeverConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["lever"]]

    settings: Required[DataConnectorsLeverConnectionSettingsSettings]


class DataConnectorsLinearConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsLinearConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsLinearConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsLinearConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsLinearConnectionSettingsSettingsOAuth]


class DataConnectorsLinearConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["linear"]]

    settings: Required[DataConnectorsLinearConnectionSettingsSettings]


class DataConnectorsLinkedinConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsLinkedinConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsLinkedinConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsLinkedinConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsLinkedinConnectionSettingsSettingsOAuth]


class DataConnectorsLinkedinConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["linkedin"]]

    settings: Required[DataConnectorsLinkedinConnectionSettingsSettings]


class DataConnectorsLunchmoneyConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["lunchmoney"]]

    settings: Required[None]


class DataConnectorsMercuryConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["mercury"]]

    settings: Required[None]


class DataConnectorsMergeConnectionSettingsSettings(TypedDict, total=False):
    account_token: Required[Annotated[str, PropertyInfo(alias="accountToken")]]

    account_details: Annotated[object, PropertyInfo(alias="accountDetails")]


class DataConnectorsMergeConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["merge"]]

    settings: Required[DataConnectorsMergeConnectionSettingsSettings]


class DataConnectorsMicrosoftConnectionSettingsSettingsOAuthCredentialsRawTyped(TypedDict, total=False):
    access_token: Required[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    expires_in: float

    refresh_token: Optional[str]

    refresh_token_expires_in: Optional[float]

    scope: str

    token_type: Optional[str]


DataConnectorsMicrosoftConnectionSettingsSettingsOAuthCredentialsRaw: TypeAlias = Union[
    DataConnectorsMicrosoftConnectionSettingsSettingsOAuthCredentialsRawTyped, Dict[str, object]
]


class DataConnectorsMicrosoftConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    raw: Required[DataConnectorsMicrosoftConnectionSettingsSettingsOAuthCredentialsRaw]

    type: Required[Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]]

    access_token: str

    api_key: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    refresh_token: str


class DataConnectorsMicrosoftConnectionSettingsSettingsOAuthConnectionConfigTyped(TypedDict, total=False):
    instance_url: Optional[str]

    portal_id: Annotated[Optional[float], PropertyInfo(alias="portalId")]


DataConnectorsMicrosoftConnectionSettingsSettingsOAuthConnectionConfig: TypeAlias = Union[
    DataConnectorsMicrosoftConnectionSettingsSettingsOAuthConnectionConfigTyped, Dict[str, object]
]


class DataConnectorsMicrosoftConnectionSettingsSettingsOAuth(TypedDict, total=False):
    credentials: Required[DataConnectorsMicrosoftConnectionSettingsSettingsOAuthCredentials]

    metadata: Required[Optional[Dict[str, object]]]

    connection_config: Optional[DataConnectorsMicrosoftConnectionSettingsSettingsOAuthConnectionConfig]


class DataConnectorsMicrosoftConnectionSettingsSettingsError(TypedDict, total=False):
    code: Required[Union[Literal["refresh_token_external_error"], str]]

    message: Optional[str]


class DataConnectorsMicrosoftConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsMicrosoftConnectionSettingsSettingsOAuth]

    client_id: str

    error: Optional[DataConnectorsMicrosoftConnectionSettingsSettingsError]


class DataConnectorsMicrosoftConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["microsoft"]]

    settings: Required[DataConnectorsMicrosoftConnectionSettingsSettings]


class DataConnectorsMootaConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["moota"]]

    settings: Required[None]


class DataConnectorsNotionConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsNotionConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsNotionConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsNotionConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsNotionConnectionSettingsSettingsOAuth]


class DataConnectorsNotionConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["notion"]]

    settings: Required[DataConnectorsNotionConnectionSettingsSettings]


class DataConnectorsOnebrickConnectionSettingsSettings(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="accessToken")]]


class DataConnectorsOnebrickConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["onebrick"]]

    settings: Required[DataConnectorsOnebrickConnectionSettingsSettings]


class DataConnectorsOutreachConnectionSettingsSettingsOAuthCredentialsRawTyped(TypedDict, total=False):
    access_token: Required[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    expires_in: float

    refresh_token: Optional[str]

    refresh_token_expires_in: Optional[float]

    scope: str

    token_type: Optional[str]


DataConnectorsOutreachConnectionSettingsSettingsOAuthCredentialsRaw: TypeAlias = Union[
    DataConnectorsOutreachConnectionSettingsSettingsOAuthCredentialsRawTyped, Dict[str, object]
]


class DataConnectorsOutreachConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    raw: Required[DataConnectorsOutreachConnectionSettingsSettingsOAuthCredentialsRaw]

    type: Required[Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]]

    access_token: str

    api_key: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    refresh_token: str


class DataConnectorsOutreachConnectionSettingsSettingsOAuthConnectionConfigTyped(TypedDict, total=False):
    instance_url: Optional[str]

    portal_id: Annotated[Optional[float], PropertyInfo(alias="portalId")]


DataConnectorsOutreachConnectionSettingsSettingsOAuthConnectionConfig: TypeAlias = Union[
    DataConnectorsOutreachConnectionSettingsSettingsOAuthConnectionConfigTyped, Dict[str, object]
]


class DataConnectorsOutreachConnectionSettingsSettingsOAuth(TypedDict, total=False):
    credentials: Required[DataConnectorsOutreachConnectionSettingsSettingsOAuthCredentials]

    metadata: Required[Optional[Dict[str, object]]]

    connection_config: Optional[DataConnectorsOutreachConnectionSettingsSettingsOAuthConnectionConfig]


class DataConnectorsOutreachConnectionSettingsSettingsError(TypedDict, total=False):
    code: Required[Union[Literal["refresh_token_external_error"], str]]

    message: Optional[str]


class DataConnectorsOutreachConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsOutreachConnectionSettingsSettingsOAuth]

    error: Optional[DataConnectorsOutreachConnectionSettingsSettingsError]


class DataConnectorsOutreachConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["outreach"]]

    settings: Required[DataConnectorsOutreachConnectionSettingsSettings]


class DataConnectorsPipedriveConnectionSettingsSettingsOAuthCredentialsRawTyped(TypedDict, total=False):
    access_token: Required[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    expires_in: float

    refresh_token: Optional[str]

    refresh_token_expires_in: Optional[float]

    scope: str

    token_type: Optional[str]


DataConnectorsPipedriveConnectionSettingsSettingsOAuthCredentialsRaw: TypeAlias = Union[
    DataConnectorsPipedriveConnectionSettingsSettingsOAuthCredentialsRawTyped, Dict[str, object]
]


class DataConnectorsPipedriveConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    raw: Required[DataConnectorsPipedriveConnectionSettingsSettingsOAuthCredentialsRaw]

    type: Required[Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]]

    access_token: str

    api_key: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    refresh_token: str


class DataConnectorsPipedriveConnectionSettingsSettingsOAuthConnectionConfigTyped(TypedDict, total=False):
    instance_url: Optional[str]

    portal_id: Annotated[Optional[float], PropertyInfo(alias="portalId")]


DataConnectorsPipedriveConnectionSettingsSettingsOAuthConnectionConfig: TypeAlias = Union[
    DataConnectorsPipedriveConnectionSettingsSettingsOAuthConnectionConfigTyped, Dict[str, object]
]


class DataConnectorsPipedriveConnectionSettingsSettingsOAuth(TypedDict, total=False):
    credentials: Required[DataConnectorsPipedriveConnectionSettingsSettingsOAuthCredentials]

    metadata: Required[Optional[Dict[str, object]]]

    connection_config: Optional[DataConnectorsPipedriveConnectionSettingsSettingsOAuthConnectionConfig]


class DataConnectorsPipedriveConnectionSettingsSettingsError(TypedDict, total=False):
    code: Required[Union[Literal["refresh_token_external_error"], str]]

    message: Optional[str]


class DataConnectorsPipedriveConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsPipedriveConnectionSettingsSettingsOAuth]

    error: Optional[DataConnectorsPipedriveConnectionSettingsSettingsError]


class DataConnectorsPipedriveConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["pipedrive"]]

    settings: Required[DataConnectorsPipedriveConnectionSettingsSettings]


class DataConnectorsPlaidConnectionSettingsSettings(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="accessToken")]]

    institution: object

    item: object

    item_id: Annotated[Optional[str], PropertyInfo(alias="itemId")]

    status: object

    webhook_item_error: Annotated[None, PropertyInfo(alias="webhookItemError")]


class DataConnectorsPlaidConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["plaid"]]

    settings: Required[DataConnectorsPlaidConnectionSettingsSettings]


class DataConnectorsPostgresConnectionSettingsSettingsSourceQueries(TypedDict, total=False):
    invoice: Optional[str]
    """Should order by lastModifiedAt and id descending"""


class DataConnectorsPostgresConnectionSettingsSettings(TypedDict, total=False):
    database_url: Required[Annotated[str, PropertyInfo(alias="databaseUrl")]]

    source_queries: Annotated[
        DataConnectorsPostgresConnectionSettingsSettingsSourceQueries, PropertyInfo(alias="sourceQueries")
    ]


class DataConnectorsPostgresConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["postgres"]]

    settings: Required[DataConnectorsPostgresConnectionSettingsSettings]


class DataConnectorsQuickbooksConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsQuickbooksConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsQuickbooksConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsQuickbooksConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsQuickbooksConnectionSettingsSettingsOAuth]

    realm_id: Required[Annotated[str, PropertyInfo(alias="realmId")]]
    """The realmId of your quickbooks company (e.g., 9341453474484455)"""


class DataConnectorsQuickbooksConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["quickbooks"]]

    settings: Required[DataConnectorsQuickbooksConnectionSettingsSettings]


class DataConnectorsRampConnectionSettingsSettings(TypedDict, total=False):
    access_token: Annotated[Optional[str], PropertyInfo(alias="accessToken")]

    start_after_transaction_id: Annotated[Optional[str], PropertyInfo(alias="startAfterTransactionId")]


class DataConnectorsRampConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["ramp"]]

    settings: Required[DataConnectorsRampConnectionSettingsSettings]


class DataConnectorsRedditConnectionSettingsSettingsOAuthCredentialsRawTyped(TypedDict, total=False):
    access_token: Required[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    expires_in: float

    refresh_token: Optional[str]

    refresh_token_expires_in: Optional[float]

    scope: str

    token_type: Optional[str]


DataConnectorsRedditConnectionSettingsSettingsOAuthCredentialsRaw: TypeAlias = Union[
    DataConnectorsRedditConnectionSettingsSettingsOAuthCredentialsRawTyped, Dict[str, object]
]


class DataConnectorsRedditConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    raw: Required[DataConnectorsRedditConnectionSettingsSettingsOAuthCredentialsRaw]

    type: Required[Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]]

    access_token: str

    api_key: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    refresh_token: str


class DataConnectorsRedditConnectionSettingsSettingsOAuthConnectionConfigTyped(TypedDict, total=False):
    instance_url: Optional[str]

    portal_id: Annotated[Optional[float], PropertyInfo(alias="portalId")]


DataConnectorsRedditConnectionSettingsSettingsOAuthConnectionConfig: TypeAlias = Union[
    DataConnectorsRedditConnectionSettingsSettingsOAuthConnectionConfigTyped, Dict[str, object]
]


class DataConnectorsRedditConnectionSettingsSettingsOAuth(TypedDict, total=False):
    credentials: Required[DataConnectorsRedditConnectionSettingsSettingsOAuthCredentials]

    metadata: Required[Optional[Dict[str, object]]]

    connection_config: Optional[DataConnectorsRedditConnectionSettingsSettingsOAuthConnectionConfig]


class DataConnectorsRedditConnectionSettingsSettingsError(TypedDict, total=False):
    code: Required[Union[Literal["refresh_token_external_error"], str]]

    message: Optional[str]


class DataConnectorsRedditConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsRedditConnectionSettingsSettingsOAuth]

    error: Optional[DataConnectorsRedditConnectionSettingsSettingsError]


class DataConnectorsRedditConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["reddit"]]

    settings: Required[DataConnectorsRedditConnectionSettingsSettings]


class DataConnectorsSalesforceConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsSalesforceConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsSalesforceConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsSalesforceConnectionSettingsSettings(TypedDict, total=False):
    instance_url: Required[str]
    """The instance URL of your Salesforce account (e.g., example)"""

    oauth: Required[DataConnectorsSalesforceConnectionSettingsSettingsOAuth]


class DataConnectorsSalesforceConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["salesforce"]]

    settings: Required[DataConnectorsSalesforceConnectionSettingsSettings]


class DataConnectorsSalesloftConnectionSettingsSettingsOAuthCredentialsRawTyped(TypedDict, total=False):
    access_token: Required[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    expires_in: float

    refresh_token: Optional[str]

    refresh_token_expires_in: Optional[float]

    scope: str

    token_type: Optional[str]


DataConnectorsSalesloftConnectionSettingsSettingsOAuthCredentialsRaw: TypeAlias = Union[
    DataConnectorsSalesloftConnectionSettingsSettingsOAuthCredentialsRawTyped, Dict[str, object]
]


class DataConnectorsSalesloftConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    raw: Required[DataConnectorsSalesloftConnectionSettingsSettingsOAuthCredentialsRaw]

    type: Required[Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]]

    access_token: str

    api_key: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    refresh_token: str


class DataConnectorsSalesloftConnectionSettingsSettingsOAuthConnectionConfigTyped(TypedDict, total=False):
    instance_url: Optional[str]

    portal_id: Annotated[Optional[float], PropertyInfo(alias="portalId")]


DataConnectorsSalesloftConnectionSettingsSettingsOAuthConnectionConfig: TypeAlias = Union[
    DataConnectorsSalesloftConnectionSettingsSettingsOAuthConnectionConfigTyped, Dict[str, object]
]


class DataConnectorsSalesloftConnectionSettingsSettingsOAuth(TypedDict, total=False):
    credentials: Required[DataConnectorsSalesloftConnectionSettingsSettingsOAuthCredentials]

    metadata: Required[Optional[Dict[str, object]]]

    connection_config: Optional[DataConnectorsSalesloftConnectionSettingsSettingsOAuthConnectionConfig]


class DataConnectorsSalesloftConnectionSettingsSettingsError(TypedDict, total=False):
    code: Required[Union[Literal["refresh_token_external_error"], str]]

    message: Optional[str]


class DataConnectorsSalesloftConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsSalesloftConnectionSettingsSettingsOAuth]

    error: Optional[DataConnectorsSalesloftConnectionSettingsSettingsError]


class DataConnectorsSalesloftConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["salesloft"]]

    settings: Required[DataConnectorsSalesloftConnectionSettingsSettings]


class DataConnectorsSaltedgeConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["saltedge"]]

    settings: object


class DataConnectorsSharepointonlineConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsSharepointonlineConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsSharepointonlineConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsSharepointonlineConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsSharepointonlineConnectionSettingsSettingsOAuth]


class DataConnectorsSharepointonlineConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["sharepointonline"]]

    settings: Required[DataConnectorsSharepointonlineConnectionSettingsSettings]


class DataConnectorsSlackConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    access_token: Required[str]

    client_id: Required[str]

    raw: Required[Dict[str, object]]

    scope: Required[str]

    expires_at: str

    expires_in: float

    refresh_token: str

    token_type: str


class DataConnectorsSlackConnectionSettingsSettingsOAuth(TypedDict, total=False):
    created_at: Required[str]

    last_fetched_at: Required[str]

    metadata: Required[Optional[Dict[str, object]]]

    updated_at: Required[str]

    credentials: DataConnectorsSlackConnectionSettingsSettingsOAuthCredentials
    """Output of the postConnect hook for oauth2 connectors"""


class DataConnectorsSlackConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsSlackConnectionSettingsSettingsOAuth]


class DataConnectorsSlackConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["slack"]]

    settings: Required[DataConnectorsSlackConnectionSettingsSettings]


class DataConnectorsSplitwiseConnectionSettingsSettingsCurrentUserNotifications(TypedDict, total=False):
    added_as_friend: Required[bool]

    added_to_group: Required[bool]

    announcements: Required[bool]

    bills: Required[bool]

    expense_added: Required[bool]

    expense_updated: Required[bool]

    monthly_summary: Required[bool]

    payments: Required[bool]


class DataConnectorsSplitwiseConnectionSettingsSettingsCurrentUserPicture(TypedDict, total=False):
    large: Optional[str]

    medium: Optional[str]

    original: Optional[str]

    small: Optional[str]

    xlarge: Optional[str]

    xxlarge: Optional[str]


class DataConnectorsSplitwiseConnectionSettingsSettingsCurrentUser(TypedDict, total=False):
    id: Required[float]

    country_code: Required[str]

    custom_picture: Required[bool]

    date_format: Required[str]

    default_currency: Required[str]

    default_group_id: Required[float]

    email: Required[str]

    first_name: Required[str]

    force_refresh_at: Required[str]

    last_name: Required[str]

    locale: Required[str]

    notifications: Required[DataConnectorsSplitwiseConnectionSettingsSettingsCurrentUserNotifications]

    notifications_count: Required[float]

    notifications_read: Required[str]

    picture: Required[DataConnectorsSplitwiseConnectionSettingsSettingsCurrentUserPicture]

    registration_status: Required[str]


class DataConnectorsSplitwiseConnectionSettingsSettings(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="accessToken")]]

    current_user: Annotated[
        Optional[DataConnectorsSplitwiseConnectionSettingsSettingsCurrentUser], PropertyInfo(alias="currentUser")
    ]


class DataConnectorsSplitwiseConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["splitwise"]]

    settings: Required[DataConnectorsSplitwiseConnectionSettingsSettings]


class DataConnectorsStripeConnectionSettingsSettings(TypedDict, total=False):
    secret_key: Required[Annotated[str, PropertyInfo(alias="secretKey")]]


class DataConnectorsStripeConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["stripe"]]

    settings: Required[DataConnectorsStripeConnectionSettingsSettings]


class DataConnectorsTellerConnectionSettingsSettings(TypedDict, total=False):
    token: Required[str]


class DataConnectorsTellerConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["teller"]]

    settings: Required[DataConnectorsTellerConnectionSettingsSettings]


class DataConnectorsTogglConnectionSettingsSettings(TypedDict, total=False):
    api_token: Required[Annotated[str, PropertyInfo(alias="apiToken")]]

    email: Optional[str]

    password: Optional[str]


class DataConnectorsTogglConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["toggl"]]

    settings: Required[DataConnectorsTogglConnectionSettingsSettings]


class DataConnectorsTwentyConnectionSettingsSettings(TypedDict, total=False):
    access_token: Required[str]


class DataConnectorsTwentyConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["twenty"]]

    settings: Required[DataConnectorsTwentyConnectionSettingsSettings]


class DataConnectorsTwitterConnectionSettingsSettingsOAuthCredentialsRawTyped(TypedDict, total=False):
    access_token: Required[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    expires_in: float

    refresh_token: Optional[str]

    refresh_token_expires_in: Optional[float]

    scope: str

    token_type: Optional[str]


DataConnectorsTwitterConnectionSettingsSettingsOAuthCredentialsRaw: TypeAlias = Union[
    DataConnectorsTwitterConnectionSettingsSettingsOAuthCredentialsRawTyped, Dict[str, object]
]


class DataConnectorsTwitterConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    raw: Required[DataConnectorsTwitterConnectionSettingsSettingsOAuthCredentialsRaw]

    type: Required[Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]]

    access_token: str

    api_key: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    refresh_token: str


class DataConnectorsTwitterConnectionSettingsSettingsOAuthConnectionConfigTyped(TypedDict, total=False):
    instance_url: Optional[str]

    portal_id: Annotated[Optional[float], PropertyInfo(alias="portalId")]


DataConnectorsTwitterConnectionSettingsSettingsOAuthConnectionConfig: TypeAlias = Union[
    DataConnectorsTwitterConnectionSettingsSettingsOAuthConnectionConfigTyped, Dict[str, object]
]


class DataConnectorsTwitterConnectionSettingsSettingsOAuth(TypedDict, total=False):
    credentials: Required[DataConnectorsTwitterConnectionSettingsSettingsOAuthCredentials]

    metadata: Required[Optional[Dict[str, object]]]

    connection_config: Optional[DataConnectorsTwitterConnectionSettingsSettingsOAuthConnectionConfig]


class DataConnectorsTwitterConnectionSettingsSettingsError(TypedDict, total=False):
    code: Required[Union[Literal["refresh_token_external_error"], str]]

    message: Optional[str]


class DataConnectorsTwitterConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsTwitterConnectionSettingsSettingsOAuth]

    error: Optional[DataConnectorsTwitterConnectionSettingsSettingsError]


class DataConnectorsTwitterConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["twitter"]]

    settings: Required[DataConnectorsTwitterConnectionSettingsSettings]


class DataConnectorsVenmoConnectionSettingsSettings(TypedDict, total=False):
    credentials: object

    me: object


class DataConnectorsVenmoConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["venmo"]]

    settings: Required[DataConnectorsVenmoConnectionSettingsSettings]


class DataConnectorsWiseConnectionSettingsSettings(TypedDict, total=False):
    env_name: Required[Annotated[Literal["sandbox", "live"], PropertyInfo(alias="envName")]]

    api_token: Annotated[Optional[str], PropertyInfo(alias="apiToken")]


class DataConnectorsWiseConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["wise"]]

    settings: Required[DataConnectorsWiseConnectionSettingsSettings]


class DataConnectorsXeroConnectionSettingsSettingsOAuthCredentialsRawTyped(TypedDict, total=False):
    access_token: Required[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    expires_in: float

    refresh_token: Optional[str]

    refresh_token_expires_in: Optional[float]

    scope: str

    token_type: Optional[str]


DataConnectorsXeroConnectionSettingsSettingsOAuthCredentialsRaw: TypeAlias = Union[
    DataConnectorsXeroConnectionSettingsSettingsOAuthCredentialsRawTyped, Dict[str, object]
]


class DataConnectorsXeroConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    raw: Required[DataConnectorsXeroConnectionSettingsSettingsOAuthCredentialsRaw]

    type: Required[Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]]

    access_token: str

    api_key: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    refresh_token: str


class DataConnectorsXeroConnectionSettingsSettingsOAuthConnectionConfigTyped(TypedDict, total=False):
    instance_url: Optional[str]

    portal_id: Annotated[Optional[float], PropertyInfo(alias="portalId")]


DataConnectorsXeroConnectionSettingsSettingsOAuthConnectionConfig: TypeAlias = Union[
    DataConnectorsXeroConnectionSettingsSettingsOAuthConnectionConfigTyped, Dict[str, object]
]


class DataConnectorsXeroConnectionSettingsSettingsOAuth(TypedDict, total=False):
    credentials: Required[DataConnectorsXeroConnectionSettingsSettingsOAuthCredentials]

    metadata: Required[Optional[Dict[str, object]]]

    connection_config: Optional[DataConnectorsXeroConnectionSettingsSettingsOAuthConnectionConfig]


class DataConnectorsXeroConnectionSettingsSettingsError(TypedDict, total=False):
    code: Required[Union[Literal["refresh_token_external_error"], str]]

    message: Optional[str]


class DataConnectorsXeroConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsXeroConnectionSettingsSettingsOAuth]

    error: Optional[DataConnectorsXeroConnectionSettingsSettingsError]


class DataConnectorsXeroConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["xero"]]

    settings: Required[DataConnectorsXeroConnectionSettingsSettings]


class DataConnectorsYodleeConnectionSettingsSettingsAccessToken(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="accessToken")]]

    expires_in: Required[Annotated[float, PropertyInfo(alias="expiresIn")]]

    issued_at: Required[Annotated[str, PropertyInfo(alias="issuedAt")]]


class DataConnectorsYodleeConnectionSettingsSettingsProviderAccount(TypedDict, total=False):
    id: Required[float]

    aggregation_source: Required[Annotated[str, PropertyInfo(alias="aggregationSource")]]

    created_date: Required[Annotated[str, PropertyInfo(alias="createdDate")]]

    dataset: Required[Iterable[object]]

    is_manual: Required[Annotated[bool, PropertyInfo(alias="isManual")]]

    provider_id: Required[Annotated[float, PropertyInfo(alias="providerId")]]

    status: Required[
        Literal["LOGIN_IN_PROGRESS", "USER_INPUT_REQUIRED", "IN_PROGRESS", "PARTIAL_SUCCESS", "SUCCESS", "FAILED"]
    ]

    is_deleted: Annotated[Optional[bool], PropertyInfo(alias="isDeleted")]


class DataConnectorsYodleeConnectionSettingsSettings(TypedDict, total=False):
    login_name: Required[Annotated[str, PropertyInfo(alias="loginName")]]

    provider_account_id: Required[Annotated[Union[float, str], PropertyInfo(alias="providerAccountId")]]

    access_token: Annotated[
        Optional[DataConnectorsYodleeConnectionSettingsSettingsAccessToken], PropertyInfo(alias="accessToken")
    ]

    provider: None

    provider_account: Annotated[
        Optional[DataConnectorsYodleeConnectionSettingsSettingsProviderAccount], PropertyInfo(alias="providerAccount")
    ]

    user: None


class DataConnectorsYodleeConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["yodlee"]]

    settings: Required[DataConnectorsYodleeConnectionSettingsSettings]


class DataConnectorsZohodeskConnectionSettingsSettingsOAuthCredentialsRawTyped(TypedDict, total=False):
    access_token: Required[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    expires_in: float

    refresh_token: Optional[str]

    refresh_token_expires_in: Optional[float]

    scope: str

    token_type: Optional[str]


DataConnectorsZohodeskConnectionSettingsSettingsOAuthCredentialsRaw: TypeAlias = Union[
    DataConnectorsZohodeskConnectionSettingsSettingsOAuthCredentialsRawTyped, Dict[str, object]
]


class DataConnectorsZohodeskConnectionSettingsSettingsOAuthCredentials(TypedDict, total=False):
    raw: Required[DataConnectorsZohodeskConnectionSettingsSettingsOAuthCredentialsRaw]

    type: Required[Literal["OAUTH2", "OAUTH1", "BASIC", "API_KEY"]]

    access_token: str

    api_key: Optional[str]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    refresh_token: str


class DataConnectorsZohodeskConnectionSettingsSettingsOAuthConnectionConfigTyped(TypedDict, total=False):
    instance_url: Optional[str]

    portal_id: Annotated[Optional[float], PropertyInfo(alias="portalId")]


DataConnectorsZohodeskConnectionSettingsSettingsOAuthConnectionConfig: TypeAlias = Union[
    DataConnectorsZohodeskConnectionSettingsSettingsOAuthConnectionConfigTyped, Dict[str, object]
]


class DataConnectorsZohodeskConnectionSettingsSettingsOAuth(TypedDict, total=False):
    credentials: Required[DataConnectorsZohodeskConnectionSettingsSettingsOAuthCredentials]

    metadata: Required[Optional[Dict[str, object]]]

    connection_config: Optional[DataConnectorsZohodeskConnectionSettingsSettingsOAuthConnectionConfig]


class DataConnectorsZohodeskConnectionSettingsSettingsError(TypedDict, total=False):
    code: Required[Union[Literal["refresh_token_external_error"], str]]

    message: Optional[str]


class DataConnectorsZohodeskConnectionSettingsSettings(TypedDict, total=False):
    oauth: Required[DataConnectorsZohodeskConnectionSettingsSettingsOAuth]

    error: Optional[DataConnectorsZohodeskConnectionSettingsSettingsError]


class DataConnectorsZohodeskConnectionSettings(TypedDict, total=False):
    connector_name: Required[Literal["zohodesk"]]

    settings: Required[DataConnectorsZohodeskConnectionSettingsSettings]


Data: TypeAlias = Union[
    DataConnectorsAircallConnectionSettings,
    DataConnectorsAirtableConnectionSettings,
    DataConnectorsApolloConnectionSettings,
    DataConnectorsBrexConnectionSettings,
    DataConnectorsCodaConnectionSettings,
    DataConnectorsConfluenceConnectionSettings,
    DataConnectorsDiscordConnectionSettings,
    DataConnectorsFacebookConnectionSettings,
    DataConnectorsFinchConnectionSettings,
    DataConnectorsFirebaseConnectionSettings,
    DataConnectorsForeceiptConnectionSettings,
    DataConnectorsGitHubConnectionSettings,
    DataConnectorsGongConnectionSettings,
    DataConnectorsGooglecalendarConnectionSettings,
    DataConnectorsGoogledocsConnectionSettings,
    DataConnectorsGoogledriveConnectionSettings,
    DataConnectorsGooglemailConnectionSettings,
    DataConnectorsGooglesheetConnectionSettings,
    DataConnectorsGreenhouseConnectionSettings,
    DataConnectorsHeronConnectionSettings,
    DataConnectorsHubspotConnectionSettings,
    DataConnectorsInstagramConnectionSettings,
    DataConnectorsIntercomConnectionSettings,
    DataConnectorsJiraConnectionSettings,
    DataConnectorsKustomerConnectionSettings,
    DataConnectorsLeverConnectionSettings,
    DataConnectorsLinearConnectionSettings,
    DataConnectorsLinkedinConnectionSettings,
    DataConnectorsLunchmoneyConnectionSettings,
    DataConnectorsMercuryConnectionSettings,
    DataConnectorsMergeConnectionSettings,
    DataConnectorsMicrosoftConnectionSettings,
    DataConnectorsMootaConnectionSettings,
    DataConnectorsNotionConnectionSettings,
    DataConnectorsOnebrickConnectionSettings,
    DataConnectorsOutreachConnectionSettings,
    DataConnectorsPipedriveConnectionSettings,
    DataConnectorsPlaidConnectionSettings,
    DataConnectorsPostgresConnectionSettings,
    DataConnectorsQuickbooksConnectionSettings,
    DataConnectorsRampConnectionSettings,
    DataConnectorsRedditConnectionSettings,
    DataConnectorsSalesforceConnectionSettings,
    DataConnectorsSalesloftConnectionSettings,
    DataConnectorsSaltedgeConnectionSettings,
    DataConnectorsSharepointonlineConnectionSettings,
    DataConnectorsSlackConnectionSettings,
    DataConnectorsSplitwiseConnectionSettings,
    DataConnectorsStripeConnectionSettings,
    DataConnectorsTellerConnectionSettings,
    DataConnectorsTogglConnectionSettings,
    DataConnectorsTwentyConnectionSettings,
    DataConnectorsTwitterConnectionSettings,
    DataConnectorsVenmoConnectionSettings,
    DataConnectorsWiseConnectionSettings,
    DataConnectorsXeroConnectionSettings,
    DataConnectorsYodleeConnectionSettings,
    DataConnectorsZohodeskConnectionSettings,
]
