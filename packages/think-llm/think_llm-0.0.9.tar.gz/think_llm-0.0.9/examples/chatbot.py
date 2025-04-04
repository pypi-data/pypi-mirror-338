#!/usr/bin/env python3
import sys
import os
import click
from typing import Optional

from dotenv import load_dotenv

# Add parent directory to path for easy local development
sys.path.append(".")

from think import LLM, Chat  # noqa E402

load_dotenv()


@click.command()
@click.option(
    "--model-url",
    "-m",
    default=None,
    help="LLM URL (e.g., 'openai:///gpt-4o-mini'). Defaults to LLM_URL env variable.",
)
@click.option(
    "--system",
    "-s",
    default="You are a helpful assistant. Be concise and friendly in your responses.",
    help="System prompt to initialize the chat.",
)
def main(model_url: Optional[str], system: str):
    """
    Interactive chatbot using the Think library.

    Start a conversation with an LLM in your terminal. Type your messages
    and receive AI responses. Use Ctrl+C or type 'exit' to end the conversation.
    """
    # Get model URL from argument or environment
    model_url = model_url or os.environ.get("LLM_URL")
    if not model_url:
        print(
            "Error: Model URL not provided. Use --model-url option or set LLM_URL environment variable."
        )
        sys.exit(1)

    try:
        # Initialize LLM from URL
        llm = LLM.from_url(model_url)
        print(f"Connected to {model_url}")
        print("Type your messages (type 'exit' to quit)")
        print("-" * 50)

        # Initialize chat with system prompt
        chat = Chat(system)

        # Main conversation loop
        while True:
            # Get user input
            user_input = input("\nYou: ").strip()

            # Check for exit command
            if user_input.lower() in ("exit", "quit", "bye"):
                print("\nGoodbye!")
                break

            if not user_input:
                continue

            # Add user message to chat and get response
            chat.user(user_input)

            # Make async call synchronous for simplicity in this example
            import asyncio

            response = asyncio.run(llm(chat))

            # Print response
            print(f"\nAI: {response}")

    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
