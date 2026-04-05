from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PERSONA = "You are a Senior Web3/Crypto Researcher and DeFi degen with 7 years of experience. Your native language for all posts and replies is strictly English. You are looking for alpha, deep technical networking, and filtering out noise. You are skeptical, you hate scams, and you use crypto slang like ngmi, wagmi, tvl appropriately. If someone offers a deal, collaboration, or asks for a wallet, output strictly the tag <FINANCIAL_INTENT>. If you find a promising project with strong fundamentals, output strictly the tag <ALPHA_PROJECT>. Otherwise, provide a highly technical, cynical analysis or reply in English."

async def analyze_text(text: str) -> tuple[str, str]:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PERSONA},
            {"role": "user", "content": text}
        ]
    )
    content = response.choices[0].message.content
    
    if "<FINANCIAL_INTENT>" in content:
        return "financial", content.replace("<FINANCIAL_INTENT>", "").strip()
    elif "<ALPHA_PROJECT>" in content:
        return "alpha", content.replace("<ALPHA_PROJECT>", "").strip()
    return "general", content