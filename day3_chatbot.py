import anthropic

client = anthropic.Anthropic()

system_prompt = "You are a senior FinTech analyst with 15 years of experience."

conversation_history = []

print("FinTech Analyst Chatbot - type quit to exit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        if conversation_history:
            summary_response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=256,
                system="You are a helpful assistant.",
                messages=conversation_history + [
                    {"role": "user", "content": "Summarise the key financial concepts we discussed in 3 bullet points."}
                ]
            )
            print("\nSession summary:")
            print(summary_response.content[0].text)
        print("Goodbye!")
        break

    conversation_history.append({"role": "user", "content": user_input})

    if len(conversation_history) > 10:
        conversation_history = conversation_history[-10:]

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=system_prompt,
        messages=conversation_history
    )

    assistant_message = response.content[0].text

    conversation_history.append({"role": "assistant", "content": assistant_message})

    print(f"\nAnalyst: {assistant_message}\n")