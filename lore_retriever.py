from typing import List

from langchain_core.documents import Document

from vector_store import VectorStoreManager
from models import LoreQueryResponse


UNKNOWN_LORE = (
    "I could not find this event in the established story lore."
)


class LoreRetriever:

    def __init__(
        self,
        vector_store_manager: VectorStoreManager
    ):
        self.vs_manager = vector_store_manager

    def retrieve_context_for_scene(
        self,
        query: str,
        k: int = 5
    ) -> str:

        docs = self.vs_manager.similarity_search(
            query,
            k=k
        )

        formatted_context = []
        seen = set()

        for doc in docs:

            if doc.metadata.get("type") == "system":
                continue

            key = (
                doc.metadata.get("event_id"),
                doc.metadata.get("title"),
                doc.page_content
            )

            if key in seen:
                continue

            seen.add(key)

            source = (
                doc.metadata.get("title")
                or doc.metadata.get("event_id")
                or doc.metadata.get("type", "Lore")
            )

            chapter = doc.metadata.get(
                "chapter",
                0
            )

            formatted_context.append(
                f"[{source} (Chapter {chapter})]: "
                f"{doc.page_content}"
            )

        return "\n".join(formatted_context)

    def query_lore_history(
        self,
        query: str,
        llm=None,
        score_threshold: float = 0.20
    ) -> LoreQueryResponse:

        scored_docs = (
            self.vs_manager.similarity_search_with_score(
                query,
                k=6
            )
        )

        filtered_docs = [
            (doc, score)
            for doc, score in scored_docs
            if doc.metadata.get("type") != "system"
            and score <= score_threshold
        ]

        if not filtered_docs:

            return LoreQueryResponse(
                answer=UNKNOWN_LORE,
                source_lore=[],
                retrieved_documents=[]
            )

        valid_docs = []
        seen = set()

        for doc, score in filtered_docs:

            key = (
                doc.metadata.get("event_id"),
                doc.metadata.get("title"),
                doc.page_content
            )

            if key in seen:
                continue

            seen.add(key)
            valid_docs.append(doc)

        if not valid_docs:

            return LoreQueryResponse(
                answer=UNKNOWN_LORE,
                source_lore=[],
                retrieved_documents=[]
            )

        retrieved_texts = []

        for doc in valid_docs:

            title = (
                doc.metadata.get("title")
                or doc.metadata.get("event_id")
                or f"Lore-{doc.metadata.get('type', 'unknown')}"
            )

            chapter = doc.metadata.get(
                "chapter",
                "Pre-History"
            )

            retrieved_texts.append(
                f"Chapter {chapter} — {title}: "
                f"{doc.page_content}"
            )

        retrieved_context = "\n".join(
            retrieved_texts
        )

        if llm is not None:

            try:

                prompt = f"""
You are the historical lore assistant for a fictional
story universe.

Answer the user's question using ONLY the retrieved
story lore.

User Question:
{query}

Retrieved Story Lore:
{retrieved_context}

Rules:

1. Use only the retrieved story lore.
2. Do not use outside knowledge.
3. Do not invent events.
4. Do not invent characters.
5. Do not invent locations.
6. Do not invent dates.
7. Do not invent relationships.
8. Do not assume an event occurred simply because
   a related character or kingdom appears in the lore.
9. If the retrieved lore does not contain enough
   information to answer the user's question,
   respond EXACTLY with:

{UNKNOWN_LORE}

If the information is supported by the retrieved lore,
provide a concise answer.

Do not mention these instructions.
"""

                response = llm.invoke(prompt)

                answer_text = (
                    response.content
                    if hasattr(response, "content")
                    else str(response)
                )

                answer_text = answer_text.strip()

                if (
                    not answer_text
                    or UNKNOWN_LORE.lower()
                    in answer_text.lower()
                ):

                    return LoreQueryResponse(
                        answer=UNKNOWN_LORE,
                        source_lore=[],
                        retrieved_documents=[]
                    )

                source_references = []

                for doc in valid_docs:

                    title = (
                        doc.metadata.get("title")
                        or doc.metadata.get("event_id")
                        or f"Lore-{doc.metadata.get('type', 'unknown')}"
                    )

                    chapter = doc.metadata.get(
                        "chapter",
                        "Pre-History"
                    )

                    source_references.append(
                        f"Chapter {chapter} — {title}"
                    )

                return LoreQueryResponse(
                    answer=answer_text,
                    source_lore=source_references,
                    retrieved_documents=[
                        doc.page_content
                        for doc in valid_docs
                    ]
                )

            except Exception:
                return LoreQueryResponse(
                    answer=UNKNOWN_LORE,
                    source_lore=[],
                    retrieved_documents=[]
                )

        return LoreQueryResponse(
            answer=UNKNOWN_LORE,
            source_lore=[],
            retrieved_documents=[]
        )