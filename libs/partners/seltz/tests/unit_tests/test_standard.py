"""Standard LangChain interface tests."""

from typing import Any

from langchain_core.tools import BaseTool
from langchain_tests.unit_tests import ToolsUnitTests

from langchain_seltz import SeltzSearchResults


class TestSeltzSearchResultsStandard(ToolsUnitTests):
    """Standard unit tests for `SeltzSearchResults`."""

    @property
    def tool_constructor(self) -> type[BaseTool]:
        """Return the tool class to test."""
        return SeltzSearchResults

    @property
    def tool_constructor_params(self) -> dict[str, Any]:
        """Return params for tool construction."""
        return {"seltz_api_key": "test"}

    @property
    def tool_invoke_params_example(self) -> dict[str, Any]:
        """Return example invoke params."""
        return {"query": "best time to visit japan", "max_documents": 5}

    @property
    def init_from_env_params(
        self,
    ) -> tuple[dict[str, str], dict[str, Any], dict[str, Any]]:
        """Return env vars, init args, and expected attrs."""
        return (
            {"SELTZ_API_KEY": "test"},
            {},
            {"seltz_api_key": "test"},
        )
