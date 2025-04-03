# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ClientListConnectionConfigsParams"]


class ClientListConnectionConfigsParams(TypedDict, total=False):
    connector_name: Literal[
        "aircall",
        "airtable",
        "apollo",
        "brex",
        "coda",
        "confluence",
        "discord",
        "facebook",
        "finch",
        "firebase",
        "foreceipt",
        "github",
        "gong",
        "googlecalendar",
        "googledocs",
        "googledrive",
        "googlemail",
        "googlesheet",
        "greenhouse",
        "heron",
        "hubspot",
        "instagram",
        "intercom",
        "jira",
        "kustomer",
        "lever",
        "linear",
        "linkedin",
        "lunchmoney",
        "merge",
        "microsoft",
        "moota",
        "notion",
        "onebrick",
        "outreach",
        "pipedrive",
        "plaid",
        "quickbooks",
        "ramp",
        "reddit",
        "salesforce",
        "salesloft",
        "saltedge",
        "sharepointonline",
        "slack",
        "splitwise",
        "stripe",
        "teller",
        "toggl",
        "twenty",
        "twitter",
        "wise",
        "xero",
        "yodlee",
        "zohodesk",
    ]
    """The name of the connector"""

    expand: str
    """Comma separated list of fields to optionally expand.

    Available Options: `connector`, `enabled_integrations`
    """

    limit: int
    """Limit the number of items returned"""

    offset: int
    """Offset the items returned"""
