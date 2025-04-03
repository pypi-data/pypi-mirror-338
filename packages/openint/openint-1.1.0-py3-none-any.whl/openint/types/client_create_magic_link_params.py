# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ClientCreateMagicLinkParams"]


class ClientCreateMagicLinkParams(TypedDict, total=False):
    connection_id: str
    """The specific connection id to load"""

    connector_names: List[
        Literal[
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
    ]
    """Filter integrations by connector names"""

    redirect_url: str
    """Where to send user to after connect / if they press back button"""

    theme: Literal["light", "dark"]
    """Magic Link display theme"""

    validity_in_seconds: float
    """How long the magic link will be valid for (in seconds) before it expires"""

    view: Literal["manage", "manage-deeplink", "add", "add-deeplink"]
    """Magic Link tab view to load in the connect magic link"""
