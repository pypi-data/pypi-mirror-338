"""Qwen QwQ Thingking chat models."""

from json import JSONDecodeError
from typing import Any, AsyncIterator, Dict, Iterator, List, Optional, Type, Union

import json_repair as json
import openai
from langchain_core.callbacks import (
    CallbackManagerForLLMRun,
)
from langchain_core.messages import (
    AIMessage,
    AIMessageChunk,
    BaseMessage,
)
from langchain_core.outputs import ChatGeneration, ChatGenerationChunk, ChatResult
from langchain_core.utils import from_env, secret_from_env
from langchain_openai.chat_models.base import BaseChatOpenAI
from pydantic import ConfigDict, Field, SecretStr, model_validator
from typing_extensions import Self

DEFAULT_API_BASE = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"


class ChatQwQ(BaseChatOpenAI):
    """Qwen QwQ Thinking chat model integration to access models hosted in Qwen QwQ Thinking's API.

    Setup:
        Install ``langchain-qwq`` and set environment variable ``DASHSCOPE_API_KEY``.

        .. code-block:: bash

            pip install -U langchain-qwq
            export DASHSCOPE_API_KEY="your-api-key"

    Key init args — completion params:
        model: str
            Name of Qwen QwQ Thinking model to use, e.g. "qwen-qwen2.5-coder-32b-instruct".
        temperature: float
            Sampling temperature.
        max_tokens: Optional[int]
            Max number of tokens to generate.

    Key init args — client params:
        timeout: Optional[float]
            Timeout for requests.
        max_retries: int
            Max number of retries.
        api_key: Optional[str]
            Qwen QwQ Thingking API key. If not passed in will be read from env var DASHSCOPE_API_KEY.

    See full list of supported init args and their descriptions in the params section.

    Instantiate:
        .. code-block:: python

            from langchain_qwq import ChatQwQ

            llm = ChatQwQ(
                model="...",
                temperature=0,
                max_tokens=None,
                timeout=None,
                max_retries=2,
                # api_key="...",
                # other params...
            )

    Invoke:
        .. code-block:: python

            messages = [
                ("system", "You are a helpful translator. Translate the user sentence to French."),
                ("human", "I love programming."),
            ]
            llm.invoke(messages)

    Stream:
        .. code-block:: python

            for chunk in llm.stream(messages):
                print(chunk.text(), end="")

        .. code-block:: python

            stream = llm.stream(messages)
            full = next(stream)
            for chunk in stream:
                full += chunk
            full

    Async:
        .. code-block:: python

            # Basic async invocation
            result = await llm.ainvoke(messages)

            # Access content and reasoning
            content = result.content
            reasoning = result.additional_kwargs.get("reasoning_content", "")

            # Stream response chunks
            async for chunk in await llm.astream(messages):
                print(chunk.content, end="")
                # Access reasoning in each chunk
                reasoning_chunk = chunk.additional_kwargs.get("reasoning_content", "")

            # Process tool calls in completion
            if hasattr(result, "tool_calls") and result.tool_calls:
                for tool_call in result.tool_calls:
                    tool_id = tool_call.get("id")
                    tool_name = tool_call.get("name")
                    tool_args = tool_call.get("args")
                    # Process tool call...

            # Batch processing of multiple message sets
            results = await llm.abatch([messages1, messages2])

    """  # noqa: E501

    model_name: str = Field(alias="model")
    """The name of the model"""
    api_key: Optional[SecretStr] = Field(
        default_factory=secret_from_env("DASHSCOPE_API_KEY", default=None)
    )
    """DeepSeek API key"""
    api_base: str = Field(
        default_factory=from_env("DASHSCOPE_API_BASE", default=DEFAULT_API_BASE)
    )
    """DeepSeek API base URL"""

    model_config = ConfigDict(populate_by_name=True)

    @property
    def _llm_type(self) -> str:
        """Return type of chat model."""
        return "chat-qwq"

    @property
    def lc_secrets(self) -> Dict[str, str]:
        """A map of constructor argument names to secret ids."""
        return {"api_key": "DASHSCOPE_API_KEY"}

    @model_validator(mode="after")
    def validate_environment(self) -> Self:
        if self.api_base == DEFAULT_API_BASE and not (
            self.api_key and self.api_key.get_secret_value()
        ):
            raise ValueError(
                "If using default api base, DASHSCOPE_API_KEY must be set."
            )
        client_params: dict = {
            k: v
            for k, v in {
                "api_key": self.api_key.get_secret_value() if self.api_key else None,
                "base_url": self.api_base,
                "timeout": self.request_timeout,
                "max_retries": self.max_retries,
                "default_headers": self.default_headers,
                "default_query": self.default_query,
            }.items()
            if v is not None
        }

        if not (self.client or None):  # type: ignore
            sync_specific: dict = {"http_client": self.http_client}
            self.root_client = openai.OpenAI(**client_params, **sync_specific)
            self.client = self.root_client.chat.completions
        if not (self.async_client or None):  # type: ignore
            async_specific: dict = {"http_client": self.http_async_client}
            self.root_async_client = openai.AsyncOpenAI(
                **client_params,
                **async_specific,
            )
            self.async_client = self.root_async_client.chat.completions
        return self

    def _create_chat_result(
        self,
        response: Union[dict, openai.BaseModel],
        generation_info: Optional[Dict] = None,
    ) -> ChatResult:
        rtn = super()._create_chat_result(response, generation_info)

        if not isinstance(response, openai.BaseModel):
            return rtn

        if hasattr(response.choices[0].message, "reasoning_content"):  # type: ignore
            rtn.generations[0].message.additional_kwargs["reasoning_content"] = (
                response.choices[0].message.reasoning_content  # type: ignore
            )
        # Handle use via OpenRouter
        elif hasattr(response.choices[0].message, "model_extra"):  # type: ignore
            model_extra = response.choices[0].message.model_extra  # type: ignore
            if isinstance(model_extra, dict) and (
                reasoning := model_extra.get("reasoning")
            ):
                rtn.generations[0].message.additional_kwargs[
                    "reasoning_content"
                ] = reasoning

        return rtn

    def _convert_chunk_to_generation_chunk(
        self,
        chunk: dict,
        default_chunk_class: Type,
        base_generation_info: Optional[Dict],
    ) -> Optional[ChatGenerationChunk]:
        generation_chunk = super()._convert_chunk_to_generation_chunk(
            chunk,
            default_chunk_class,
            base_generation_info,
        )

        if (choices := chunk.get("choices")) and generation_chunk:
            top = choices[0]
            if isinstance(generation_chunk.message, AIMessageChunk):
                if delta := top.get("delta", {}):
                    if reasoning_content := delta.get("reasoning_content"):
                        generation_chunk.message.additional_kwargs[
                            "reasoning_content"
                        ] = reasoning_content

                    # Handle tool calls
                    if tool_calls := delta.get("tool_calls"):
                        generation_chunk.message.tool_calls = []
                        for tool_call in tool_calls:
                            generation_chunk.message.tool_calls.append(
                                {
                                    "id": tool_call.get("id", ""),
                                    "type": "function",
                                    "name": tool_call.get("function", {}).get(
                                        "name", ""
                                    ),
                                    "args": tool_call.get("function", {}).get(
                                        "arguments", ""
                                    ),
                                }
                            )

        return generation_chunk

    def _stream(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> Iterator[ChatGenerationChunk]:
        from langchain_core.messages import AIMessageChunk

        # Store the original __add__ method
        original_add = AIMessageChunk.__add__

        # Helper function to check if a tool call is valid
        def is_valid_tool_call(tc):
            # Filter out invalid/incomplete tool calls
            if not tc:
                return False

            # Check that we have an ID
            if not tc.get("id"):
                return False

            # Check that we have a name
            if tc.get("name") is None and tc.get("type") == "function":
                return False

            # Check for valid args
            args = tc.get("args")
            if args is None or args == "}" or args == "{}}":
                return False

            return True

        # Create a patched version that ensures tool_calls are preserved
        def patched_add(self, other):
            result = original_add(self, other)

            # Ensure tool_calls are preserved across additions
            if hasattr(self, "tool_calls") and self.tool_calls:
                if not hasattr(result, "tool_calls") or not result.tool_calls:
                    result.tool_calls = [
                        tc for tc in self.tool_calls if is_valid_tool_call(tc)
                    ]

            if hasattr(other, "tool_calls") and other.tool_calls:
                if not hasattr(result, "tool_calls"):
                    result.tool_calls = [
                        tc for tc in other.tool_calls if is_valid_tool_call(tc)
                    ]
                else:
                    # Merge unique tool calls, filtering out invalid ones
                    existing_ids = {tc.get("id", "") for tc in result.tool_calls}
                    for tc in other.tool_calls:
                        if tc.get("id", "") not in existing_ids and is_valid_tool_call(
                            tc
                        ):
                            result.tool_calls.append(tc)

            return result

        # Monkey patch the __add__ method
        AIMessageChunk.__add__ = patched_add

        try:
            # Original streaming
            for chunk in super()._stream(
                messages, stop=stop, run_manager=run_manager, **kwargs
            ):
                yield chunk
        finally:
            # Restore the original method
            AIMessageChunk.__add__ = original_add

    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        try:
            chunks = list(
                self._stream(messages, stop=stop, run_manager=run_manager, **kwargs)
            )
            content = ""
            reasoning_content = ""
            tool_calls = []
            current_tool_calls = {}  # Track tool calls being built

            for chunk in chunks:
                if isinstance(chunk.message.content, str):
                    content += chunk.message.content
                reasoning_content += chunk.message.additional_kwargs.get(
                    "reasoning_content", ""
                )

                if chunk_tool_calls := chunk.message.additional_kwargs.get(
                    "tool_calls", []
                ):
                    for tool_call in chunk_tool_calls:
                        index = tool_call.get("index", "")

                        # Initialize tool call entry if needed
                        if index not in current_tool_calls:
                            current_tool_calls[index] = {
                                "id": "",
                                "name": "",
                                "args": "",
                                "type": "function",
                            }

                        # Update tool call ID
                        if tool_id := tool_call.get("id"):
                            current_tool_calls[index]["id"] = tool_id

                        # Update function name and arguments
                        if function := tool_call.get("function"):
                            if name := function.get("name"):
                                current_tool_calls[index]["name"] = name
                            if args := function.get("arguments"):
                                current_tool_calls[index]["args"] += args

            # Convert accumulated tool calls to final format
            tool_calls = list(current_tool_calls.values())
            for tool_call in tool_calls:
                tool_call["args"] = json.loads(tool_call["args"])

            last_chunk = chunks[-1]

            return ChatResult(
                generations=[
                    ChatGeneration(
                        generation_info=last_chunk.generation_info,
                        message=AIMessage(
                            content=content,
                            additional_kwargs={"reasoning_content": reasoning_content},
                            tool_calls=tool_calls,
                        ),
                    )
                ]
            )

        except JSONDecodeError as e:
            raise JSONDecodeError(
                "Qwen QwQ Thingking API returned an invalid response. "
                "Please check the API status and try again.",
                e.doc,
                e.pos,
            ) from e

    async def _agenerate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        try:
            chunks = [
                chunk
                async for chunk in self._astream(
                    messages, stop=stop, run_manager=run_manager, **kwargs
                )
            ]
            content = ""
            reasoning_content = ""
            tool_calls = []
            current_tool_calls = {}  # Track tool calls being built

            for chunk in chunks:
                if isinstance(chunk.message.content, str):
                    content += chunk.message.content
                reasoning_content += chunk.message.additional_kwargs.get(
                    "reasoning_content", ""
                )

                if chunk_tool_calls := chunk.message.additional_kwargs.get(
                    "tool_calls", []
                ):
                    for tool_call in chunk_tool_calls:
                        index = tool_call.get("index", "")

                        # Initialize tool call entry if needed
                        if index not in current_tool_calls:
                            current_tool_calls[index] = {
                                "id": "",
                                "name": "",
                                "args": "",
                                "type": "function",
                            }

                        # Update tool call ID
                        if tool_id := tool_call.get("id"):
                            current_tool_calls[index]["id"] = tool_id

                        # Update function name and arguments
                        if function := tool_call.get("function"):
                            if name := function.get("name"):
                                current_tool_calls[index]["name"] = name
                            if args := function.get("arguments"):
                                current_tool_calls[index]["args"] += args

            # Convert accumulated tool calls to final format
            tool_calls = list(current_tool_calls.values())
            for tool_call in tool_calls:
                tool_call["args"] = json.loads(tool_call["args"])

            last_chunk = chunks[-1]

            return ChatResult(
                generations=[
                    ChatGeneration(
                        generation_info=last_chunk.generation_info,
                        message=AIMessage(
                            content=content,
                            additional_kwargs={"reasoning_content": reasoning_content},
                            tool_calls=tool_calls,
                        ),
                    )
                ]
            )

        except JSONDecodeError as e:
            raise JSONDecodeError(
                "Qwen QwQ Thingking API returned an invalid response. "
                "Please check the API status and try again.",
                e.doc,
                e.pos,
            ) from e

    async def _astream(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> AsyncIterator[ChatGenerationChunk]:
        from langchain_core.messages import AIMessageChunk

        # Store the original __add__ method
        original_add = AIMessageChunk.__add__

        # Helper function to check if a tool call is valid
        def is_valid_tool_call(tc):
            # Filter out invalid/incomplete tool calls
            if not tc:
                return False

            # Check that we have an ID
            if not tc.get("id"):
                return False

            # Check that we have a name
            if tc.get("name") is None and tc.get("type") == "function":
                return False

            # Check for valid args
            args = tc.get("args")
            if args is None or args == "}" or args == "{}}":
                return False

            return True

        # Create a patched version that ensures tool_calls are preserved
        def patched_add(self, other):
            result = original_add(self, other)

            # Ensure tool_calls are preserved across additions
            if hasattr(self, "tool_calls") and self.tool_calls:
                if not hasattr(result, "tool_calls") or not result.tool_calls:
                    result.tool_calls = [
                        tc for tc in self.tool_calls if is_valid_tool_call(tc)
                    ]

            if hasattr(other, "tool_calls") and other.tool_calls:
                if not hasattr(result, "tool_calls"):
                    result.tool_calls = [
                        tc for tc in other.tool_calls if is_valid_tool_call(tc)
                    ]
                else:
                    # Merge unique tool calls, filtering out invalid ones
                    existing_ids = {tc.get("id", "") for tc in result.tool_calls}
                    for tc in other.tool_calls:
                        if tc.get("id", "") not in existing_ids and is_valid_tool_call(
                            tc
                        ):
                            result.tool_calls.append(tc)

            return result

        # Monkey patch the __add__ method
        AIMessageChunk.__add__ = patched_add

        try:
            # Original async streaming
            async for chunk in super()._astream(
                messages, stop=stop, run_manager=run_manager, **kwargs
            ):
                yield chunk
        finally:
            # Restore the original method
            AIMessageChunk.__add__ = original_add
