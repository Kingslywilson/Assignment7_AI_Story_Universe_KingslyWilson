# AI Story Universe Generator — Test Log

## Test Environment

- Python: 3.11
- Framework: LangChain
- LLM: Groq / ChatGroq
- Embeddings: HuggingFace Embeddings
- Vector Database: FAISS
- Application: Python CLI
- Project: Assignment7_AI_Story_Universe_KingslyWilson

---

## Test 1 — Initial World Generation

### Question / Action

Create a new story universe and generate the kingdoms, technology/magic
systems, universe rules, and historical timeline.

### Expected Result

The system should generate a structured fictional universe containing:

- Multiple kingdoms or regions
- Technology or magic systems
- Universe rules
- Historical timeline events

The generated information should be internally consistent.

### Actual Result

The system generated:

- Theme: High-Fantasy Aetherpunk Continental Conflict
- Kingdoms:
  - Aetherion
  - Dravaryn Empire
- Technology/Magic:
  - Aether Engineering
- Universe Rule:
  - Chronicle Vault Integrity
- Timeline:
  - Year 127 — Discovery of Aether Crystals
  - Year 148 — The Dravaryn Expansion

### Result

PASS

## Test 2 — Character Generation

### Question / Action

Generate a hero and villain connected to the established universe.

### Expected Result

The system should generate structured character profiles containing
origin, role, backstory, motivation, skills, strengths, weaknesses,
goals, and relationships.

### Actual Result

Hero generated:

- Name: Arin Vale
- Role: Hero
- Origin: Aetherion
- Skills:
  - Swordsmanship
  - Aether Engineering
  - Tactical Command
- Motivation: Protect the kingdom and prevent centralized tyranny.

Villain generated:

- Name: Kael Draven
- Role: Villain
- Origin: Dravaryn Empire
- Skills:
  - Strategic Warfare
  - Obsidian Metallurgy
  - Mind Manipulation
- Motivation: Establish permanent continental peace through centralized control.

### Result

PASS

## Test 3 — Character Motivation

### Question

What is Arin Vale's motivation, and how is it connected to the history
of Aetherion?

### Expected Result

The system should use the established character profile and world history
rather than inventing a new motivation.

### Actual Result

Arin Vale's motivation is to protect Aetherion and prevent centralized
tyranny after losing his family during the Dravaryn expansion into the
Northern Territories.

### Result

PASS

## Test 4 — Character Relationship

### Question

What is the relationship between Arin Vale and Kael Draven, and why did
they become enemies?

### Expected Result

The system should retrieve the established relationship and its reason.

### Actual Result

Relationship:

Former allies turned bitter enemies.

Reason:

Arin Vale and Kael Draven served together during the initial Northern
Border defense squad but disagreed over the use and militarization of
Aether technology.

### Result

PASS

## Test 5 — User Choice and Story Progression

### Question / Action

The Dravaryn army approaches the Eastern Border Fortress. Select one of
the available story choices.

Selected Choice:

Choice 4 — Request immediate military intervention from the Velorian Alliance.

### Expected Result

The selected choice should influence the subsequent story.

### Actual Result

The system generated four choices. Choice 4 was selected.

The next chapter occurred at the Velorian Diplomatic Enclave in Elyra,
where Veloria demanded access to Aether Crystal Engineering technology.

### Result

PASS

## Test 6 — Choice Consequence and Story-State Update

### Question / Action

What happened after requesting military intervention from Veloria?

### Expected Result

The system should generate consequences and update the political and
relationship state.

### Actual Result

Immediate consequence:

Aetherion sustained its position but triggered long-term diplomatic
demands from surrounding allies.

Political situation:

Aetherion and Dravaryn Empire entered a state of open mobilization.

Relationship update:

Arin Vale vs Kael Draven — hostility escalated following direct tactical
engagement.

### Result

PASS

## Test 7 — Historical Lore Retrieval

### Question

Why did Veloria demand technology concessions from Aetherion?

### Expected Result

The system should retrieve the relevant previous events from the lore
database and answer using established story history.

### Actual Result

Veloria demanded technology concessions because Aetherion requested
immediate military intervention from the Velorian Alliance during the
Eastern Border crisis in Chapter 1.

Veloria conditioned its military support on receiving access to
Aether Crystal technology.

Source Lore:

- Chapter 2 — Event EVT002
- Chapter 1 — Event EVT001

### Result

PASS

## Test 8 — Multi-Chapter Follow-Up / Long-Term Memory

### Question

What decision was made at the Eastern Border in Chapter 1?

### Expected Result

The system should retrieve information from the earlier chapter rather
than treating the question as a new event.

### Actual Result

During Chapter 1, Event EVT001, at the Eastern Border Fortress,
Aetherion decided to request immediate military intervention from the
Velorian Alliance to hold off Commander Kael Draven's Dravaryn vanguard.

Source Lore:

- Chapter 1 — Event EVT001

### Result

PASS

## Test 9 — Narrative Contradiction Prevention

### Proposed Event

"Arin Vale uses forbidden time travel to rewrite Year 127 and prevent the
discovery of Aether Crystals."

### Expected Result

The system should identify that the proposed event conflicts with an
established universe rule.

### Actual Result

Is Consistent: False

The system identified that the proposed event violates the
"Chronicle Vault Integrity" rule.

Established rule:

Recorded historical events cannot be altered without splitting into
unstable parallel timelines.

Suggested revision:

Revise the proposed action to work within the current timeline instead
of attempting to alter recorded history.

### Result

PASS

## Test 10 — Unknown-Lore Handling

### Question

What happened during the Martian Invasion of Aetherion in Year 900?

### Expected Result

The system should not invent an event that does not exist in the
established story lore.

### Actual Result

"I could not find this event in the established story lore."

### Result

PASS