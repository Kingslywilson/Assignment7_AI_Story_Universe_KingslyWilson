import os
import json
from typing import List, Dict, Any, Tuple, Optional
from dotenv import load_dotenv

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import BaseMessage, AIMessage
from langchain_core.outputs import ChatResult, ChatGeneration

from models import (
    WorldSchema, CharacterProfile, CharacterRelationship, 
    StoryEvent, ChoiceConsequence, ConsistencyCheckResult, LoreQueryResponse
)
from story_state import StoryState
from memory import StoryMemoryManager
from vector_store import VectorStoreManager
from lore_retriever import LoreRetriever

from chains.world_generation import WorldGenerationChain
from chains.character_generation import CharacterGenerationChain
from chains.relationship_generation import RelationshipGenerationChain
from chains.story_progression import StoryProgressionChain
from chains.consequence_generation import ConsequenceGenerationChain
from chains.consistency_checker import ConsistencyCheckerChain

class DummyLLM(BaseChatModel):
    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[Any] = None,
        **kwargs: Any,
    ) -> ChatResult:
        msg = AIMessage(content="Default AI Narrative Response")
        return ChatResult(generations=[ChatGeneration(message=msg)])

    @property
    def _llm_type(self) -> str:
        return "dummy-llm"

class StoryEngine:
    def __init__(self, llm=None, persistence_dir: str = "data/lore", outputs_dir: str = "outputs"):
        load_dotenv()
        self.outputs_dir = outputs_dir
        os.makedirs(self.outputs_dir, exist_ok=True)

        if llm is None:
            self._init_llm()
        else:
            self.llm = llm

        self.vector_store_mgr = VectorStoreManager(persistence_dir=persistence_dir)
        self.lore_retriever = LoreRetriever(self.vector_store_mgr)
        self.memory_mgr = StoryMemoryManager()
        self.state = StoryState()

        self.world_chain = WorldGenerationChain(self.llm)
        self.character_chain = CharacterGenerationChain(self.llm)
        self.relationship_chain = RelationshipGenerationChain(self.llm)
        self.progression_chain = StoryProgressionChain(self.llm)
        self.consequence_chain = ConsequenceGenerationChain(self.llm)
        self.consistency_chain = ConsistencyCheckerChain(self.llm)

        self.world: WorldSchema = None
        self.characters: List[CharacterProfile] = []
        self.relationships: List[CharacterRelationship] = []
        self.story_history: List[Dict[str, Any]] = []

    def _init_llm(self):
        groq_key = os.getenv("GROQ_API_KEY")
        openai_key = os.getenv("OPENAI_API_KEY")
        
        if groq_key:
            try:
                from langchain_groq import ChatGroq
                self.llm = ChatGroq(model_name="llama-3.1-8b-instant", groq_api_key=groq_key)
                return
            except Exception:
                pass
        
        if openai_key:
            try:
                from langchain_openai import ChatOpenAI
                self.llm = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=openai_key)
                return
            except Exception:
                pass
        
        self.llm = DummyLLM()

    def create_universe(self, theme: str = "High-Fantasy Aetherpunk Continental Conflict") -> WorldSchema:
        self.world = self.world_chain.run(theme=theme)
        
        for k in self.world.kingdoms:
            text = f"Kingdom {k.name} ({k.type}): Capital {k.capital}, Government {k.government}, Resource {k.primary_resource}. Culture: {k.culture}. Geography: {k.geography}. Allies: {', '.join(k.allies)}. Enemies: {', '.join(k.enemies)}."
            self.vector_store_mgr.add_lore(text, metadata={"type": "kingdom", "name": k.name, "chapter": 0})

        for sys in self.world.tech_magic_systems:
            text = f"System {sys.name}: Purpose {sys.purpose}. Capabilities: {', '.join(sys.capabilities)}. Limitations: {', '.join(sys.limitations)}. Users: {', '.join(sys.users)}. Consequences: {sys.cost_or_consequence}."
            self.vector_store_mgr.add_lore(text, metadata={"type": "magic_tech", "name": sys.name, "chapter": 0})

        for r in self.world.rules:
            text = f"Universe Rule [{r.category}] {r.rule}: Consequence for breaking: {r.consequence}."
            self.vector_store_mgr.add_lore(text, metadata={"type": "rule", "title": r.rule, "chapter": 0})

        for t in self.world.timeline:
            text = f"Timeline Event ({t.year_or_era}) - {t.title}: {t.description}. Impact: {t.impact}."
            self.vector_store_mgr.add_lore(text, metadata={"type": "timeline", "title": t.title, "year": t.year_or_era, "chapter": 0})

        with open(os.path.join(self.outputs_dir, "world.json"), "w", encoding="utf-8") as f:
            json.dump(self.world.model_dump(), f, indent=2)

        with open(os.path.join(self.outputs_dir, "timeline.json"), "w", encoding="utf-8") as f:
            json.dump([t.model_dump() for t in self.world.timeline], f, indent=2)

        return self.world

    def generate_characters(self, roles: List[str] = ["Hero", "Villain"]) -> List[CharacterProfile]:
        world_ctx = json.dumps(self.world.model_dump(), indent=2) if self.world else "Default World Context"
        self.characters = []

        for role in roles:
            char_profile = self.character_chain.run(world_context=world_ctx, role=role)
            self.characters.append(char_profile)
            self.state.active_characters.append(char_profile.name)
            self.state.character_status[char_profile.name] = "Active and unharmed"

            text = f"Character Profile [{char_profile.role}] {char_profile.name} from {char_profile.origin}. Backstory: {char_profile.backstory} Motivation: {char_profile.motivation} Skills: {', '.join(char_profile.skills)} Weakness: {', '.join(char_profile.weaknesses)}."
            self.vector_store_mgr.add_lore(text, metadata={"type": "character", "name": char_profile.name, "role": char_profile.role, "chapter": 0})

        char_names = [c.name for c in self.characters]
        rel = self.relationship_chain.run(world_context=world_ctx, character_list=", ".join(char_names))
        self.relationships = [rel]
        
        self.state.relationships[f"{rel.character_1} vs {rel.character_2}"] = rel.relationship_type

        rel_text = f"Relationship between {rel.character_1} and {rel.character_2}: {rel.relationship_type}. Origin: {rel.origin_story} Reason: {rel.reason}"
        self.vector_store_mgr.add_lore(rel_text, metadata={"type": "relationship", "characters": [rel.character_1, rel.character_2], "chapter": 0})

        with open(os.path.join(self.outputs_dir, "characters.json"), "w", encoding="utf-8") as f:
            json.dump([c.model_dump() for c in self.characters], f, indent=2)

        return self.characters

    def initialize_story(self) -> StoryEvent:
        retrieved_lore = self.lore_retriever.retrieve_context_for_scene("Eastern Border invasion Kael Draven Arin Vale")
        event = self.progression_chain.run(
            story_state=self.state.get_summary(),
            retrieved_lore=retrieved_lore,
            previous_context="Beginning of chapter 1 narrative arc."
        )
        return event

    def process_user_choice(self, event: StoryEvent, choice_selected: str) -> Tuple[StoryEvent, ChoiceConsequence]:
        retrieved_lore = self.lore_retriever.retrieve_context_for_scene(f"{event.event_description} {choice_selected}")
        
        consequence = self.consequence_chain.run(
            story_state=self.state.get_summary(),
            retrieved_lore=retrieved_lore,
            event_description=event.event_description,
            user_choice=choice_selected
        )

        event.user_choice_selected = choice_selected
        event.consequence = consequence.immediate_consequence

        self.state.update_state(consequence.model_dump(), choice_text=choice_selected)
        self.state.record_event(event.model_dump())
        self.memory_mgr.add_event(event.model_dump())

        lore_text = f"Event {event.event_id} (Chapter {self.state.chapter}) at {event.location}: {event.event_description} User selected choice: '{choice_selected}'. Consequence: {consequence.immediate_consequence} Long-term impact: {consequence.long_term_impact}."
        self.vector_store_mgr.add_lore(
            lore_text, 
            metadata={
                "type": "story_event",
                "event_id": event.event_id,
                "chapter": self.state.chapter,
                "location": event.location,
                "characters": event.active_characters,
                "title": f"Event {event.event_id}"
            }
        )

        self.story_history.append({
            "chapter": self.state.chapter,
            "event": event.model_dump(),
            "consequence": consequence.model_dump(),
            "state_after": self.state.to_dict()
        })

        with open(os.path.join(self.outputs_dir, "story_history.json"), "w", encoding="utf-8") as f:
            json.dump(self.story_history, f, indent=2)

        self.state.advance_chapter()
        return event, consequence

    def generate_next_chapter_event(self, user_intent: str = "Continue narrative after recent decision") -> StoryEvent:
        retrieved_lore = self.lore_retriever.retrieve_context_for_scene(user_intent)
        recent_context = self.memory_mgr.get_recent_summary()
        
        event = self.progression_chain.run(
            story_state=self.state.get_summary(),
            retrieved_lore=retrieved_lore,
            previous_context=recent_context,
            user_intent=user_intent
        )
        event.chapter = self.state.chapter
        return event

    def query_lore(self, user_query: str) -> LoreQueryResponse:
        return self.lore_retriever.query_lore_history(user_query, llm=self.llm)

    def test_contradiction(self, proposed_event: str) -> ConsistencyCheckResult:
        retrieved_lore = self.lore_retriever.retrieve_context_for_scene(proposed_event)
        return self.consistency_chain.run(
            proposed_event=proposed_event,
            story_state=self.state.get_summary(),
            established_lore=retrieved_lore
        )
