import os
import json
from langchain_core.prompts import ChatPromptTemplate
from models import WorldSchema, Kingdom, TechMagicSystem, UniverseRule, TimelineEvent

class WorldGenerationChain:
    def __init__(self, llm, prompt_path: str = "prompts/world_generation_prompt.txt"):
        self.llm = llm
        if os.path.exists(prompt_path):
            with open(prompt_path, "r", encoding="utf-8") as f:
                template_str = f.read()
        else:
            template_str = "Generate a fictional world for theme: {theme}. Context: {lore_context}"
        
        self.prompt = ChatPromptTemplate.from_template(template_str)

    def run(self, theme: str, lore_context: str = "None") -> WorldSchema:
        if hasattr(self.llm, "_llm_type") and self.llm._llm_type != "dummy-llm":
            try:
                structured_llm = self.llm.with_structured_output(WorldSchema)
                chain = self.prompt | structured_llm
                result = chain.invoke({"theme": theme, "lore_context": lore_context})
                if isinstance(result, WorldSchema):
                    return result
            except Exception:
                pass

            try:
                chain = self.prompt | self.llm
                raw_output = chain.invoke({"theme": theme, "lore_context": lore_context})
                text = raw_output.content if hasattr(raw_output, "content") else str(raw_output)
                start_idx = text.find("{")
                end_idx = text.rfind("}") + 1
                if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
                    clean_json = text[start_idx:end_idx]
                    data = json.loads(clean_json)
                    return WorldSchema(**data)
            except Exception:
                pass

        return WorldSchema(
            theme=theme,
            kingdoms=[
                Kingdom(
                    name="Aetherion",
                    capital="Elyra",
                    government="Council Monarchy",
                    primary_resource="Aether Crystals",
                    culture="High-tech arcanists and scholars",
                    geography="Floating sky islands and crystalline towers",
                    economy="Aether crystal trading and arcane tech exports",
                    allies=["Veloria"],
                    enemies=["Dravaryn Empire"],
                    important_locations=["The Grand Citadel", "Aether Crystal Vaults"],
                    political_importance="Dominant economic and technological hub"
                ),
                Kingdom(
                    name="Dravaryn Empire",
                    capital="Vraks",
                    government="Military Autocracy",
                    primary_resource="Obsidian Ore",
                    culture="Martial, expansionist, disciplined",
                    geography="Volcanic mountain ranges and obsidian fortresses",
                    economy="Heavy metallurgy and military conquest",
                    allies=[],
                    enemies=["Aetherion", "Veloria"],
                    important_locations=["The Iron Citadel", "The Dread Forges"],
                    political_importance="Formidable military superpower"
                )
            ],
            tech_magic_systems=[
                TechMagicSystem(
                    name="Aether Engineering",
                    purpose="Converts raw Aether Crystals into clean power and anti-gravity thrust",
                    capabilities=["Infinite power generation", "Levitation", "Energy shielding"],
                    limitations=["Continuous overload destabilizes surrounding magnetic fields"],
                    users=["Licensed Engineers and Guild Technicians"],
                    cost_or_consequence="Overuse causes localized mana corruption and magnetic storms",
                    origin="Discovered in Year 127 within the Sunken Vaults"
                )
            ],
            rules=[
                UniverseRule(
                    rule="Chronicle Vault Integrity",
                    category="Magic/Time",
                    consequence="Recorded historical events cannot be altered without splitting into unstable parallel timelines"
                )
            ],
            timeline=[
                TimelineEvent(
                    year_or_era="Year 127",
                    title="Discovery of Aether Crystals",
                    description="Aetherion miners uncover crystalline energy veins beneath Elyra",
                    key_factions=["Aetherion"],
                    impact="Revolutionized continental power generation and sky travel"
                ),
                TimelineEvent(
                    year_or_era="Year 148",
                    title="The Dravaryn Expansion",
                    description="Dravaryn armies annex northern borderlands",
                    key_factions=["Dravaryn Empire"],
                    impact="Ignited the Great Northern War"
                )
            ]
        )
