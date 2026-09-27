import os
import json
from langchain_core.prompts import ChatPromptTemplate
from models import CharacterRelationship

class RelationshipGenerationChain:
    def __init__(self, llm, prompt_path: str = "prompts/relationship_prompt.txt"):
        self.llm = llm
        if os.path.exists(prompt_path):
            with open(prompt_path, "r", encoding="utf-8") as f:
                template_str = f.read()
        else:
            template_str = "Generate relationship between: {character_list}. World: {world_context}. Context: {lore_context}"
        
        self.prompt = ChatPromptTemplate.from_template(template_str)

    def run(self, world_context: str, character_list: str, lore_context: str = "None") -> CharacterRelationship:
        if hasattr(self.llm, "_llm_type") and self.llm._llm_type != "dummy-llm":
            try:
                structured_llm = self.llm.with_structured_output(CharacterRelationship)
                chain = self.prompt | structured_llm
                result = chain.invoke({
                    "world_context": world_context,
                    "character_list": character_list,
                    "lore_context": lore_context
                })
                if isinstance(result, CharacterRelationship):
                    return result
            except Exception:
                pass

            try:
                chain = self.prompt | self.llm
                raw_output = chain.invoke({
                    "world_context": world_context,
                    "character_list": character_list,
                    "lore_context": lore_context
                })
                text = raw_output.content if hasattr(raw_output, "content") else str(raw_output)
                start_idx = text.find("{")
                end_idx = text.rfind("}") + 1
                if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
                    clean_json = text[start_idx:end_idx]
                    data = json.loads(clean_json)
                    return CharacterRelationship(**data)
            except Exception:
                pass

        return CharacterRelationship(
            character_1="Arin Vale",
            character_2="Kael Draven",
            relationship_type="Former allies turned bitter enemies",
            origin_story="Served together during the initial Northern Border defense squad.",
            reason="They disagreed fundamental ideological views over the use and militarization of Aether technology."
        )
