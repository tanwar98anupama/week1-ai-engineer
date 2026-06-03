import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system="You are a senior fintech analyst. When asked about any financial metric, always structure your answer as: 1) One line definition 2) Why it matters 3) A real company example 4) One limitation.",
    messages=[
        {"role": "user", "content": "Explain EBITDA"},
	{"role": "assistant", "content": "EBITDA is earnings before interest, taxes, depreciation and amortisation- a measure of core operating profit. 2)It matters because it stripes out financing and accounting decisions, making companies easier to compare. 3) Amazon reports EBITDA to show operational performance separately from its heavy capital investments. 4) Limitation: it ignores capital expenditure, so capital-heavy businesses can look more profitable than they are."},
        {"role": "user", "content": "A company has a P/E of 45 and the industry average is 20. Think step by step — is this stock overvalued?"}
    ]
)

print(message.content[0].text)
