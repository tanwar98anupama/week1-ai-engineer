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



code day4_extractor.py
import anthropic
import json
client= anthropic.Anthropic()

sample_text = """Apple reported record quarterly revenue of $119.6 billion, up 8% year over year. 
The company saw strong iPhone sales despite macroeconomic headwinds. 
CEO Tim Cook expressed cautious optimism about the next quarter, 
though supply chain risks remain a concern. Profit margins improved to 43%.
"""

response = client.message.create(
    model= "claude-sonnet-4-6",
    max_tokens= 1024,
    system= """You are Financial Data Extraction Engine.
    -Extract data from text and return ONLY a JSON objects with these exact fields:
    -company : company name
    -revenue : revenue figure as string
    -revenue_growth : growth percentage as number
    -profit margin :margin percentage as number
    -sentiment : one of "positive", "neutral", "negative" based on the overall tone of the text
    -risk level : one of "low", "medium", "high" 
    -key risks : list of risk factors mentioned in the text
    Return only the JSON No explanations, no markdown, no backticks.""",
    messages=[
        {"role": "user", "content": sample_text}
    ]
)

raw= response.content[0].text
data= json.loads(raw)

print("Extracted Data:")
print(json.dumps(data, indent=2))
print(f"\n Company : {data['company']}")
print(f" Sentiment: {data['sentiment']}")
print(f" Risk Level: {data['risk level']}")