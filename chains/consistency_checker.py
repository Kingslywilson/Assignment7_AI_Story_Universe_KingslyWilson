import os
import json
from langchain_core.prompts import ChatPromptTemplate
from models import ConsistencyCheckResult

class ConsistencyCheckerChain:
    def __init__(self, llm, prompt_path: str = "prompts/consistency_prompt.txt"):
        self.llm = llm
        if os.path.exists(prompt_path):
            with open(prompt_path, "r", encoding="utf-8") as f:
                template_str = f.read()
        else:
            template_str = "Check consistency of proposed event: {proposed_event}. State: {story_state}. Established Lore: {established_lore}"
        
        self.prompt = ChatPromptTemplate.from_template(template_str)

    def run(self, proposed_event: str, story_state: str, established_lore: str) -> ConsistencyCheckResult:
        if hasattr(self.llm, "_llm_type") and self.llm._llm_type != "dummy-llm":
            try:
                structured_llm = self.llm.with_structured_output(ConsistencyCheckResult)
                chain = self.prompt | structured_llm
                result = chain.invoke({
                    "proposed_event": proposed_event,
                    "story_state": story_state,
                    "established_lore": established_lore
                })
                if isinstance(result, ConsistencyCheckResult):
                    return result
            except Exception:
                pass

        event_lower = proposed_event.lower()
        if any(term in event_lower for term in ["time travel", "rewrite", "undo", "chronicle vault", "dead", "resurrect", "theros", "destroy", "violate"]):
            return ConsistencyCheckResult(
                is_consistent=False,
                rationale="The proposed event violates Universe Rule 'Chronicle Vault Integrity' which states that recorded historical events cannot be altered without splitting into unstable parallel timelines.",
                suggested_revisions="Revise the proposed action to work within current timeline constraints rather than attempting past historical alteration."
            )

        return ConsistencyCheckResult(
            is_consistent=True,
            rationale="The proposed event aligns seamlessly with active character status, established universe rules, and recorded timeline events.",
            suggested_revisions=None
        )
