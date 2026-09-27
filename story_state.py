import json
from typing import Dict, Any, List

class StoryState:
    def __init__(self):
        self.chapter: int = 1
        self.current_location: str = "Capital City"
        self.active_characters: List[str] = []
        self.character_status: Dict[str, str] = {}
        self.relationships: Dict[str, str] = {}
        self.completed_events: List[Dict[str, Any]] = []
        self.current_goals: List[str] = []
        self.political_situation: str = "Tense Peace"
        self.world_state_changes: List[str] = []
        self.user_decisions: List[Dict[str, Any]] = []
        self.active_conflict: str = "Unrest on the borders"

    def update_state(self, consequence_data: Dict[str, Any], choice_text: str = None):
        if choice_text:
            self.user_decisions.append({
                "chapter": self.chapter,
                "choice": choice_text
            })
        
        if "political_changes" in consequence_data:
            self.political_situation = consequence_data["political_changes"]
            self.world_state_changes.append(f"Chapter {self.chapter}: {consequence_data['political_changes']}")

        if "relationship_updates" in consequence_data and isinstance(consequence_data["relationship_updates"], dict):
            for rel_key, rel_val in consequence_data["relationship_updates"].items():
                self.relationships[rel_key] = rel_val

        if "state_updates" in consequence_data and isinstance(consequence_data["state_updates"], dict):
            updates = consequence_data["state_updates"]
            if "location" in updates:
                self.current_location = updates["location"]
            if "active_conflict" in updates:
                self.active_conflict = updates["active_conflict"]
            if "character_status" in updates and isinstance(updates["character_status"], dict):
                self.character_status.update(updates["character_status"])

    def record_event(self, event_data: Dict[str, Any]):
        self.completed_events.append(event_data)

    def advance_chapter(self):
        self.chapter += 1

    def to_dict(self) -> Dict[str, Any]:
        return {
            "chapter": self.chapter,
            "current_location": self.current_location,
            "active_characters": self.active_characters,
            "character_status": self.character_status,
            "relationships": self.relationships,
            "completed_events": self.completed_events,
            "current_goals": self.current_goals,
            "political_situation": self.political_situation,
            "world_state_changes": self.world_state_changes,
            "user_decisions": self.user_decisions,
            "active_conflict": self.active_conflict
        }

    def get_summary(self) -> str:
        return json.dumps(self.to_dict(), indent=2)
