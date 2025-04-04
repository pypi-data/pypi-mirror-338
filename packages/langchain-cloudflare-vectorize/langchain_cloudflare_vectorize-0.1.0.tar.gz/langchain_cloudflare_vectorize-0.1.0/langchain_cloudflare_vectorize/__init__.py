from importlib import metadata

from langchain_cloudflare_vectorize.chat_models import ChatCloudflareVectorize
from langchain_cloudflare_vectorize.document_loaders import CloudflareVectorizeLoader
from langchain_cloudflare_vectorize.embeddings import CloudflareVectorizeEmbeddings
from langchain_cloudflare_vectorize.retrievers import CloudflareVectorizeRetriever
from langchain_cloudflare_vectorize.toolkits import CloudflareVectorizeToolkit
from langchain_cloudflare_vectorize.tools import CloudflareVectorizeTool
from langchain_cloudflare_vectorize.vectorstores import CloudflareVectorizeVectorStore

try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""
del metadata  # optional, avoids polluting the results of dir(__package__)

__all__ = [
    "ChatCloudflareVectorize",
    "CloudflareVectorizeVectorStore",
    "CloudflareVectorizeEmbeddings",
    "CloudflareVectorizeLoader",
    "CloudflareVectorizeRetriever",
    "CloudflareVectorizeToolkit",
    "CloudflareVectorizeTool",
    "__version__",
]
