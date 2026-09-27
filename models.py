from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class Kingdom(BaseModel):
    name: str
    type: str = "Kingdom"
    capital: str
    government: str
    primary_resource: str
    culture: str
    geography: str
    economy: str
    allies: List[str]
    enemies: List[str]
    important_locations: List[str]
    political_importance: str

class TechMagicSystem(BaseModel):
    name: str
    purpose: str
    capabilities: List[str]
    limitations: List[str]
    users: List[str]
    cost_or_consequence: str
    origin: str

class UniverseRule(BaseModel):
    rule: str
    category: str
    consequence: str

class TimelineEvent(BaseModel):
    year_or_era: str
    title: str
    description: str
    key_factions: List[str]
    impact: str

class WorldSchema(BaseModel):
    theme: str
    kingdoms: List[Kingdom]
    tech_magic_systems: List[TechMagicSystem]
    rules: List[UniverseRule]
    timeline: List[TimelineEvent]

class CharacterProfile(BaseModel):
    name: str
    role: str
    origin: str
    age: Optional[str] = "Unknown"
    skills: List[str]
    strengths: List[str]
    weaknesses: List[str]
    personality: str
    backstory: str
    motivation: str
    goals: List[str]
    fears: List[str]
    relationships: List[str] = Field(default_factory=list)
    secrets: Optional[str] = None

class CharacterRelationship(BaseModel):
    character_1: str
    character_2: str
    relationship_type: str
    origin_story: str
    reason: str

class StoryChoice(BaseModel):
    choice_id: int
    description: str
    potential_risk: str

class StoryEvent(BaseModel):
    event_id: str
    chapter: int
    location: str
    active_characters: List[str]
    event_description: str
    user_choices: List[StoryChoice]
    user_choice_selected: Optional[str] = None
    consequence: Optional[str] = None

class ChoiceConsequence(BaseModel):
    choice_selected: str
    immediate_consequence: str
    long_term_impact: str
    relationship_updates: Dict[str, str] = Field(default_factory=dict)
    political_changes: str
    state_updates: Dict[str, Any] = Field(default_factory=dict)

class ConsistencyCheckResult(BaseModel):
    is_consistent: bool
    rationale: str
    suggested_revisions: Optional[str] = None

class LoreQueryResponse(BaseModel):
    answer: str
    source_lore: List[str]
    retrieved_documents: List[str]
