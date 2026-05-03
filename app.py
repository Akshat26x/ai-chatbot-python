print("Simple AI Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Goodbye!")
        break

    elif "ai" in user_input:
        print("Bot: AI stands for Artificial Intelligence.")

    elif "cloud" in user_input:
        print("Bot: Cloud computing means storing and accessing data over the internet.")

    elif "hello" in user_input:
        print("Bot: Hello! How can I help you?")

    elif "devops" in user_input:
        print("Bot: DevOps combines development and operations to improve software delivery.")

    else:
        print("Bot: I'm still learning, but I understand basic queries!")