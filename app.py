import os
import sys
import json

from story_engine import StoryEngine


def display_choices(choices, title="Available Choices"):
    """Display story choices in a clean numbered format."""
    print(f"\n{title}:")

    for choice in choices:
        print(
            f"  {choice.choice_id}. {choice.description} "
            f"(Risk: {choice.potential_risk})"
        )


def get_user_choice(choices):
    """
    Ask the user to select one of the available story choices.

    Returns:
        str: Description of the selected choice.
    """
    while True:
        try:
            choice_number = int(
                input(f"\nEnter your choice (1-{len(choices)}): ").strip()
            )

            if 1 <= choice_number <= len(choices):
                selected_choice = choices[choice_number - 1]

                print(
                    f"\nUser Selected Decision: "
                    f"Choice {choice_number} -> '{selected_choice.description}'"
                )

                return selected_choice.description

            print(
                f"Please enter a number between 1 and {len(choices)}."
            )

        except ValueError:
            print("Invalid input. Please enter a number.")


def print_world(world):
    """Display generated world information."""

    print(f"Generated Theme: {world.theme}")

    print(f"Kingdoms Created ({len(world.kingdoms)}):")

    for kingdom in world.kingdoms:
        print(
            f"  - [{kingdom.type}] {kingdom.name} "
            f"(Capital: {kingdom.capital}) | "
            f"Resource: {kingdom.primary_resource}"
        )

    print(f"Tech/Magic Systems ({len(world.tech_magic_systems)}):")

    for system in world.tech_magic_systems:
        limitation = (
            system.limitations[0]
            if system.limitations
            else "No limitation specified"
        )

        print(
            f"  - {system.name}: {system.purpose} "
            f"| Limit: {limitation}"
        )

    print(f"Universe Rules ({len(world.rules)}):")

    for rule in world.rules:
        print(
            f"  - Rule: {rule.rule} "
            f"| Consequence: {rule.consequence}"
        )

    print(f"Timeline Entries ({len(world.timeline)}):")

    for timeline_entry in world.timeline:
        print(
            f"  - [{timeline_entry.year_or_era}] "
            f"{timeline_entry.title}: "
            f"{timeline_entry.description}"
        )


def print_characters(characters, relationships):
    """Display generated characters and relationships."""

    for character in characters:
        print(
            f"Character: {character.name} "
            f"({character.role}) | Origin: {character.origin}"
        )

        print(f"  Backstory: {character.backstory}")
        print(f"  Motivation: {character.motivation}")

        if character.skills:
            print(
                f"  Skills: {', '.join(character.skills)}"
            )

        if hasattr(character, "strengths") and character.strengths:
            print(
                f"  Strengths: {', '.join(character.strengths)}"
            )

        if hasattr(character, "weaknesses") and character.weaknesses:
            print(
                f"  Weaknesses: {', '.join(character.weaknesses)}"
            )

        if hasattr(character, "goals") and character.goals:
            print(
                f"  Goals: {', '.join(character.goals)}"
            )

    print("\nCharacter Relationships:")

    for relationship in relationships:
        print(
            f"Relationship: "
            f"{relationship.character_1} <-> "
            f"{relationship.character_2}"
        )

        print(
            f"  Type: {relationship.relationship_type}"
        )

        print(
            f"  Origin & Reason: "
            f"{relationship.origin_story} "
            f"({relationship.reason})"
        )


def print_lore_response(lore_response):
    """Display a lore retrieval response and its references."""

    print(f"Answer: {lore_response.answer}")

    if lore_response.source_lore:
        print("Source Lore References:")

        for reference in lore_response.source_lore:
            print(f"  - {reference}")


