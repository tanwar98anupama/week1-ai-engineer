import anthropic
import json

client = anthropic.Anthropic()

def extract_financial_data(text, retries=3):
    for attempt in range(retries):
        try:
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1024,
                system="""You are a financial data extraction engine.
Extract data from text and return ONLY a JSON object with these exact fields:
- company: company name
- revenue: revenue figure as string
- revenue_growth: growth percentage as number
- profit_margin: margin percentage as number
- sentiment: one of 'positive', 'neutral', 'negative'
- risk_level: one of 'low', 'medium', 'high'
- key_risks: list of risk factors mentioned

Return ONLY the JSON. No explanation, no markdown, no backticks.""",
                messages=[
                    {"role": "user", "content": text}
                ]
            )
            raw = response.content[0].text
            data = json.loads(raw)
            return data
        except json.JSONDecodeError:
            print(f"Attempt {attempt + 1} failed, retrying...")
    return None

companies = [
    """Apple reported record quarterly revenue of $119.6 billion, up 8% year over year.
    Strong iPhone sales despite macroeconomic headwinds.
    CEO Tim Cook expressed cautious optimism. Profit margins improved to 43%.""",

    """Goldman Sachs reported net revenue of $12.7 billion, down 1% from last year.
    Investment banking fees dropped significantly amid market uncertainty.
    The firm flagged increased credit risk exposure in emerging markets.""",

    """SVB Financial reported rising deposit outflows and significant losses
    on its bond portfolio. Management warned of liquidity pressures
    and a challenging rate environment ahead."""
]

print("--- Batch Financial Risk Dashboard ---\n")
for i, text in enumerate(companies):
    result = extract_financial_data(text)
    if result:
        print(f"Company: {result['company']}")
        print(f"Revenue: {result['revenue']} | Growth: {result['revenue_growth']}%")
        print(f"Sentiment: {result['sentiment']} | Risk: {result['risk_level']}")
        print(f"Key risks: {', '.join(result['key_risks'])}")
        print("-" * 50)