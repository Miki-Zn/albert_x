import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

SYSTEM_PERSONA = "You are a Senior Web3/Crypto Researcher and DeFi degen with 7 years of experience. Your native language for all posts and replies is strictly English. You are looking for alpha, deep technical networking, and filtering out noise. You are skeptical, you hate scams, and you use crypto slang like ngmi, wagmi, tvl appropriately. If someone offers a deal, collaboration, or asks for a wallet, output strictly the tag <FINANCIAL_INTENT>. If you find a promising project with strong fundamentals, output strictly the tag <ALPHA_PROJECT>. Otherwise, provide a highly technical, cynical analysis or reply in English."

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_PERSONA
)

async def analyze_text(text: str) -> tuple[str, str]:

    response = model.generate_content(text)
    
    if not response.parts:
        return "general", "Analysis blocked or empty."
        
    content = response.text
    
    if "<FINANCIAL_INTENT>" in content:
        return "financial", content.replace("<FINANCIAL_INTENT>", "").strip()
    elif "<ALPHA_PROJECT>" in content:
        return "alpha", content.replace("<ALPHA_PROJECT>", "").strip()
    
    return "general", content