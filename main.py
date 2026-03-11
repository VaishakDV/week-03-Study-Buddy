from chatbot import StudyBuddy

def main():
    print("\n"+"="*50)
    print("     STUDY BUDDY - Your CS Tutor")
    print("="*50)
    print("Commands: 'quit' to exit, 'clear' to reset chat")
    print("="*50 + "\n")

    buddy = StudyBuddy()

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("\nGoodbye! Kepp coding. 🔥")
            break

        if user_input.lower() == "clear":
            buddy.memory.clear()
            continue

        response = buddy.chat(user_input)
        print(f"\nBuddy: {response}\n")

if __name__ == "__main__":
    main()