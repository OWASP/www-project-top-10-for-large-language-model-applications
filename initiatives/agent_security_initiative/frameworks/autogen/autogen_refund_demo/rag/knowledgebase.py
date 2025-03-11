import os
from llama_index.core  import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.embeddings.openai import OpenAIEmbedding


class RetrieverAugmenter:
    def __init__(self, data_dir=None, persist_dir=None):
        """
        Initialize the RetrieverAugmenter with data and embedding directories.
        """
        base_dir = os.path.dirname(__file__)  # Path of `knowledgebase.py`
        self.data_dir = data_dir or os.path.join(base_dir, "policy.txt")  # Default to `policy.txt`
        self.persist_dir = persist_dir or os.path.join(base_dir, "knowledgebase_embeddings")  # Embedding storage
        self.index = None

    def load_documents(self):
        """
        Load documents from the knowledgebase and build or load the embedding index.
        """
        # Check if it's a single file or a directory
        if os.path.isfile(self.data_dir):
            # Read a single file
            with open(self.data_dir, "r") as file:
                content = file.read()
            documents = [{"content": content}]
        elif os.path.isdir(self.data_dir):
            # Read all documents in the directory
            documents = SimpleDirectoryReader(self.data_dir).load_data()
        else:
            raise FileNotFoundError(f"Invalid data source: {self.data_dir}")

        self.build_index(documents)

    def build_index(self, documents):
        embedding_model = OpenAIEmbedding(model="text-embedding-ada-002")  
        print(f"Using embedding model: {embedding_model.model_name}")

        if not os.path.exists(self.persist_dir):
            print("Building a new embedding index...")
            self.index = VectorStoreIndex.from_documents(
                documents,
                embed_model=embedding_model,  # Pass the embedding model
                show_progress=True,
            )
            print("Embedding generation completed.")
            self.index.storage_context.persist(self.persist_dir)
            print(f"Index persisted to: {self.persist_dir}")
        else:
            print("Loading existing embedding index...")
            storage_context = StorageContext.from_defaults(persist_dir=self.persist_dir)
            self.index = load_index_from_storage(storage_context)

    def query(self, prompt):
        """
        Query the embedding index for a response.
        """
        if not self.index:
            raise ValueError("Index is not initialized. Call `load_documents` first.")

        # Create a query engine and run the query
        query_engine = self.index.as_query_engine()
        response = query_engine.query(prompt)
        return response.response  # Extract and return the response content
