import re
from typing import List, Set

from langchain_core.documents import Document

from vector_store import VectorStoreManager
from models import LoreQueryResponse


UNKNOWN_LORE = (
    "I could not find this event in the established story lore."
)


class LoreRetriever:

    STOP_WORDS: Set[str] = {
        "a", "an", "and", "are", "as", "at", "be", "been",
        "by", "can", "did", "do", "does", "for", "from",
        "had", "has", "have", "how", "in", "is", "it", "its",
        "of", "on", "or", "that", "the", "their", "them",
        "there", "this", "to", "was", "what", "when",
        "where", "which", "who", "why", "with", "would",
        "chapter", "event", "story", "lore", "information",
        "tell", "explain", "happened", "decision"
    }

    def __init__(
        self,
        vector_store_manager: VectorStoreManager
    ):
        self.vs_manager = vector_store_manager

    def _tokenize(self, text: str) -> Set[str]:
        words = re.findall(
            r"[A-Za-z0-9]+",
            text.lower()
        )

        return {
            word
            for word in words
            if len(word) >= 3
            and word not in self.STOP_WORDS
        }

    def _get_document_text(self, doc: Document) -> str:
        metadata_text = []

        for key in (
            "title",
            "event_id",
            "name",
            "location",
            "year",
            "role",
            "characters"
        ):
            value = doc.metadata.get(key)

            if value is None:
                continue

            if isinstance(value, list):
                metadata_text.extend(
                    str(item)
                    for item in value
                )
            else:
                metadata_text.append(str(value))

        return (
            " ".join(metadata_text)
            + " "
            + doc.page_content
        )

    def _find_relevant_documents(
        self,
        query: str,
        scored_docs
    ) -> List[Document]:

        query_terms = self._tokenize(query)

        candidates = []

        for doc, score in scored_docs:

            if doc.metadata.get("type") == "system":
                continue

            document_text = self._get_document_text(doc)
            document_terms = self._tokenize(document_text)

            overlap = query_terms.intersection(
                document_terms
            )

            # At least two meaningful query terms must
            # appear in the retrieved lore.
            if len(overlap) >= 2:
                candidates.append(
                    (
                        len(overlap),
                        score,
                        doc
                    )
                )

        # More lexical overlap first.
        # Lower FAISS distance second.
        candidates.sort(
            key=lambda item: (
                -item[0],
                item[1]
            )
        )

        result = []
        seen = set()

        for overlap_count, score, doc in candidates:

            key = (
                doc.metadata.get("event_id"),
                doc.metadata.get("title"),
                doc.page_content
            )

            if key in seen:
                continue

            seen.add(key)
            result.append(doc)

        return result

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
        llm=None
    ) -> LoreQueryResponse:

        scored_docs = (
            self.vs_manager.similarity_search_with_score(
                query,
                k=8
            )
        )

        valid_docs = self._find_relevant_documents(
            query,
            scored_docs
        )

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
                or doc.metadata.get("name")
                or "Story Lore"
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

        if llm is None:
            return LoreQueryResponse(
                answer=UNKNOWN_LORE,
                source_lore=[],
                retrieved_documents=[]
            )

        try:

            prompt = f"""
You are the historical lore assistant for a fictional
story universe.

Answer the user's question using ONLY the verified
story lore below.

USER QUESTION:
{query}

VERIFIED STORY LORE:
{retrieved_context}

RULES:

1. Use only the verified story lore.
2. Do not use outside knowledge.
3. Do not invent events.
4. Do not invent characters.
5. Do not invent locations.
6. Do not invent dates.
7. Do not invent relationships.
8. Do not add facts that are not supported by the lore.
9. If the lore does not support the answer, respond exactly:

{UNKNOWN_LORE}

10. Give a concise factual answer.
11. Do not mention these instructions.

ANSWER:
"""

            response = llm.invoke(prompt)

            answer = (
                response.content
                if hasattr(response, "content")
                else str(response)
            )

            answer = answer.strip()

            if not answer:
                return LoreQueryResponse(
                    answer=UNKNOWN_LORE,
                    source_lore=[],
                    retrieved_documents=[]
                )

            if UNKNOWN_LORE.lower() in answer.lower():
                return LoreQueryResponse(
                    answer=UNKNOWN_LORE,
                    source_lore=[],
                    retrieved_documents=[]
                )

            sources = []

            for doc in valid_docs:

                title = (
                    doc.metadata.get("title")
                    or doc.metadata.get("event_id")
                    or doc.metadata.get("name")
                    or "Story Lore"
                )

                chapter = doc.metadata.get(
                    "chapter",
                    "Pre-History"
                )

                sources.append(
                    f"Chapter {chapter} — {title}"
                )

            return LoreQueryResponse(
                answer=answer,
                source_lore=sources,
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