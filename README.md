# AI Story Universe Generator

## Assignment 7 — AI Story Universe Generator

A Python and LangChain-based **Narrative Intelligence and Long-Term Memory System** that creates a fictional story universe, generates characters and relationships, manages user-driven story progression, stores evolving lore, retrieves historical context using embeddings and FAISS, and maintains narrative consistency across multiple story events.

---

## 1. Project Overview

The AI Story Universe Generator is designed as a long-running narrative intelligence system rather than a simple story-generation application.

The system combines:

* World building
* Kingdom and region generation
* Technology and magic systems
* Universe rules
* Historical timeline generation
* Hero generation
* Villain generation
* Character backstories
* Character motivations
* Character relationships
* Structured story state
* User-driven story choices
* Story consequences
* Long-term narrative memory
* Lore storage
* Embeddings
* FAISS vector database
* Semantic lore retrieval
* Context-aware story generation
* Narrative consistency checking
* Unknown-lore handling

The application demonstrates how LangChain and Python can be used to maintain information across a long-running fictional narrative.

---

## 2. Main Objective

The objective is to build a narrative intelligence system that follows this workflow:

```text
World Building
      ↓
Character Generation
      ↓
Motivations & Relationships
      ↓
Structured Story State
      ↓
User Choices
      ↓
Consequences
      ↓
Narrative Memory
      ↓
Lore Storage
      ↓
Embeddings
      ↓
FAISS Vector Database
      ↓
Lore Retrieval
      ↓
Relevant Historical Context
      ↓
Consistent Story Generation
```

The system uses previously established information when generating new story events.

---

## 3. Features

### World Building

The system generates:

* Fictional kingdoms
* Regions
* Capitals
* Resources
* Political relationships
* Technology or magic systems
* Universe rules
* Historical timeline

Example generated universe:

```text
Theme:
High-Fantasy Aetherpunk Continental Conflict

Kingdoms:
Aetherion
Dravaryn Empire

Technology:
Aether Engineering

Universe Rule:
Chronicle Vault Integrity

Historical Events:
Year 127 — Discovery of Aether Crystals
Year 148 — The Dravaryn Expansion
```

---

### Character Generation

The system generates heroes and villains with structured information.

Characters can contain:

* Name
* Role
* Origin
* Faction
* Skills
* Strengths
* Weaknesses
* Backstory
* Motivation
* Goals
* Relationships
* Conflicts

Example:

```text
Hero:
Arin Vale

Origin:
Aetherion

Skills:
Swordsmanship
Aether Engineering
Tactical Command

Motivation:
Protect the kingdom and prevent centralized tyranny.
```

Example villain:

```text
Villain:
Kael Draven

Origin:
Dravaryn Empire

Motivation:
Establish permanent continental peace through centralized control.
```

---

## 4. Technology Stack

### Programming Language

* Python 3.11

### AI / LLM Framework

* LangChain

### LLM

* Groq
* ChatGroq

### Embeddings

* Hugging Face Embeddings

### Vector Database

* FAISS

### Data Validation

* Pydantic

### Configuration

* Python environment variables
* `.env`

### Supporting Libraries

* python-dotenv
* LangChain components
* FAISS
* Hugging Face embedding integration

---

## 5. LangChain Concepts Demonstrated

The project demonstrates the following LangChain concepts:

### Prompt Templates

Separate prompts are used for major narrative-generation stages.

Examples:

```text
world_generation_prompt.txt
character_generation_prompt.txt
relationship_prompt.txt
story_progression_prompt.txt
consequence_prompt.txt
consistency_prompt.txt
```

### Multi-Stage Workflows

The system separates narrative generation into multiple stages:

```text
World
 ↓
Characters
 ↓
Relationships
 ↓
Story Event
 ↓
User Choice
 ↓
Consequence
 ↓
State Update
 ↓
Lore Storage
 ↓
Retrieval
 ↓
Next Event
```

### Structured Output

Pydantic models are used to maintain consistent data structures for:

* World information
* Characters
* Relationships
* Story events
* Story state
* Timeline information

