"""Utilities for the Seltz integration."""

import os

from langchain_core.utils import convert_to_secret_str
from seltz import Seltz  # type: ignore[import-untyped]


def initialize_client(values: dict) -> dict:
    """Initialize the Seltz client.

    Args:
        values: Configuration values for the client.

    Returns:
        Updated values dict with initialized client.
    """
    seltz_api_key = values.get("seltz_api_key") or os.environ.get("SELTZ_API_KEY") or ""
    values["seltz_api_key"] = convert_to_secret_str(seltz_api_key)
    args: dict = {
        "api_key": values["seltz_api_key"].get_secret_value(),
    }
    if values.get("seltz_endpoint"):
        args["endpoint"] = values["seltz_endpoint"]
    if values.get("seltz_insecure") is not None:
        args["insecure"] = values["seltz_insecure"]
    values["client"] = Seltz(**args)
    return values
