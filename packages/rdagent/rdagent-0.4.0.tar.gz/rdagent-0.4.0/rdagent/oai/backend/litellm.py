from typing import Any

from litellm import (
    completion,
    completion_cost,
    embedding,
    supports_response_schema,
    token_counter,
)

from rdagent.log import LogColors
from rdagent.log import rdagent_logger as logger
from rdagent.oai.backend.base import APIBackend
from rdagent.oai.llm_conf import LLMSettings


class LiteLLMSettings(LLMSettings):

    class Config:
        env_prefix = "LITELLM_"
        """Use `LITELLM_` as prefix for environment variables"""

    # Placeholder for LiteLLM specific settings, so far it's empty


LITELLM_SETTINGS = LiteLLMSettings()
logger.info(f"{LITELLM_SETTINGS}")
ACC_COST = 0.0


class LiteLLMAPIBackend(APIBackend):
    """LiteLLM implementation of APIBackend interface"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def _calculate_token_from_messages(self, messages: list[dict[str, Any]]) -> int:
        """
        Calculate the token count from messages
        """
        num_tokens = token_counter(
            model=LITELLM_SETTINGS.chat_model,
            messages=messages,
        )
        logger.info(f"{LogColors.CYAN}Token count: {LogColors.END} {num_tokens}", tag="debug_litellm_token")
        return num_tokens

    def _create_embedding_inner_function(
        self, input_content_list: list[str], *args: Any, **kwargs: Any
    ) -> list[list[float]]:  # noqa: ARG002
        """
        Call the embedding function
        """
        response_list = []
        for input_content_iter in input_content_list:
            model_name = LITELLM_SETTINGS.embedding_model
            logger.info(f"{LogColors.GREEN}Using emb model{LogColors.END} {model_name}", tag="debug_litellm_emb")
            logger.info(f"Creating embedding for: {input_content_iter}", tag="debug_litellm_emb")
            if not isinstance(input_content_iter, str):
                raise ValueError("Input content must be a string")
            response = embedding(
                model=model_name,
                input=input_content_iter,
                *args,
                **kwargs,
            )
            response_list.append(response.data[0]["embedding"])
        return response_list

    def _create_chat_completion_inner_function(  # type: ignore[no-untyped-def] # noqa: C901, PLR0912, PLR0915
        self,
        messages: list[dict[str, Any]],
        json_mode: bool = False,
        *args,
        **kwargs,
    ) -> tuple[str, str | None]:
        """
        Call the chat completion function
        """
        if json_mode and supports_response_schema(model=LITELLM_SETTINGS.chat_model):
            kwargs["response_format"] = {"type": "json_object"}

        logger.info(self._build_log_messages(messages), tag="llm_messages")
        # Call LiteLLM completion
        response = completion(
            model=LITELLM_SETTINGS.chat_model,
            messages=messages,
            stream=LITELLM_SETTINGS.chat_stream,
            temperature=LITELLM_SETTINGS.chat_temperature,
            max_tokens=LITELLM_SETTINGS.chat_max_tokens,
            **kwargs,
        )
        logger.info(
            f"{LogColors.GREEN}Using chat model{LogColors.END} {LITELLM_SETTINGS.chat_model}", tag="llm_messages"
        )

        if LITELLM_SETTINGS.chat_stream:
            logger.info(f"{LogColors.BLUE}assistant:{LogColors.END}", tag="llm_messages")
            content = ""
            finish_reason = None
            for message in response:
                if message["choices"][0]["finish_reason"]:
                    finish_reason = message["choices"][0]["finish_reason"]
                if "content" in message["choices"][0]["delta"]:
                    chunk = (
                        message["choices"][0]["delta"]["content"] or ""
                    )  # when finish_reason is "stop", content is None
                    content += chunk
                    logger.info(LogColors.CYAN + chunk + LogColors.END, raw=True, tag="llm_messages")

            logger.info("\n", raw=True, tag="llm_messages")
        else:
            content = str(response.choices[0].message.content)
            finish_reason = response.choices[0].finish_reason
            finish_reason_str = (
                f"({LogColors.RED}Finish reason: {finish_reason}{LogColors.END})"
                if finish_reason and finish_reason != "stop"
                else ""
            )
            logger.info(f"{LogColors.BLUE}assistant:{LogColors.END} {finish_reason_str}\n{content}", tag="llm_messages")

        global ACC_COST
        cost = completion_cost(model=LITELLM_SETTINGS.chat_model, messages=messages, completion=content)
        ACC_COST += cost
        logger.info(
            f"Current Cost: ${float(cost):.10f}; Accumulated Cost: ${float(ACC_COST):.10f}; {finish_reason=}",
        )
        return content, finish_reason
