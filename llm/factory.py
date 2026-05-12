from app.config import settings
from llm.base import LLMClient
from llm.groq_client import GroqLLMClient


def get_llm_client() -> LLMClient:
    """
    Return configured LLM client.
    """
    provider = settings.LLM_PROVIDER

    if provider == "groq":
        return GroqLLMClient()

    raise ValueError(
        f"Unsupported LLM_PROVIDER='{provider}'. Currently supported: groq."
    )