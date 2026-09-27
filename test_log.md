# AI Story Universe Generator — Test Log

## Test Environment

* Python: 3.11
* Framework: LangChain
* LLM: Groq / ChatGroq
* Embeddings: Hugging Face Embeddings
* Vector Database: FAISS
* Application: Python CLI
* Project: Assignment7_AI_Story_Universe_KingslyWilson

---

# Test 1 — World Generation

## Question / Action

Create a new story universe and generate the initial world.

## Expected Result

The system should generate a structured fictional universe containing kingdoms, technology or magic, universe rules, and historical information.

## Actual Result

The system generated:

* Theme: High-Fantasy Aetherpunk Continental Conflict
* Kingdoms:

  * Aetherion
  * Dravaryn Empire
* Technology:

  * Aether Engineering
* Universe Rule:

  * Chronicle Vault Integrity
* Timeline:

  * Year 127 — Discovery of Aether Crystals
  * Year 148 — The Dravaryn Expansion

## Result

**PASS**

---

# Test 2 — Kingdom Generation

## Question / Action

Verify that the world-generation stage creates multiple kingdoms with their associated capitals and resources.

## Expected Result

Multiple kingdoms should be generated as part of the fictional universe.

## Actual Result

The generated kingdoms were:

### Aetherion

* Capital: Elyra
* Primary Resource: Aether Crystals

### Dravaryn Empire

* Capital: Vraks
* Primary Resource: Obsidian Ore

## Result

**PASS**

---

# Test 3 — Universe Rule Generation

## Question / Action

Verify that the generated universe contains explicit rules that can later be used by the consistency checker.

## Expected Result

The system should generate at least one rule governing the fictional universe.

## Actual Result

Generated rule:

**Chronicle Vault Integrity**

Consequence:

Recorded historical events cannot be altered without splitting into unstable parallel timelines.

This rule was later used during the contradiction-prevention scenario.

## Result

**PASS**

---

# Test 4 — Timeline Generation

## Question / Action

Verify that the world-generation stage creates historical timeline events.

## Expected Result

The system should generate historical events with years and descriptions.

## Actual Result

Generated timeline:

* Year 127 — Discovery of Aether Crystals
* Year 148 — The Dravaryn Expansion

These events became part of the established story lore.

## Result

**PASS**

---

# Test 5 — Hero Generation

## Question / Action

Generate a hero connected to the established fictional universe.

## Expected Result

The system should generate a structured hero profile containing information such as name, role, origin, skills, backstory, and motivation.

## Actual Result

Generated hero:

* Name: Arin Vale
* Role: Hero
* Origin: Aetherion
* Skills:

  * Swordsmanship
  * Aether Engineering
  * Tactical Command
* Backstory: Lost his family during the Dravaryn expansion into the Northern Territories.
* Motivation: Protect the kingdom and prevent centralized tyranny.

## Result

**PASS**

---

# Test 6 — Villain Generation

## Question / Action

Generate a villain connected to the established fictional universe.

## Expected Result

The system should generate an antagonist with an origin, skills, backstory, motivation, and objective.

## Actual Result

Generated villain:

* Name: Kael Draven
* Role: Villain
* Origin: Dravaryn Empire
* Skills:

  * Strategic Warfare
  * Obsidian Metallurgy
  * Mind Manipulation
* Backstory: Distinguished Dravaryn commander who believes independent kingdoms create endless war.
* Motivation: Establish permanent continental peace through centralized control.

## Result

**PASS**

---

# Test 7 — Character Motivation

## Question

What is Arin Vale's motivation, and how is it connected to the history of Aetherion?

## Expected Result

The system should use the established character profile and world history rather than inventing a new motivation.

## Actual Result

Arin Vale's motivation is to protect Aetherion and prevent centralized tyranny after losing his family during the Dravaryn expansion into the Northern Territories.

## Result

**PASS**

---

# Test 8 — Character Relationship

## Question

What is the relationship between Arin Vale and Kael Draven, and why did they become enemies?

## Expected Result

The system should maintain the established relationship and its origin.

## Actual Result

Relationship:

**Former allies turned bitter enemies.**

Reason:

Arin Vale and Kael Draven served together during the initial Northern Border defense squad but disagreed over the use and militarization of Aether technology.

## Result

**PASS**

---

# Test 9 — User Choice Scenario

## Question / Action

The Dravaryn army approaches the Eastern Border Fortress. Select one of the available story choices.

Selected Choice:

**Choice 4 — Request immediate military intervention from the Velorian Alliance.**

## Expected Result

The selected user decision should become part of the story progression and influence the next event.

## Actual Result

The system generated four choices.

Choice 4 was selected.

The subsequent chapter occurred at the Velorian Diplomatic Enclave in Elyra, where Veloria demanded access to Aether Crystal Engineering technology.

## Result

**PASS**

---

# Test 10 — Choice Consequence

## Question / Action

Determine the consequences of requesting military intervention from Veloria.

## Expected Result

The selected decision should produce immediate and longer-term narrative consequences.

## Actual Result

Immediate consequence:

Aetherion sustained its position but triggered long-term diplomatic demands from surrounding allies.

Long-term impact:

The balance of power shifted across Elyra, creating heightened tension between Aetherion, Veloria, and Dravaryn.

