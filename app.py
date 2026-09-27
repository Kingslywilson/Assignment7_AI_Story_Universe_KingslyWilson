import os
import sys
import json
from story_engine import StoryEngine

def main():
    print("=" * 80)
    print("AI STORY UNIVERSE GENERATOR - NARRATIVE INTELLIGENCE & LONG-TERM MEMORY SYSTEM")
    print("=" * 80)

    engine = StoryEngine(outputs_dir="outputs")

    print("\n--- SCENARIO 1: INITIAL WORLD GENERATION ---")
    world = engine.create_universe(theme="High-Fantasy Aetherpunk Continental Conflict")
    print(f"Generated Theme: {world.theme}")
    print(f"Kingdoms Created ({len(world.kingdoms)}):")
    for k in world.kingdoms:
        print(f"  - [{k.type}] {k.name} (Capital: {k.capital}) | Resource: {k.primary_resource}")
    print(f"Tech/Magic Systems ({len(world.tech_magic_systems)}):")
    for sys_item in world.tech_magic_systems:
        print(f"  - {sys_item.name}: {sys_item.purpose} | Limit: {sys_item.limitations[0]}")
    print(f"Universe Rules ({len(world.rules)}):")
    for r in world.rules:
        print(f"  - Rule: {r.rule} | Consequence: {r.consequence}")
    print(f"Timeline Entries ({len(world.timeline)}):")
    for t in world.timeline:
        print(f"  - [{t.year_or_era}] {t.title}: {t.description}")

    print("\n--- SCENARIO 2: CHARACTER GENERATION & RELATIONSHIPS ---")
    characters = engine.generate_characters(roles=["Hero", "Villain"])
    for c in characters:
        print(f"Character: {c.name} ({c.role}) | Origin: {c.origin}")
        print(f"  Backstory: {c.backstory}")
        print(f"  Motivation: {c.motivation}")
        print(f"  Skills: {', '.join(c.skills)}")
    for rel in engine.relationships:
        print(f"Relationship: {rel.character_1} <-> {rel.character_2}")
        print(f"  Type: {rel.relationship_type}")
        print(f"  Origin & Reason: {rel.origin_story} ({rel.reason})")

    print("\n--- SCENARIO 3: USER CHOICE & STORY PROGRESSION (CHAPTER 1) ---")
    evt1 = engine.initialize_story()
    print(f"Chapter {evt1.chapter} Event [{evt1.event_id}] @ {evt1.location}")
    print(f"Description: {evt1.event_description}")
    print("Available Choices:")
    for choice in evt1.user_choices:
        print(f"  {choice.choice_id}. {choice.description} (Risk: {choice.potential_risk})")
    
    selected_choice_text = evt1.user_choices[3].description
    print(f"\nUser Selected Decision: Choice 4 -> '{selected_choice_text}'")

    print("\n--- SCENARIO 4: CHOICE CONSEQUENCES & RELATIONSHIP CHANGE ---")
    evt1_processed, consequence1 = engine.process_user_choice(evt1, selected_choice_text)
    print(f"Immediate Consequence: {consequence1.immediate_consequence}")
    print(f"Long-term Impact: {consequence1.long_term_impact}")
    print(f"Political Situation Updated: {engine.state.political_situation}")
    print(f"Relationship Dynamics Updated: {engine.state.relationships}")

    print("\n--- PROGRESSING TO CHAPTER 2 (NEW EVENT GENERATION BASED ON CHAPTER 1 DECISION) ---")
    evt2 = engine.generate_next_chapter_event(user_intent="Velorian diplomats arrive demanding Aether Crystal blueprints following Chapter 1 intervention")
    print(f"Chapter {evt2.chapter} Event [{evt2.event_id}] @ {evt2.location}")
    print(f"Description: {evt2.event_description}")
    print("Available Choices (Chapter 2):")
    for choice in evt2.user_choices:
        print(f"  {choice.choice_id}. {choice.description} (Risk: {choice.potential_risk})")
    
    selected_choice_2 = evt2.user_choices[1].description
    print(f"\nUser Selected Decision (Chapter 2): Choice 2 -> '{selected_choice_2}'")
    evt2_processed, consequence2 = engine.process_user_choice(evt2, selected_choice_2)
    print(f"Immediate Consequence: {consequence2.immediate_consequence}")

    print("\n--- SCENARIO 5: HISTORICAL LORE RETRIEVAL ---")
    query_1 = "Why did Veloria demand technology concessions from Aetherion?"
    print(f"User Query: '{query_1}'")
    lore_resp1 = engine.query_lore(query_1)
    print(f"Answer: {lore_resp1.answer}")
    print("Source Lore References:")
    for ref in lore_resp1.source_lore:
        print(f"  - {ref}")

    print("\n--- SCENARIO 6: LONG-TERM FOLLOW-UP QUERY (MULTI-CHAPTER MEMORY) ---")
    query_2 = "What decision was made at the Eastern Border in Chapter 1?"
    print(f"User Query: '{query_2}'")
    lore_resp2 = engine.query_lore(query_2)
    print(f"Answer: {lore_resp2.answer}")
    print("Source Lore References:")
    for ref in lore_resp2.source_lore:
        print(f"  - {ref}")

    print("\n--- SCENARIO 7: CONTRADICTION PREVENTION ---")
    invalid_event = "Arin Vale decides to use forbidden time travel to rewrite Year 127 and undo the discovery of Aether Crystals in the Chronicle Vault."
    print(f"Proposed Contradictory Event: '{invalid_event}'")
    check_res = engine.test_contradiction(invalid_event)
    print(f"Is Consistent: {check_res.is_consistent}")
    print(f"Rationale: {check_res.rationale}")
    if check_res.suggested_revisions:
        print(f"Suggested Revision: {check_res.suggested_revisions}")

    print("\n--- SCENARIO 8: UNKNOWN LORE HANDLING ---")
    unknown_query = "What happened during the Martian Invasion of Aetherion in Year 900?"
    print(f"User Query: '{unknown_query}'")
    lore_resp3 = engine.query_lore(unknown_query)
    print(f"Answer: {lore_resp3.answer}")

    print("\n" + "=" * 80)
    print("EXECUTION COMPLETE. All artifacts and state persisted in outputs/ and data/lore/")
    print("=" * 80)

if __name__ == "__main__":
    main()