### Embeddings

Story lore is converted into vector embeddings using Hugging Face embeddings.

### Vector Store

FAISS stores the generated lore vectors and associated metadata.

### Retriever Interface

The application retrieves relevant historical lore before answering historical questions or generating context-dependent story information.

### Context-Aware Generation

Retrieved lore is supplied to the generation process so that new story events can use established information.

### Error / Unknown Lore Handling

The system avoids inventing historical events that are not present in the established lore.

---

## 6. Project Structure

```text
Assignment7_AI_Story_Universe_KingslyWilson/
│
├── app.py
├── story_engine.py
├── story_state.py
├── memory.py
├── vector_store.py
├── lore_retriever.py
├── models.py
│
├── chains/
│   ├── world_generation.py
│   ├── character_generation.py
│   ├── relationship_generation.py
│   ├── story_progression.py
│   ├── consequence_generation.py
│   └── consistency_checker.py
│
├── prompts/
│   ├── world_generation_prompt.txt
│   ├── character_generation_prompt.txt
│   ├── relationship_prompt.txt
│   ├── story_progression_prompt.txt
│   ├── consequence_prompt.txt
│   └── consistency_prompt.txt
│
├── data/
│   └── lore/
│       ├── index.faiss
│       └── index.pkl
│
├── outputs/
│   ├── world.json
│   ├── characters.json
│   ├── timeline.json
│   └── story_history.json
│
├── story_universe_strategy.md
├── test_log.md
├── README.md
├── requirements.txt
└── .env.example
```

---

## 7. Important Python Files

### `app.py`

Main application entry point.

It executes the narrative scenarios and demonstrates:

1. Initial world generation
2. Character generation
3. User choice
4. Choice consequences
5. Historical lore retrieval
6. Long-term memory
7. Contradiction prevention
8. Unknown-lore handling

Run the application using:

```bash
python app.py
```

---

### `story_engine.py`

Coordinates the overall narrative workflow.

It connects:

* World generation
* Character generation
* Story progression
* Consequence generation
* Lore retrieval
* Consistency checking

---

### `models.py`

Contains structured Pydantic models used by the application.

These models provide consistent representations of generated narrative data.

---

### `story_state.py`

Maintains the current state of the story.

The state can contain information such as:

* Current chapter
* Current location
* Active characters
* Character status
* Relationships
* Current conflict
* Political situation
* Recent choices
* Story goals
* Completed events

---

### `memory.py`

Handles narrative memory and persistence of story information.

---

### `vector_store.py`

Creates and manages the FAISS vector database.

It handles:

* Embedding generation
* Vector storage
* FAISS persistence
* Loading the existing vector index

---

### `lore_retriever.py`

Provides the retrieval interface used to find relevant historical lore.

It retrieves information based on semantic similarity rather than only exact keyword matching.

---

## 8. Prompt Architecture

The project uses separate prompts for different narrative tasks.

### World Generation

```text
prompts/world_generation_prompt.txt
```

Responsible for generating:

* Kingdoms
* Technology/magic
* Universe rules
* Timeline

### Character Generation

```text
prompts/character_generation_prompt.txt
```

Responsible for:

* Heroes
* Villains
* Backstories
* Motivations
* Goals

### Relationship Generation

```text
prompts/relationship_prompt.txt
```

Responsible for character relationships and conflicts.

### Story Progression

```text
prompts/story_progression_prompt.txt
```

Responsible for generating story events and user choices.

### Consequence Generation

```text
prompts/consequence_prompt.txt
```

Responsible for determining consequences of user decisions.

### Consistency Checking

```text
prompts/consistency_prompt.txt
```

Responsible for checking proposed events against established world rules and lore.

---

## 9. Environment Configuration

API credentials are stored using environment variables.

Create a local `.env` file based on `.env.example`.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

Do not commit the actual `.env` file.

The `.env` file must never be included in the submission ZIP.

---

## 10. Installation

### Step 1 — Create a Virtual Environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

---

### Step 2 — Install Dependencies

```powershell
pip install -r requirements.txt
```

