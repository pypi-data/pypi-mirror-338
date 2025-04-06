# langchain-cloudflare

This package contains the LangChain integration with CloudflareVectorize

## Installation

```bash
pip install -U langchain-cloudflare
```

And you should configure credentials by setting the following environment variables:

* TODO: fill this out

## Chat Models

`ChatCloudflareVectorize` class exposes chat models from CloudflareVectorize.

```python
from langchain_cloudflare_vectorize import ChatCloudflareVectorize

llm = ChatCloudflareVectorize()
llm.invoke("Sing a ballad of LangChain.")
```

## Embeddings

`CloudflareVectorizeEmbeddings` class exposes embeddings from CloudflareVectorize.

```python
from langchain_cloudflare_vectorize import CloudflareVectorizeEmbeddings

embeddings = CloudflareVectorizeEmbeddings()
embeddings.embed_query("What is the meaning of life?")
```

## LLMs
`CloudflareVectorizeLLM` class exposes LLMs from CloudflareVectorize.

```python
from langchain_cloudflare_vectorize import CloudflareVectorizeLLM

llm = CloudflareVectorizeLLM()
llm.invoke("The meaning of life is")
```
