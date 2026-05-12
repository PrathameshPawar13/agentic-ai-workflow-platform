from groq import Groq
from app.config import settings
from llm.base import LLMClient


class GroqLLMClient(LLMClient):
    """
    Groq-backed LLM client using open-weight models.
    """

    def __init__(self):
        if not settings.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is missing. Add it to your .env file.")

        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model = settings.GROQ_MODEL

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI data analysis assistant. "
                        "Return concise, structured, factual insights. "
                        "Use only the provided analysis data. "
                        "Do not invent numbers or facts."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.1,
        )

        return response.choices[0].message.content