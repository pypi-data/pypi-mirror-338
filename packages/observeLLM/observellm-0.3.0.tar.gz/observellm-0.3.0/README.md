# ObserveLLM
## Installation
Install the package from PyPI using:
```bash
   pip install observeLLM
```

Note: It is recommended to use the latest version for optimal performance.

## Setup

### 1. Initialize Langfuse Client
First, initialize the Langfuse client at the application startup:

```python
from observe_traces.config.langfuse_init import LangfuseInitializer

# Initialize Langfuse client
LangfuseInitializer.initialize(
    langfuse_public_key='your_langfuse_public_key',
    langfuse_secret_key='your_langfuse_secret_key',
    langfuse_host='your_host_url',
    release='app_version',
    environment='your_environment'
)

# Optional: Close Langfuse client when shutting down
LangfuseInitializer.close()
```

### 2. Middleware Setup
Add the unified middleware to your FastAPI application in `main.py` or the appropriate entry point:

```python
from fastapi import FastAPI, Request
from observe_traces.middleware.middleware import unified_middleware

app = FastAPI()

@app.middleware("http")
async def unified_middleware_handler(request: Request, call_next):
    metadata = {
        "user_id": request.headers.get("X-User-ID"),
        "user_email": request.headers.get("X-User-Email"),
        "user_role": request.headers.get("X-User-Role"),
    }
    # Add metadata related to your application
    return await unified_middleware(request, call_next, metadata)
```

## Using Decorators for Tracing
ObserveLLM provides four decorators to enable tracing for different AI/ML components:

- @embedding_tracing → Tracks embedding model calls
- @llm_tracing → Tracks LLM (Language Model) interactions
- @reranking_tracing → Tracks reranking models used in search/retrieval
- @vectordb_tracing → Tracks vector database operations

### Example: Using the @embedding_tracing Decorator

```python
from observe_traces.tracer.embed_tracer import embedding_tracing

@embedding_tracing(provider='embedding_provider_name')
async def embedding_generation_function(model_name: str, inputs: list, **kwargs):
    # Your custom API calling logic
    # Returns either:
    # 1. Tuple of (embeddings, raw_response)
    # 2. Raw response object
```

### Example: Using the @llm_tracing Decorator

```python
from observe_traces.tracer.llm_tracer import llm_tracing

@llm_tracing(provider='llm_provider_name')
async def llm_api_calling_function(model: str, system_prompt: str, chat_messages: list, **params):
    # Your custom API calling logic
    # Returns either:
    # 1. Tuple of (response_data, raw_response)
    # 2. Raw response object
```

Required parameters for the `llm_tracing` decorator:
- `model`: The name of the LLM model being used
- `system_prompt`: The system prompt/instructions for the LLM
- `chat_messages`: The conversation history or messages to be sent to the LLM

### Example: Using the @reranking_tracing Decorator

```python
from observe_traces.tracer.rerank_tracer import reranking_tracing

@reranking_tracing(provider='reranker_provider_name')
async def reranking_function(model_name: str, query: str, documents: list, top_n: int, **kwargs):
    # Your custom API calling logic
    # Returns either:
    # 1. Tuple of (rerank_results, raw_response)
    # 2. Raw response object
```

### Example: Using the @vectordb_tracing Decorator

```python
from observe_traces.tracer.vector_tracer import vectordb_tracing

# For write operation
@vectordb_tracing(provider='pinecone', operation_type='write')
async def vectordb_write_function(index_host: str, vectors: list, namespace: str):
    # Your custom API calling logic
    # Returns raw response object

# For read operation
@vectordb_tracing(provider='pinecone', operation_type='read')
async def vectordb_read_function(
    index_host: str,
    namespace: str,
    top_k: int,
    query: str,
    query_vector_embeds: list,
    query_sparse_embeds: dict = None,
    include_metadata: bool = True,
    filter_dict: dict = None
):
    # Your custom API calling logic
    # Returns raw response object
```

## Features
- Automatic request tracing with unique trace IDs
- Comprehensive metadata tracking for each operation
- Cost calculation and token usage tracking
- Response time measurements
- Support for multiple AI/ML providers
- Flexible parameter handling with kwargs support

## Prerequisite: Self-Hosted Langfuse
To ensure proper logging and tracing, you must have a self-hosted Langfuse instance up and running. Without it, tracing will not function correctly. Configure the langfuse_host, langfuse_public_key, and langfuse_secret_key appropriately to connect your application with Langfuse.

## Note
The tracing system uses context variables to maintain request state throughout the request lifecycle. It's essential to define your methods using the specified parameters for consistency and compatibility. The decorators handle both tuple returns (response data + raw response) and single raw response returns, making them flexible for different API implementations.