def main():

    print("=" * 80)
    print(
        "AI STORY UNIVERSE GENERATOR - "
        "NARRATIVE INTELLIGENCE & LONG-TERM MEMORY SYSTEM"
    )
    print("=" * 80)

    engine = StoryEngine(outputs_dir="outputs")

    print("\n--- SCENARIO 1: INITIAL WORLD GENERATION ---")

    world = engine.create_universe(
        theme="High-Fantasy Aetherpunk Continental Conflict"
    )

    print_world(world)

    print(
        "\n--- SCENARIO 2: "
        "CHARACTER GENERATION & RELATIONSHIPS ---"
    )

    characters = engine.generate_characters(
        roles=["Hero", "Villain"]
    )

    print_characters(
        characters,
        engine.relationships
    )

    print(
        "\n--- SCENARIO 3: "
        "USER CHOICE & STORY PROGRESSION (CHAPTER 1) ---"
    )

    evt1 = engine.initialize_story()

    print(
        f"Chapter {evt1.chapter} "
        f"Event [{evt1.event_id}] @ {evt1.location}"
    )

    print(
        f"Description: {evt1.event_description}"
    )

    display_choices(evt1.user_choices)

    selected_choice_text = get_user_choice(
        evt1.user_choices
    )

    print(
        "\n--- SCENARIO 4: "
        "CHOICE CONSEQUENCES & RELATIONSHIP CHANGE ---"
    )

    evt1_processed, consequence1 = (
        engine.process_user_choice(
            evt1,
            selected_choice_text
        )
    )

    print(
        f"Immediate Consequence: "
        f"{consequence1.immediate_consequence}"
    )

    print(
        f"Long-term Impact: "
        f"{consequence1.long_term_impact}"
    )

    print(
        f"Political Situation Updated: "
        f"{engine.state.political_situation}"
    )

    print(
        f"Relationship Dynamics Updated: "
        f"{engine.state.relationships}"
    )

    print(
        "\n--- PROGRESSING TO CHAPTER 2 "
        "(NEW EVENT BASED ON CHAPTER 1 DECISION) ---"
    )

    evt2 = engine.generate_next_chapter_event(
        user_intent=(
            "Generate the next story event using the "
            "consequences of the Chapter 1 decision, "
            "including relevant political, character, "
            "relationship, and historical lore context."
        )
    )

    print(
        f"Chapter {evt2.chapter} "
        f"Event [{evt2.event_id}] @ {evt2.location}"
    )

    print(
        f"Description: {evt2.event_description}"
    )

    display_choices(
        evt2.user_choices,
        title="Available Choices (Chapter 2)"
    )

    selected_choice_2 = get_user_choice(
        evt2.user_choices
    )

    evt2_processed, consequence2 = (
        engine.process_user_choice(
            evt2,
            selected_choice_2
        )
    )

    print(
        f"Immediate Consequence: "
        f"{consequence2.immediate_consequence}"
    )

    print(
        f"Long-term Impact: "
        f"{consequence2.long_term_impact}"
    )

    print(
        f"Political Situation Updated: "
        f"{engine.state.political_situation}"
    )

    print(
        f"Relationship Dynamics Updated: "
        f"{engine.state.relationships}"
    )

    print(
        "\n--- SCENARIO 5: "
        "HISTORICAL LORE RETRIEVAL ---"
    )

    query_1 = (
        "Why did Veloria demand technology concessions "
        "from Aetherion?"
    )

    print(f"User Query: '{query_1}'")

    lore_resp1 = engine.query_lore(query_1)

    print_lore_response(lore_resp1)

    print(
        "\n--- SCENARIO 6: "
        "LONG-TERM FOLLOW-UP QUERY "
        "(MULTI-CHAPTER MEMORY) ---"
    )

    query_2 = (
        "What decision was made at the Eastern Border "
        "in Chapter 1?"
    )

    print(f"User Query: '{query_2}'")

    lore_resp2 = engine.query_lore(query_2)

    print_lore_response(lore_resp2)


    print(
        "\n--- SCENARIO 7: "
        "CONTRADICTION PREVENTION ---"
    )

    invalid_event = (
        "Arin Vale decides to use forbidden time travel "
        "to rewrite Year 127 and undo the discovery of "
        "Aether Crystals in the Chronicle Vault."
    )

    print(
        f"Proposed Contradictory Event: "
        f"'{invalid_event}'"
    )

    check_res = engine.test_contradiction(
        invalid_event
    )

    print(
        f"Is Consistent: "
        f"{check_res.is_consistent}"
    )

    print(
        f"Rationale: "
        f"{check_res.rationale}"
    )

    if check_res.suggested_revisions:
        print(
            f"Suggested Revision: "
            f"{check_res.suggested_revisions}"
        )


    print(
        "\n--- SCENARIO 8: "
        "UNKNOWN LORE HANDLING ---"
    )

    unknown_query = (
        "What happened during the Martian Invasion "
        "of Aetherion in Year 900?"
    )

    print(
        f"User Query: '{unknown_query}'"
    )

    lore_resp3 = engine.query_lore(
        unknown_query
    )

    print(
        f"Answer: {lore_resp3.answer}"
    )

    print("\n" + "=" * 80)

    print(
        "EXECUTION COMPLETE. "
        "All artifacts and state persisted in "
        "outputs/ and data/lore/"
    )

    print("=" * 80)


if __name__ == "__main__":
    main()
