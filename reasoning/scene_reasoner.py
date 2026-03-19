import requests
import json
import os

from rag.retriever import Retriever
from reasoning.prompt_templates import SCENE_REASONING_PROMPT


class SceneReasoner:

    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.retriever = Retriever()

    def reason(self, scene):

        rules = self.retriever.retrieve(scene)
        print("\nRAG Retrieved Rules:")
        print(rules) 


        context = "\n".join(rules)

        prompt = SCENE_REASONING_PROMPT.format(
            scene=scene,
            context=context
        )

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}"
            },
            json={
                "model": "qwen/qwen-2.5-7b-instruct",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        result = response.json()

        print("LLM raw response:", result)

        content = result["choices"][0]["message"]["content"]

        return json.loads(content) 