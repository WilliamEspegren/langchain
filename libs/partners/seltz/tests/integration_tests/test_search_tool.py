"""Integration tests for Seltz search tool."""

from langchain_seltz import SeltzSearchResults  # type: ignore[import-not-found]


def test_search_tool() -> None:
    """Test that the Seltz search tool works."""
    tool = SeltzSearchResults()
    res = tool.invoke({"query": "best time to visit japan", "max_documents": 5})
    print(res)  # noqa: T201
    assert not isinstance(res, str)  # str means error for this tool
    assert isinstance(res, list)
    assert len(res) > 0
    assert "url" in res[0]
    assert "content" in res[0]


def test_search_tool_default() -> None:
    """Test default behavior of the Seltz search tool."""
    tool = SeltzSearchResults()
    res = tool.invoke({"query": "python programming"})
    print(res)  # noqa: T201
    assert not isinstance(res, str)  # str means error for this tool
    assert isinstance(res, list)
    assert len(res) == 10  # default max_documents
