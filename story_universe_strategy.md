# Technical Strategy & Architecture Documentation
## AI Story Universe Generator: Narrative Intelligence & Long-Term Memory System

### 1. World Generation Strategy
- **World Schema**: Defined using Pydantic `WorldSchema` containing `theme`, `kingdoms`, `tech_magic_systems`, `rules`, and `timeline`.
- **Kingdom Generation**: Structured models enforcing geographical, cultural, economic, political, resource, and alliance/enemy attributes to guarantee grounded political dynamics.
- **Universe Rules**: Explicit logical constraints governing magic/tech/physics with specified penalties/consequences to anchor narrative boundaries.
- **Timeline Generation**: Chronological historical events establishing historical precedents, past wars, discoveries, and alliances that serve as world memory foundations.

---

### 2. Character Generation Pipeline
- **Hero & Villain Generation**: Multi-stage workflow generating contrasting protagonists and antagonists. Heroes possess distinct origins, skills, strengths, weaknesses, fears, and secrets. Villains possess rationalized motivations driven by political or ideological ideals rather than senseless evil.
- **Backstory Generation**: Backstories explicitly tie into timeline events (e.g. past border wars or technology discoveries) ensuring deep integration with universe history.
- **Motivation Handling**: Motivations drive character goals and are passed as context to the narrative progression engine to influence dynamic choice responses.
- **Relationship Generation**: Relational matrices mapping pair dynamics (ally, rival, enemy, former ally) with origin stories and underlying ideological conflicts.

---

### 3. Story State & Progression Engine
- **State Structure**: `StoryState` tracks dynamic story metrics including current chapter, location, active characters, character status, active conflict, political situation, relationships, and user decisions.
- **User Choices**: At major narrative junctures, 3 to 4 distinct user choices are presented with explicit risk profiles.
- **Consequence Handling**: Choices trigger `ConsequenceGenerationChain` evaluating immediate outcomes, long-term political shifts, relationship updates, and location transitions.
- **State Updates**: Updates mutate the active `StoryState` object and record events into the story history ledger.

---

### 4. Narrative Memory Architecture
- **Short-Term Memory**: `StoryMemoryManager` retains a rolling sliding window of recent chapter events for immediate conversational context.
- **Long-Term Memory**: All events, user choices, consequences, character profiles, kingdom facts, and universe rules are embedded into the FAISS vector database.
- **Context-Aware Generation**: Scene generation queries long-term vector lore prior to generating narrative continuations.

---

### 5. Lore Storage & Vector Database
- **Lore Types Stored**:
  - `kingdom`: Political structures, resources, alliances
  - `magic_tech`: System capabilities, costs, limitations
  - `rule`: Universe rules and consequences
  - `timeline`: Historical chronological events
  - `character`: Profiles, motivations, backstories
  - `relationship`: Inter-character dynamics
  - `story_event`: Event descriptions, user choices, consequences
- **Metadata Structure**: Each entry stores `type`, `chapter`, `event_id`, `name`/`title`, `location`, and `characters`.
- **Embeddings**:
  - **Provider & Model**: HuggingFace Embeddings (`sentence-transformers/all-MiniLM-L6-v2`)
  - **Reason for Selection**: Highly efficient 384-dimensional dense vectors, zero API dependency, fast local similarity computations, and seamless LangChain integration.
- **Vector Database**: `FAISS` (Facebook AI Similarity Search) local vector store serialized in `data/lore/`.
- **Retrieval Configuration**: `k=4` to `k=5` nearest neighbor cosine similarity retrieval with metadata filtering.

---

### 6. Prompt Engineering & Consistency Control
- **Prompt Architecture**: Modular text templates saved in `prompts/` separating role, task, constraints, world context, lore context, and output format.
- **Consistency Controls**: `ConsistencyCheckerChain` evaluates proposed narrative events against retrieved universe rules and state history before execution.
- **Hallucination Prevention**: Prompt directives enforce strict adherence to established lore and dictate standard fallback responses ("I could not find this event in the established story lore.") when queried about non-existent events.