## Result

**PASS**

---

# Test 11 — Story-State Update

## Question / Action

Verify that the selected decision and its consequences affect the evolving story state.

## Expected Result

The story state should reflect changes resulting from the user's decision.

## Actual Result

The execution showed:

Political Situation:

**Aetherion and Dravaryn Empire entered a state of open mobilization.**

Relationship Dynamics:

**Arin Vale vs Kael Draven — Hostility escalated following direct tactical engagement.**

The selected Velorian intervention also affected the subsequent Chapter 2 event.

## Result

**PASS**

---

# Test 12 — Lore Storage

## Question / Action

Verify that generated story events and narrative history are persisted for future retrieval.

## Expected Result

Important story events should be stored as persistent lore and made available to the retrieval system.

## Actual Result

The application completed with:

```text
EXECUTION COMPLETE. All artifacts and state persisted in outputs/ and data/lore/
```

The project contains the persisted FAISS vector-store files:

```text
data/lore/index.faiss
data/lore/index.pkl
```

The project also contains:

```text
outputs/world.json
outputs/characters.json
outputs/timeline.json
outputs/story_history.json
```

## Result

**PASS**

---

## Test 13 — Historical Lore Retrieval

## Question

Why did Veloria demand technology concessions from Aetherion?

## Expected Result

The system should retrieve relevant previous events from the lore database and answer using established story history.

## Actual Result

Veloria demanded technology concessions because Aetherion requested immediate military intervention from the Velorian Alliance during the Eastern Border crisis in Chapter 1.

Veloria conditioned its military support on receiving access to Aether Crystal technology.

Source Lore:

* Chapter 2 — Event EVT002
* Chapter 1 — Event EVT001

## Result

**PASS**

# Test 14 — Multi-Chapter Follow-Up / Long-Term Memory

## Question

What decision was made at the Eastern Border in Chapter 1?

## Expected Result

The system should retrieve information from an earlier chapter rather than treating the question as a new event.

## Actual Result

During Chapter 1, Event EVT001, at the Eastern Border Fortress, Aetherion decided to request immediate military intervention from the Velorian Alliance to hold off Commander Kael Draven's Dravaryn vanguard.

Source Lore:

* Chapter 1 — Event EVT001

## Result

**PASS**

---

# Test 15 — Narrative Contradiction Prevention

## Proposed Event

> Arin Vale uses forbidden time travel to rewrite Year 127 and prevent the discovery of Aether Crystals.

## Expected Result

The system should identify that the proposed event conflicts with an established universe rule.

## Actual Result

```text
Is Consistent: False
```

The system identified that the proposed event violates the:

**Chronicle Vault Integrity**

rule.

Established rule:

Recorded historical events cannot be altered without splitting into unstable parallel timelines.

Suggested revision:

Revise the proposed action to work within the current timeline instead of attempting to alter recorded history.

## Result

**PASS**

---

# Test 16 — Unknown-Lore Handling

## Question

What happened during the Martian Invasion of Aetherion in Year 900?

## Expected Result

The system should not invent an event that does not exist in the established story lore.

## Actual Result

```text
I could not find this event in the established story lore.
```

The system did not fabricate a historical event.

## Result

**PASS**

---

# Overall Test Summary

| Test | Requirement               | Result |
| ---- | ------------------------- | ------ |
| 1    | World generation          | PASS   |
| 2    | Kingdom generation        | PASS   |
| 3    | Universe-rule generation  | PASS   |
| 4    | Timeline generation       | PASS   |
| 5    | Hero generation           | PASS   |
| 6    | Villain generation        | PASS   |
| 7    | Character motivation      | PASS   |
| 8    | Character relationship    | PASS   |
| 9    | User-choice scenario      | PASS   |
| 10   | Choice consequence        | PASS   |
| 11   | Story-state update        | PASS   |
| 12   | Lore storage              | PASS   |
| 13   | Historical lore retrieval | PASS   |
| 14   | Multi-chapter follow-up   | PASS   |
| 15   | Contradiction prevention  | PASS   |
| 16   | Unknown-lore handling     | PASS   |

**Total Tests: 16**

**Passed: 16**

**Failed: 0**

---

# Final Execution Evidence

The application completed successfully with:

```text
EXECUTION COMPLETE. All artifacts and state persisted in outputs/ and data/lore/
```

The test results demonstrate:

* World building
* Kingdom generation
* Technology generation
* Universe rules
* Timeline generation
* Hero generation
* Villain generation
* Character motivations
* Character relationships
* User-driven story choices
* Choice consequences
* Story-state changes
* Persistent lore
* Historical lore retrieval
* Multi-chapter memory
* Narrative consistency checking
* Unknown-lore handling

## Test Conclusion

The implemented AI Story Universe Generator successfully demonstrates the required narrative intelligence workflow:

```text
World Building
      ↓
Character Generation
      ↓
Motivations & Relationships
      ↓
Structured Story State
      ↓
User Choice
      ↓
Consequences
      ↓
Narrative Memory
      ↓
Lore Storage
      ↓
Embeddings
      ↓
FAISS
      ↓
Lore Retrieval
      ↓
Consistency Checking
      ↓
Long-Term Story Progression
```
