import anthropic
import os
from dotenv import load_dotenv
from memory import ConversationMemory

load_dotenv()

SYSTEM_PROMPT = """You are a strict but helpful CS tutor.
You teach Python and LLM engineering concepts.
Rules you follow:
- Always explain concepts before showing code
- Use simple analogies and real world examples
- When student makes an error, guide them to find the fix themselves
- Keep responses concise and clear
- If asked something outside CS/programming, redirect back to topic"""

class StudyBuddy:
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        self.memory = ConversationMemory(max_messages=20)

    def chat(self, user_message):
        self.memory.add_message("user", user_message)

        response = self.client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1000,
            system=SYSTEM_PROMPT,
            messages=self.memory.get_messages()
        )

        assistant_message = response.content[0].text
        self.memory.add_message("assistant", assistant_message)

        return assistant_message