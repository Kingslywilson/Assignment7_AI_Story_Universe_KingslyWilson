import os
import json
from langchain_core.prompts import ChatPromptTemplate
from models import CharacterProfile

class CharacterGenerationChain:
    def __init__(self, llm, prompt_path: str = "prompts/character_generation_prompt.txt"):
        self.llm = llm
        if os.path.exists(prompt_path):
            with open(prompt_path, "r", encoding="utf-8") as f:
                template_str = f.read()
        else:
            template_str = "Generate a {role} for world: {world_context}. Context: {lore_context}"
        
        self.prompt = ChatPromptTemplate.from_template(template_str)

    def run(self, world_context: str, role: str, lore_context: str = "None") -> CharacterProfile:
        if hasattr(self.llm, "_llm_type") and self.llm._llm_type != "dummy-llm":
            try:
                structured_llm = self.llm.with_structured_output(CharacterProfile)
                chain = self.prompt | structured_llm
                result = chain.invoke({
                    "world_context": world_context,
                    "role": role,
                    "lore_context": lore_context
                })
                if isinstance(result, CharacterProfile):
                    return result
            except Exception:
                pass

            try:
                chain = self.prompt | self.llm
                raw_output = chain.invoke({
                    "world_context": world_context,
                    "role": role,
                    "lore_context": lore_context
                })
                text = raw_output.content if hasattr(raw_output, "content") else str(raw_output)
                start_idx = text.find("{")
                end_idx = text.rfind("}") + 1
                if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
                    clean_json = text[start_idx:end_idx]
                    data = json.loads(clean_json)
                    return CharacterProfile(**data)
            except Exception:
                pass

        if role.lower() == "hero":
            return CharacterProfile(
                name="Arin Vale",
                role="Hero",
                origin="Aetherion",
                age="28",
                skills=["Swordsmanship", "Aether Engineering", "Tactical Command"],
                strengths=["Courageous", "Tech-savvy", "Loyal to citizens"],
                weaknesses=["Distrusts political leaders", "Impulsive under threat"],
                personality="Determined, introspective, protective",
                backstory="Lost his family during the Dravaryn expansion into the Northern Territories (Year 148). Dedicated his life to mastering Aether tech to safeguard the innocent.",
                motivation="Protect the kingdom and prevent centralized tyranny after losing his family.",
                goals=["Defend Aetherion's borders", "Uncover ancient Aether secrets"],
                fears=["Failing his companions", "Seeing Elyra fall"],
                relationships=["Former comrade of Kael Draven"],
                secrets="Possesses a classified schematic for an ancient Aether core"
            )
        else:
            return CharacterProfile(
                name="Kael Draven",
                role="Villain",
                origin="Dravaryn Empire",
                age="35",
                skills=["Strategic Warfare", "Obsidian Metallurgy", "Mind Manipulation"],
                strengths=["Brilliant strategist", "Unwavering resolve", "Charismatic leader"],
                weaknesses=["Inflexible idealism", "Underestimates rebel resilience"],
                personality="Cold, calculating, vision-driven",
                backstory="Distinguished Dravaryn commander who believes chaotic independent kingdoms inevitably breed endless war.",
                motivation="Believes centralized control is the only way to establish permanent continental peace.",
                goals=["Unify all realms under Dravaryn law", "Neutralize independent Aether tech"],
                fears=["Endless war consuming the continent"],
                relationships=["Former ally turned enemy of Arin Vale"],
                secrets="Suffers from corruption caused by early Obsidian ore experiments"
            )
