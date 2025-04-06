# LlamaVector

[![PyPI version](https://badge.fury.io/py/llamavector.svg)](https://badge.fury.io/py/llamavector)
[![Python Version](https://img.shields.io/pypi/pyversions/llamavector.svg)](https://pypi.org/project/llamavector/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/yourusername/llamavector-pkg/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/llamavector-pkg/actions/workflows/ci.yml)

Handles vector embedding generation, storage, and similarity search within the LlamaAI Ecosystem. Provides interfaces to various embedding models and vector databases.

## Features

*   **Embedding Generation**: Supports multiple embedding models (e.g., via `sentence-transformers`).
*   **Vector Storage Adapters**: Interfaces for various vector databases (e.g., FAISS, ChromaDB, Pinecone, Qdrant, Weaviate).
*   **Similarity Search**: Efficiently find vectors similar to a query vector.
*   **Data Models**: Pydantic models for structured vector data.
*   **Indexing Utilities**: Tools for building and managing vector indexes.
*   **(Optional) API**: Can expose functionality via a FastAPI server.

## Installation

```bash
# Core installation
pip install llamavector

# To install with specific vector database support (e.g., ChromaDB):
pip install llamavector[chromadb]

# To install with API support:
pip install llamavector[api]
```

## Quick Start

```python
# Example (TBD after code migration)
# from llamavector import VectorStore, EmbeddingModel

# model = EmbeddingModel(model_name='all-MiniLM-L6-v2')
# store = VectorStore(adapter='chromadb', collection_name='my_vectors')

# texts = ["This is the first document.", "This document is the second document."]
# embeddings = model.encode(texts)
# ids = ["doc1", "doc2"]

# store.add(ids=ids, embeddings=embeddings)

# query_embedding = model.encode(["A query about the second doc"])
# results = store.search(query_embeddings=query_embedding, k=1)
# print(results)
```

## Contributing

Contributions are welcome! Please see `CONTRIBUTING.md`.

## License

MIT License. See `LICENSE` file. 