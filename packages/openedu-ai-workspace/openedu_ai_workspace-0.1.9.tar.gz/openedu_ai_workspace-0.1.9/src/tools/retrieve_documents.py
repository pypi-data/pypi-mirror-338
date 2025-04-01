from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langchain_openai import AzureOpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from src.config.config import settings


@tool
def retrieve_document(query: str, config: RunnableConfig, top_k: int = 5):
    """
    Retrieves documents from the knowledge base based on a given query.

    This tool utilizes a vector store to perform similarity searches on documents in the knowledge base. It takes a query string and an optional parameter for the number of top documents to retrieve. The tool returns a list of documents that are most similar to the query.

    Args:
        query (str): The query string to search for in the knowledge base.
        top_k (int, optional): The number of top documents to retrieve. Defaults to 5.
    Returns:
        list: A list of documents that are most similar to the query.
    """

    try:
        session_id = config.get("configurable", {}).get("thread_id", None)
        embeddings = AzureOpenAIEmbeddings(
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            azure_deployment="embedding",
            api_key=settings.AZURE_OPENAI_API_KEY,
            api_version=settings.AZURE_OPENAI_API_VERSION,
        )
        client = QdrantClient(
            url=settings.QDRANT_URL, api_key=settings.QDRANT_API_KEY, port=443
        )
        vector_store = QdrantVectorStore(
            client=client,
            collection_name=session_id,
            embedding=embeddings,
        )
        found_docs = vector_store.similarity_search(query, k=top_k)
        return found_docs
    except Exception as e:
        print(f"ERROR in retrieve document from source:   {e}")
        return "please try again"
