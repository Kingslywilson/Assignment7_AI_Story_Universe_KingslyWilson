import os
import json
from langchain_core.prompts import ChatPromptTemplate
from models import ChoiceConsequence

class ConsequenceGenerationChain:
    def __init__(self, llm, prompt_path: str = "prompts/consequence_prompt.txt"):
        self.llm = llm
        if os.path.exists(prompt_path):
            with open(prompt_path, "r", encoding="utf-8") as f:
                template_str = f.read()
        else:
            template_str = "Evaluate consequence of choice: {user_choice} for event: {event_description}. State: {story_state}. Lore: {retrieved_lore}"
        
        self.prompt = ChatPromptTemplate.from_template(template_str)

    def run(self, story_state: str, retrieved_lore: str, event_description: str, user_choice: str) -> ChoiceConsequence:
        if hasattr(self.llm, "_llm_type") and self.llm._llm_type != "dummy-llm":
            try:
                structured_llm = self.llm.with_structured_output(ChoiceConsequence)
                chain = self.prompt | structured_llm
                result = chain.invoke({
                    "story_state": story_state,
                    "retrieved_lore": retrieved_lore,
                    "event_description": event_description,
                    "user_choice": user_choice
                })
                if isinstance(result, ChoiceConsequence):
                    return result
            except Exception:
                pass

            try:
                chain = self.prompt | self.llm
                raw_output = chain.invoke({
                    "story_state": story_state,
                    "retrieved_lore": retrieved_lore,
                    "event_description": event_description,
                    "user_choice": user_choice
                })
                text = raw_output.content if hasattr(raw_output, "content") else str(raw_output)
                start_idx = text.find("{")
                end_idx = text.rfind("}") + 1
                if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
                    clean_json = text[start_idx:end_idx]
                    data = json.loads(clean_json)
                    return ChoiceConsequence(**data)
            except Exception:
                pass

        return ChoiceConsequence(
            choice_selected=user_choice,
            immediate_consequence=f"Selecting '{user_choice}' altered the narrative course. Aetherion sustained its position, but triggered long-term diplomatic demands from surrounding allies.",
            long_term_impact="The balance of power shifted dramatically across Elyra, creating heightened tension between Aetherion, Veloria, and Dravaryn.",
            relationship_updates={"Arin Vale vs Kael Draven": "Hostility escalated following direct tactical engagement."},
            political_changes="Aetherion and Dravaryn Empire entered a state of open mobilization.",
            state_updates={"active_conflict": "Open Border War & Diplomatic Standoff", "location": "Velorian Diplomatic Enclave, Elyra"}
        )
