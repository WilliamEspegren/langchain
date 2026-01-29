"""Integration tests for `SeltzSearchRetriever`."""

from langchain_core.documents import Document  # type: ignore[import-not-found]

from langchain_seltz import SeltzSearchRetriever


def test_seltz_retriever() -> None:
    """Test basic functionality of the `SeltzSearchRetriever`."""
    retriever = SeltzSearchRetriever()
    res = retriever.invoke("best time to visit japan")
    print(res)  # noqa: T201
    assert len(res) == 10  # default k
    assert isinstance(res, list)
    assert isinstance(res[0], Document)
    assert "url" in res[0].metadata


def test_seltz_retriever_k() -> None:
    """Test k parameter of the `SeltzSearchRetriever`."""
    retriever = SeltzSearchRetriever(k=3)
    res = retriever.invoke("best time to visit japan")
    print(res)  # noqa: T201
    assert isinstance(res, list)
    assert len(res) > 0
    assert isinstance(res[0], Document)