If required by the installed LangChain version, install the Hugging Face integration:

```powershell
pip install -U langchain-huggingface
```

---

### Step 3 — Configure Environment Variables

Create:

```text
.env
```

Example:

```env
GROQ_API_KEY=your_actual_api_key
```

The real API key must not be included in the ZIP.

---

### Step 4 — Run the Application

```powershell
python app.py
```

---

## 11. Running the Application

The application automatically demonstrates the complete narrative workflow.

The execution contains the following scenarios:

```text
SCENARIO 1
Initial World Generation

SCENARIO 2
Character Generation & Relationships

SCENARIO 3
User Choice & Story Progression

SCENARIO 4
Choice Consequences & Relationship Change

SCENARIO 5
Historical Lore Retrieval

SCENARIO 6
Long-Term Follow-Up Query

SCENARIO 7
Contradiction Prevention

SCENARIO 8
Unknown Lore Handling
```

---

## 12. World Generation

The first stage generates the fictional universe.

The generated information is stored in structured form.

Example:

```text
Aetherion
Capital: Elyra
Resource: Aether Crystals

Dravaryn Empire
Capital: Vraks
Resource: Obsidian Ore
```

The system also generates the technology system:

```text
Aether Engineering

Capability:
Converts raw Aether Crystals into clean power and anti-gravity thrust.

Limitation:
Continuous overload destabilizes surrounding magnetic fields.
```

---

## 13. Universe Rules

The world contains explicit rules that should be respected by future story events.

Example:

```text
Rule:
Chronicle Vault Integrity

Consequence:
Recorded historical events cannot be altered without splitting into
unstable parallel timelines.
```

These rules are later used by the consistency checker.

---

## 14. Timeline

The initial timeline establishes the historical foundation of the universe.

Example:

```text
Year 127:
Discovery of Aether Crystals

Year 148:
The Dravaryn Expansion
```

Timeline information becomes part of the narrative lore.

---

## 15. Character Generation

Characters are generated using the established world context.

The generated character information includes:

```text
Name
Role
Origin
Backstory
Motivation
Skills
Strengths
Weaknesses
Goals
Relationships
```

This prevents characters from being generated independently of the fictional world.

---

## 16. User Choices

At important story moments, the system generates multiple choices.

Example:

```text
1. Send defensive reinforcements.
2. Attempt diplomatic negotiations.
3. Secretly evacuate civilians.
4. Request military intervention from Veloria.
```

The user selects an option.

The selected choice becomes part of the story state.

---

## 17. Consequence System

User choices affect subsequent story events.

For example:

```text
Choice:
Request immediate military intervention from Veloria.

Consequence:
Aetherion receives support but Veloria demands access to
Aether Crystal technology.
```

The consequence becomes part of the evolving story.

---

## 18. Story State

The application maintains structured story state.

Example information includes:

```text
Current Chapter
Current Location
Active Characters
Active Conflict
Political Situation
Recent Choice
Character Relationships
Completed Events
```

This allows future events to reflect earlier decisions.

---

## 19. Long-Term Narrative Memory

Important story events are stored as lore.

For example:

```text
Chapter 1
Event EVT001

Aetherion requested military intervention from Veloria.
```

Later, the system can retrieve this information:

```text
Question:
What decision was made at the Eastern Border in Chapter 1?

Answer:
Aetherion requested immediate military intervention from the
Velorian Alliance.
```

This demonstrates multi-chapter narrative memory.

---

## 20. Lore Storage

The system stores important narrative information including:

* Kingdoms
* Technology systems
* Universe rules
* Timeline events
* Character profiles
* Character motivations
* Relationships
* Story events
* User decisions
* Consequences
* Political changes

Lore is persisted in the project data directory.

---

## 21. Embeddings

The application uses a Hugging Face embedding model to convert narrative lore into numerical vector representations.

This allows semantically similar pieces of lore to be retrieved even when the query does not use exactly the same wording as the original event.

---

## 22. FAISS Vector Database

FAISS is used as the vector database.

The persisted vector store is located under:

```text
data/lore/
```

The database contains the vector representations of stored narrative information.

Each lore document can contain metadata such as:

```text
type
event_id
chapter
characters
location
```

---

## 23. Lore Retrieval

Before answering questions about previous events, the system retrieves relevant lore.

Example:

```text
User:
Why did Veloria demand technology concessions from Aetherion?
```

The system retrieves relevant events such as:

```text
Chapter 1 — EVT001
Chapter 2 — EVT002
```

and uses those events to construct the response.

---

## 24. Contextual Story Generation

The narrative engine uses relevant historical context before generating subsequent story information.

Conceptually:

```text
New Story Request
       ↓
Current Story State
       ↓
Retrieve Relevant Lore
       ↓
Retrieve Character Information
       ↓
Retrieve Relationships
       ↓
Retrieve Timeline
       ↓
Check Universe Rules
       ↓
Generate Story Event
       ↓
Update Story State
       ↓
Store New Lore
```

---

## 25. Narrative Consistency

The consistency checker verifies new events against established information.

The system checks:

* Universe rules
* Character status
* Character relationships
* Previous events
* Timeline
* Existing lore
* Story state

Example contradiction:

```text
Arin Vale uses forbidden time travel to rewrite Year 127 and
prevent the discovery of Aether Crystals.
```

The system identifies the event as inconsistent because it violates the:

```text
Chronicle Vault Integrity
```

rule.

Result:

```text
Is Consistent: False
```

---

## 26. Unknown-Lore Handling

The application does not intentionally invent historical events that are absent from the stored lore.

Example:

```text
Question:
What happened during the Martian Invasion of Aetherion in Year 900?
```

Response:

```text
I could not find this event in the established story lore.
```

This provides protection against unsupported historical claims within the fictional universe.

---

## 27. Test Log

Testing results are documented in:

```text
test_log.md
```

The test log covers:

* World generation
* Kingdom generation
* Universe rules
* Timeline generation
* Hero generation
* Villain generation
* Character motivation
* Character relationships
* User choices
* Consequences
* Story-state updates
* Lore retrieval
* Multi-chapter memory
* Contradiction prevention
* Unknown-lore handling

The test log is based on the output produced by the running application.

---

## 28. Strategy Documentation

The implementation strategy is documented in:

```text
story_universe_strategy.md
```

The document describes:

* World generation
* Character pipeline
* Story state
* User choices
* Consequences
* Narrative memory
* Lore storage
* Embeddings
* FAISS
* Retrieval
* Prompt design
* Consistency controls
* Hallucination prevention

---

## 29. Output Files

The application produces structured output files under:

```text
outputs/
```

### `world.json`

Contains generated world information.

### `characters.json`

Contains generated character information.

### `timeline.json`

Contains historical timeline information.

### `story_history.json`

Contains story events and progression history.

---

## 30. Error and Failure Handling

The system handles several narrative failure scenarios:

### Unknown Lore

The system reports when an event cannot be found in established lore.

### Contradictory Events

The consistency checker identifies events that conflict with established universe rules.

### Invalid Narrative Changes

The system can recommend modifying a proposed event so that it remains compatible with the existing timeline.

---

## 31. Security

API credentials are loaded from environment variables.

The following must never be committed:

```text
.env
API keys
Passwords
Access tokens
```

The submission should contain:

```text
.env.example
```

instead of the actual `.env`.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

---

## 32. Files Excluded from Submission

Do not include:

```text
.env
venv/
.venv/
__pycache__/
IDE configuration
Temporary files
Cache files
Large downloaded models
Unrelated files
```

---

## 33. Known Limitations

* The application depends on access to the configured LLM provider.
* Generated narratives depend on the quality and availability of the LLM.
* FAISS provides vector similarity retrieval but does not provide a full relational database.
* Very large story universes may require additional memory-management and summarization strategies.
* The current application is designed as a demonstration of narrative intelligence rather than a production-scale multiplayer storytelling platform.
* Generated story content is probabilistic, so consistency checking is used to reduce contradictions.

---

## 34. Example Execution

