import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is a P/E ratio and why does it matter?"}
    ]
)

print(message.content[0].text)

