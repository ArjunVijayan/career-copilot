"""
app/infrastructure/llm/mistral_client.py

Local Mistral client using Ollama.
"""

from __future__ import annotations

import json
from app.core.logger import get_logger
from typing import Any

import ollama

from app.core.config.settings import settings

logger = get_logger(__name__)


class MistralClient:
    """
    Wrapper around local Mistral models served via Ollama.
    """

    def __init__(
        self,
        model: str | None = None,
        temperature: float = 0.2,
    ) -> None:
        self.model = model or settings.MISTRAL_MODEL
        self.temperature = temperature

        logger.info(
            "Initialized MistralClient with model=%s",
            self.model,
        )

    def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:
        """
        Generate plain text response from Mistral.
        """

        try:
            messages: list[dict[str, str]] = []

            if system_prompt:
                messages.append(
                    {
                        "role": "system",
                        "content": system_prompt,
                    }
                )

            messages.append(
                {
                    "role": "user",
                    "content": prompt,
                }
            )

            response = ollama.chat(
                model=self.model,
                messages=messages,
                options={
                    "temperature": self.temperature,
                },
            )

            content = response["message"]["content"]

            logger.info("LLM generation successful")

            return content

        except Exception as exc:
            logger.exception(
                "Failed during Mistral generation"
            )
            raise RuntimeError(
                "Mistral generation failed"
            ) from exc

    def generate_json(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> dict[str, Any]:
        """
        Generate structured JSON response.
        """

        response = self.generate(
            prompt=prompt,
            system_prompt=system_prompt,
        )

        try:
            parsed = json.loads(response)

            logger.info("JSON parsing successful")

            return parsed

        except json.JSONDecodeError as exc:
            logger.exception(
                "Invalid JSON response from model"
            )

            raise ValueError(
                "Model returned invalid JSON"
            ) from exc
        

if __name__ == "__main__":
    client = MistralClient()
    test_prompt = "What is 2 + 2?"
    result = client.generate(test_prompt)
    print("LLM Response:", result)