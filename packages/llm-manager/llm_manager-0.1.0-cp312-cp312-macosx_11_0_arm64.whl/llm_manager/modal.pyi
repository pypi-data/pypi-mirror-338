from enum import StrEnum
import requests
from langchain_community.llms.modal import Modal
from langchain_core.outputs import GenerationChunk
from pydantic import Field
from llm_manager.message import Message, MessageRole
from llm_manager.tools import Tools
from typing import Any, Iterator

class LLMStatus(StrEnum):
    idle = "idle"
    answer = "answer"
    reason = "reason"
    tool = "tool"

class LLModal(Modal):
    section: str = Field(default="llm", alias="section")
    endpoint_url: str = Field(default="", alias="endpoint_url")
    model: str = Field(default="", alias="model")
    system_prompt: str = Field(default="", alias="system_prompt")
    images: list[str] = Field(default_factory=list, alias="images")
    video: list[str] = Field(default_factory=list, alias="video")
    tools: Tools = Field(default_factory=Tools, alias="tools")
    messages: list[Message] = Field(default_factory=list, alias="messages")
    temperature: float | None = Field(default=None, alias="temperature")
    max_tokens: int | None = Field(default=None, alias="max_tokens")
    top_p: float | None = Field(default=None, alias="top_p")
    n: int | None = Field(default=None, alias="n")
    streaming: bool = Field(default=False, alias="stream")
    retry: bool = Field(default=False, alias="retry")
    tool_calls: list[dict[str, Any]] = Field(default_factory=list, alias="tool_calls")
    tool_calls_limit: int = Field(default=3, alias="tool_calls_limit")
    status: LLMStatus = LLMStatus.idle
    _tool_calls_count: int = 0
    _close: bool = False
    _default: str = "The server is busy. Please try again later."
    def _reset(self) -> None: ...
    @property
    def _stream_default(self) -> Iterator[GenerationChunk]: ...
    @property
    def _hyperparameter(self) -> dict[str, Any]: ...
    @property
    def _headers(self) -> dict[str, str]: ...
    @property
    def _body(self) -> dict[str, Any]: ...
    @property
    def messages_latest(self) -> list[dict[str, Any]]: ...
    def message_latest(self, role: MessageRole) -> Message | None: ...
    def add_message(self, role: MessageRole, content: str) -> None: ...
    def _add_tool_calls(self, message: dict[str, Any]) -> None: ...
    def _message_process(self, message: dict[str, Any]) -> dict[str, str]: ...
    def _response(self, response: requests.Response) -> str: ...
    def _stream_response(self, response: requests.Response) -> Iterator[GenerationChunk]: ...
    def _tool_calls(self) -> str | Iterator[GenerationChunk]: ...
    def _core_call(self) -> str | Iterator[GenerationChunk]: ...
    def _call(self, prompt: str, **kwargs: Any) -> str | Iterator[GenerationChunk]: ...
    def _stream(self, prompt: str, **kwargs: Any) -> Iterator[GenerationChunk]: ...
