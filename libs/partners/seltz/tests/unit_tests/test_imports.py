"""Unit tests for imports in `langchain_seltz`."""

from langchain_seltz import __all__  # type: ignore[import-not-found]

EXPECTED_ALL = [
    "SeltzSearchResults",
    "SeltzSearchRetriever",
]


def test_all_imports() -> None:
    """Test that all expected imports are in `__all__`."""
    assert sorted(EXPECTED_ALL) == sorted(__all__)
