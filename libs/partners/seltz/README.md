# langchain-seltz

[![PyPI - Version](https://img.shields.io/pypi/v/langchain-seltz?label=%20)](https://pypi.org/project/langchain-seltz/#history)
[![PyPI - License](https://img.shields.io/pypi/l/langchain-seltz)](https://opensource.org/licenses/MIT)
[![PyPI - Downloads](https://img.shields.io/pepy/dt/langchain-seltz)](https://pypistats.org/packages/langchain-seltz)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/langchain.svg?style=social&label=Follow%20%40LangChain)](https://x.com/langchain)

Looking for the JS/TS version? Check out [LangChain.js](https://github.com/langchain-ai/langchainjs).

## Quick Install

```bash
pip install langchain-seltz
```

## What is this?

This package contains the LangChain integration with [Seltz](https://seltz.ai?utm_source=langchain), a web knowledge search API providing fast, context-engineered web content for AI reasoning.

## Usage

### Search Tool

```python
from langchain_seltz import SeltzSearchResults

tool = SeltzSearchResults()
results = tool.invoke({"query": "best time to visit japan", "max_documents": 5})
# Returns list of dicts with 'url' and 'content' keys
```

### Retriever

```python
from langchain_seltz import SeltzSearchRetriever

retriever = SeltzSearchRetriever(k=5)
docs = retriever.invoke("best time to visit japan")
# Returns list of Document objects
```

## Configuration

Set your API key as an environment variable:

```bash
export SELTZ_API_KEY="your-api-key"
```

Or pass it directly:

```python
tool = SeltzSearchResults(seltz_api_key="your-api-key")
retriever = SeltzSearchRetriever(seltz_api_key="your-api-key")
```
