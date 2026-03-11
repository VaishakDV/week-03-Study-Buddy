# Week 03 - Study Buddy CLI

A command-line AI tutor powered by Claude API that remembers 
your conversation and teaches Python and LLM engineering concepts.

## What it does
- Has a real conversation with Claude via the Anthropic API
- Remembers the last 20 messages using a sliding window memory system
- Custom system prompt makes Claude behave as a strict CS tutor
- Type 'clear' to reset the conversation
- Type 'quit' to exit

## What I learned
- How to use the Anthropic Python SDK
- What tokens are and how context windows work
- System prompts vs user messages vs assistant turns
- How LLMs have no memory — and how to build memory yourself
- Sliding window memory pattern
- How every chatbot in the world works under the hood

## How to run
1. Clone the repo
2. Create a virtual environment and activate it
3. pip install anthropic python-dotenv
4. Create a .env file with your Anthropic API key
5. python main.py

## Tech used
- Python 3.11
- Anthropic SDK
- python-dotenv
