from abc import ABC, abstractmethod


class LLMClient(ABC):
    """
    Abstract interface for LLM providers.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate text from a prompt.
        """
        pass