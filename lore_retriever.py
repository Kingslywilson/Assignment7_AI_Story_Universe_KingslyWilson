from typing import List
from langchain_core.documents import Document

from vector_store import VectorStoreManager
from models import LoreQueryResponse


class LoreRetriever:
    def __init__(self, vector_store_manager: VectorStoreManager):
        self.vs_manager = vector_store_manager

    def retrieve_context_for_scene(self, query: str, k: int = 5) -> str:
        """
        Retrieve relevant lore for generating a new story scene.
        """
        docs = self.vs_manager.similarity_search(query, k=k)

        formatted_context = []

        for doc in docs:
            source = (
                doc.metadata.get("title")
                or doc.metadata.get("event_id")
                or doc.metadata.get("type", "Lore")
            )

            chapter = doc.metadata.get("chapter", 0)

            formatted_context.append(
                f"[{source} (Chapter {chapter})]: {doc.page_content}"
            )

        return "\n".join(formatted_context)

    def query_lore_history(
        self,
        query: str,
        llm=None,
        score_threshold: float = 0.5
    ) -> LoreQueryResponse:
        """
        Retrieve historical lore relevant to the user's query.

        The method relies on FAISS semantic retrieval rather than
        hardcoded test questions.
        """

        docs = self.vs_manager.similarity_search(query, k=4)

        valid_docs = [
            doc
            for doc in docs
            if doc.metadata.get("type") != "system"
        ]

        if not valid_docs:
            return LoreQueryResponse(
                answer="I could not find this event in the established story lore.",
                source_lore=[],
                retrieved_documents=[]
            )

        source_references = []
        retrieved_texts = []

        for doc in valid_docs:
            title = (
                doc.metadata.get("title")
                or doc.metadata.get("event_id")
                or f"Lore-{doc.metadata.get('type', 'unknown')}"
            )

            chapter = doc.metadata.get("chapter", "Pre-History")

            reference = f"Chapter {chapter} — {title}"

            source_references.append(reference)

            retrieved_texts.append(
                f"({reference}) {doc.page_content}"
            )

        if llm is not None:
            try:
                prompt = f"""
You are the historical lore assistant for a fictional story universe.

Answer the user's question using ONLY the retrieved story lore below.

Rules:
- Do not use outside knowledge.
- Do not invent events.
- Do not create characters, locations, dates, or relationships that
  are not supported by the retrieved lore.
- If the retrieved lore does not contain enough information to answer
  the question, respond exactly with:

I could not find this event in the established story lore.

Retrieved Story Lore:
{chr(10).join(retrieved_texts)}

User Question:
{query}
"""

                response = llm.invoke(prompt)

                answer_text = (
                    response.content
                    if hasattr(response, "content")
                    else str(response)
                )

                if answer_text and answer_text.strip():
                    return LoreQueryResponse(
                        answer=answer_text.strip(),
                        source_lore=source_references,
                        retrieved_documents=[
                            doc.page_content for doc in valid_docs
                        ]
                    )

            except Exception:
                pass

        answer_text = (
            "Based on the retrieved story lore:\n"
            + "\n".join(
                f"- {doc.page_content}"
                for doc in valid_docs[:2]
            )
        )

        return LoreQueryResponse(
            answer=answer_text,
            source_lore=source_references,
            retrieved_documents=[
                doc.page_content for doc in valid_docs
            ]
        )