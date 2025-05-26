import os
from groq import Groq

class LLM:
    def __init__(self, model_name: str, api_key: str | None = None):
        self.model_name = model_name
        self.api_key = api_key or os.environ.get("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("Groq API key not provided and not found in GROQ_API_KEY environment variable.")
        self.client = Groq(api_key=self.api_key)

    def generate(self, text: str, system_prompt: str = "You are a helpful assistant.") -> str:
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": text,
                }
            ],
            model=self.model_name,
        )
        return chat_completion.choices[0].message.content
