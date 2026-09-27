from typing import List, Dict, Any

class StoryMemoryManager:
    def __init__(self, max_short_term_events: int = 5):
        self.short_term_history: List[Dict[str, Any]] = []
        self.max_short_term_events = max_short_term_events

    def add_event(self, event_dict: Dict[str, Any]):
        self.short_term_history.append(event_dict)
        if len(self.short_term_history) > self.max_short_term_events:
            self.short_term_history.pop(0)

    def get_recent_summary(self) -> str:
        if not self.short_term_history:
            return "No recent story events."
        summary_lines = []
        for evt in self.short_term_history:
            chap = evt.get("chapter", 1)
            desc = evt.get("event_description", "")
            choice = evt.get("user_choice_selected", "None")
            conseq = evt.get("consequence", "None")
            summary_lines.append(f"Chapter {chap}: {desc} | Decision: {choice} | Consequence: {conseq}")
        return "\n".join(summary_lines)

    def clear(self):
        self.short_term_history.clear()