A successful execution follows this general sequence:

```text
AI STORY UNIVERSE GENERATOR
        ↓
Initial World Generation
        ↓
Aetherion + Dravaryn Empire
        ↓
Aether Engineering
        ↓
Chronicle Vault Integrity
        ↓
Timeline Generation
        ↓
Arin Vale + Kael Draven
        ↓
Character Relationship
        ↓
Chapter 1
        ↓
User selects Velorian intervention
        ↓
Chapter 2
        ↓
Veloria requests Aether technology
        ↓
Lore Retrieval
        ↓
Long-Term Memory
        ↓
Consistency Check
        ↓
Unknown-Lore Handling
        ↓
Execution Complete
```

---

## 35. Assignment Requirement Mapping

| Requirement                | Implementation                          |
| -------------------------- | --------------------------------------- |
| Python                     | Python application                      |
| LangChain                  | LangChain chains and LLM integration    |
| LLM                        | Groq / ChatGroq                         |
| Structured output          | Pydantic models                         |
| PromptTemplate / prompts   | Dedicated prompt files                  |
| Multi-stage workflow       | Multiple generation and checking stages |
| Story memory               | Story state and persistent history      |
| Embeddings                 | Hugging Face embeddings                 |
| Vector database            | FAISS                                   |
| Retriever                  | Lore retriever                          |
| World building             | World generation chain                  |
| Kingdom generation         | World generation                        |
| Magic/technology           | World generation                        |
| Universe rules             | World generation                        |
| Timeline                   | Timeline generation                     |
| Hero generation            | Character generation                    |
| Villain generation         | Character generation                    |
| Backstories                | Character generation                    |
| Motivations                | Character generation                    |
| Relationships              | Relationship generation                 |
| User choices               | Story progression                       |
| Consequences               | Consequence generation                  |
| Long narrative progression | Story state                             |
| Lore storage               | Persistent lore                         |
| Historical retrieval       | FAISS retrieval                         |
| Context-aware generation   | Retrieved lore + prompts                |
| Consistency checking       | Consistency checker                     |
| Unknown-lore handling      | Lore retrieval validation               |

---

## 36. Final Submission Checklist

Before creating the final ZIP, verify:

* [ ] `app.py` runs successfully
* [ ] World generation works
* [ ] Kingdoms/regions are generated
* [ ] Technology/magic system is generated
* [ ] Universe rules are generated
* [ ] Timeline is generated
* [ ] Hero is generated
* [ ] Villain is generated
* [ ] Motivations are generated
* [ ] Relationships are generated
* [ ] User choice works
* [ ] Consequences are generated
* [ ] Story state is updated
* [ ] Lore is stored
* [ ] FAISS vector store is available
* [ ] Lore retrieval works
* [ ] Multi-chapter memory works
* [ ] Contradiction prevention works
* [ ] Unknown-lore handling works
* [ ] `story_universe_strategy.md` is included
* [ ] `test_log.md` contains actual execution results
* [ ] `requirements.txt` is included
* [ ] `.env.example` is included
* [ ] Actual `.env` is removed
* [ ] No API key appears anywhere in the project
* [ ] No `venv/` is included
* [ ] No `__pycache__/` is included

---

## 37. Running the Project

After extracting the project:

```powershell
cd Assignment7_AI_Story_Universe_KingslyWilson
```

Activate the environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Configure the environment:

```text
.env
```

Then run:

```powershell
python app.py
```

A successful run should finish with:

```text
EXECUTION COMPLETE. All artifacts and state persisted in outputs/ and data/lore/
```

---

## 38. Conclusion

This project demonstrates a Python and LangChain-based narrative intelligence system that goes beyond simple text generation.

The application combines:

```text
World Building
+
Character Intelligence
+
Structured Story State
+
User Decisions
+
Consequences
+
Narrative Memory
+
Embeddings
+
FAISS
+
Lore Retrieval
+
Context-Aware Generation
+
Consistency Checking
```

This architecture allows the fictional universe to evolve across multiple story events while preserving important historical context and established narrative rules.
