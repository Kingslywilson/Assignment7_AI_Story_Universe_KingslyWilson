import os
from typing import List, Dict, Any
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

class VectorStoreManager:
    def __init__(self, persistence_dir: str = "data/lore", model_name: str = "all-MiniLM-L6-v2"):
        self.persistence_dir = persistence_dir
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        self.vector_store = None
        self._initialize_store()

    def _initialize_store(self):
        os.makedirs(self.persistence_dir, exist_ok=True)
        faiss_index_path = os.path.join(self.persistence_dir, "index.faiss")
        if os.path.exists(faiss_index_path):
            self.vector_store = FAISS.load_local(
                self.persistence_dir, 
                self.embeddings, 
                allow_dangerous_deserialization=True
            )
        else:
            initial_doc = Document(
                page_content="Genesis of the Universe lore store.", 
                metadata={"type": "system", "chapter": 0}
            )
            self.vector_store = FAISS.from_documents([initial_doc], self.embeddings)
            self.save()

    def add_lore(self, text: str, metadata: Dict[str, Any]):
        doc = Document(page_content=text, metadata=metadata)
        self.vector_store.add_documents([doc])
        self.save()

    def add_lore_documents(self, documents: List[Document]):
        self.vector_store.add_documents(documents)
        self.save()

    def similarity_search(self, query: str, k: int = 4, filter_dict: Dict[str, Any] = None) -> List[Document]:
        return self.vector_store.similarity_search(query, k=k, filter=filter_dict)

    def as_retriever(self, k: int = 4):
        return self.vector_store.as_retriever(search_kwargs={"k": k})

    def save(self):
        os.makedirs(self.persistence_dir, exist_ok=True)
        self.vector_store.save_local(self.persistence_dir)
