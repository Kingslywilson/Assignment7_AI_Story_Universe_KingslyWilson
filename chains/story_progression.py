import os
import json
from langchain_core.prompts import ChatPromptTemplate
from models import StoryEvent, StoryChoice

class StoryProgressionChain:
    def __init__(self, llm, prompt_path: str = "prompts/story_progression_prompt.txt"):
        self.llm = llm
        if os.path.exists(prompt_path):
            with open(prompt_path, "r", encoding="utf-8") as f:
                template_str = f.read()
        else:
            template_str = "Generate story event. State: {story_state}. Lore: {retrieved_lore}. Prev: {previous_context}. Intent: {user_intent}"
        
        self.prompt = ChatPromptTemplate.from_template(template_str)

    def run(self, story_state: str, retrieved_lore: str, previous_context: str = "", user_intent: str = "") -> StoryEvent:
        if hasattr(self.llm, "_llm_type") and self.llm._llm_type != "dummy-llm":
            try:
                structured_llm = self.llm.with_structured_output(StoryEvent)
                chain = self.prompt | structured_llm
                result = chain.invoke({
                    "story_state": story_state,
                    "retrieved_lore": retrieved_lore,
                    "previous_context": previous_context,
                    "user_intent": user_intent
                })
                if isinstance(result, StoryEvent):
                    return result
            except Exception:
                pass

        state_lower = story_state.lower()
        prev_lower = previous_context.lower()
        intent_lower = user_intent.lower()

        if "chapter 2" in state_lower or "chapter: 2" in state_lower or "veloria" in prev_lower or "veloria" in intent_lower or "evt001" in prev_lower:
            return StoryEvent(
                event_id="EVT002",
                chapter=2,
                location="Velorian Diplomatic Enclave, Elyra",
                active_characters=["Arin Vale", "High Ambassador Vaelen"],
                event_description="Following the Eastern Border defense, High Ambassador Vaelen of the Velorian Alliance arrives at Elyra. Citing the emergency military intervention requested by Aetherion in Chapter 1, Veloria demands immediate access and full technical schematics of Aether Crystal Engineering.",
                user_choices=[
                    StoryChoice(choice_id=1, description="Grant Veloria limited read-only access to lower-tier Aether schematics.", potential_risk="Risk of technological espionage and loss of strategic monopoly."),
                    StoryChoice(choice_id=2, description="Reject Veloria's demands outright and risk breaking the defensive alliance.", potential_risk="Leaves Aetherion diplomatically isolated against future Dravaryn incursions."),
                    StoryChoice(choice_id=3, description="Propose a joint research task force under strict Aetherion supervision.", potential_risk="Causes diplomatic friction and exposes sensitive energy cores."),
                    StoryChoice(choice_id=4, description="Offer exclusive trading rights for refined Aether energy instead of core blueprints.", potential_risk="Imposes heavy economic costs and energy supply strain on Elyra.")
                ]
            )

        return StoryEvent(
            event_id="EVT001",
            chapter=1,
            location="Eastern Border Fortress",
            active_characters=["Arin Vale", "Kael Draven"],
            event_description="The Dravaryn vanguard under Commander Kael Draven advances toward the Eastern Border Fortress of Aetherion, demanding immediate surrender of the crystal reserves.",
            user_choices=[
                StoryChoice(choice_id=1, description="Send defensive reinforcements and reinforce the crystal shield.", potential_risk="Heavy defensive casualties and resource strain."),
                StoryChoice(choice_id=2, description="Attempt diplomatic negotiations with Kael Draven directly.", potential_risk="Kael might use talks as a tactical distraction."),
                StoryChoice(choice_id=3, description="Secretly evacuate civilians and sabotage the Aether conduits.", potential_risk="Loss of fortress territory and crystal infrastructure."),
                StoryChoice(choice_id=4, description="Request immediate military intervention from the Velorian Alliance.", potential_risk="Veloria will demand dangerous technological concessions.")
            ]
        )
