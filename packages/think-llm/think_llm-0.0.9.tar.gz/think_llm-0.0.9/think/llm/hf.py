from typing import AsyncGenerator, Any

from .base import BaseAdapter, LLM, ConfigError, BadRequestError
from .chat import Chat, Message, Role, ContentType, ContentPart
from .tool import ToolDefinition


class HuggingFaceAdapter(BaseAdapter):
    """Adapter for converting chat messages to/from HuggingFace format"""

    def get_tool_spec(self, tool: ToolDefinition) -> dict:
        # HuggingFace doesn't have native function calling support
        # You could implement this through prompt engineering
        raise NotImplementedError("Tool calls not supported by HuggingFace")

    def dump_chat(self, chat: Chat) -> tuple[str, list[dict]]:
        """Convert Think chat format to HuggingFace format"""
        messages = []
        system_message = None

        # HuggingFace typically expects a single string with messages
        # concatenated with special tokens
        for msg in chat.messages:
            if msg.role == Role.system:
                system_message = self._get_message_text(msg)
            else:
                messages.append(self._format_message(msg))

        # Format as a single string with special tokens
        formatted = ""
        if system_message:
            formatted += f"<|system|>{system_message}<|endoftext|>"

        for msg in messages:
            formatted += msg

        return formatted, []  # Return formatted string and empty list for compatibility

    def _format_message(self, message: Message) -> str:
        """Format a single message with role tokens"""
        text = self._get_message_text(message)
        if message.role == Role.user:
            return f"<|user|>{text}<|endoftext|>"
        elif message.role == Role.assistant:
            return f"<|assistant|>{text}<|endoftext|>"
        return text

    def _get_message_text(self, message: Message) -> str:
        """Extract text content from message"""
        text = ""
        for part in message.content:
            if part.type == ContentType.text:
                text += part.text
        return text

    def load_chat(self, response: str, system: str = "") -> Chat:
        """Convert HuggingFace response to Think chat format"""
        chat = Chat(system_message=system)
        chat.messages.append(
            Message(
                role=Role.assistant,
                content=[ContentPart(type=ContentType.text, text=response)],
            )
        )
        return chat


class HuggingFaceClient(LLM):
    """Client for making API calls to HuggingFace Inference API"""

    adapter_class = HuggingFaceAdapter

    def __init__(
        self,
        model: str,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        **kwargs,
    ):
        super().__init__(model, api_key=api_key, base_url=base_url, **kwargs)

        # Import here to avoid dependency if not using HuggingFace
        try:
            import huggingface_hub

            self.client = huggingface_hub.InferenceClient(
                model=model,
                token=api_key,
                api_url=base_url or "https://api-inference.huggingface.co/models",
            )
        except ImportError:
            raise ConfigError(
                "huggingface-hub package not installed. "
                "Install with: pip install huggingface-hub"
            )

    async def _internal_call(
        self,
        chat: Chat,
        temperature: float | None,
        max_tokens: int | None,
        adapter: BaseAdapter,
        response_format: Any | None = None,
    ) -> Message:
        """Make API call to HuggingFace"""
        formatted_prompt, _ = adapter.dump_chat(chat)

        try:
            response = await self.client.text_generation(
                formatted_prompt,
                temperature=temperature or 0.7,
                max_new_tokens=max_tokens,
                return_full_text=False,
            )

            return Message(
                role=Role.assistant,
                content=[ContentPart(type=ContentType.text, text=response)],
            )

        except Exception as e:
            raise BadRequestError(f"HuggingFace API error: {str(e)}")

    async def _internal_stream(
        self,
        chat: Chat,
        adapter: BaseAdapter,
        temperature: float | None,
        max_tokens: int | None,
    ) -> AsyncGenerator[str, None]:
        """Stream responses from HuggingFace"""
        formatted_prompt, _ = adapter.dump_chat(chat)

        try:
            async for response in self.client.text_generation(
                formatted_prompt,
                temperature=temperature or 0.7,
                max_new_tokens=max_tokens,
                return_full_text=False,
                stream=True,
            ):
                yield response.token.text

        except Exception as e:
            raise BadRequestError(f"HuggingFace API error: {str(e)}")
