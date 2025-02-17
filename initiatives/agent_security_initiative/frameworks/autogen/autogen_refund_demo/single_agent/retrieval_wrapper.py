from rag.knowledgebase import RetrieverAugmenter


def retrieve_policy(query: str) -> str:
    """
    Retrieve refund policies using the RetrieverAugmenter.
    """
    retriever = RetrieverAugmenter(
        data_dir="rag",  # Directory containing the knowledgebase (policy.txt or other docs)
        persist_dir="rag/knowledgebase_embeddings"  # Embedding storage location
    )
    retriever.load_documents()
    response = retriever.query(query)
    return response if response else "No relevant policy found."
