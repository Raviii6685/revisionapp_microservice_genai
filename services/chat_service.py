from services.gemini_service import generate_from_text

async def chat_with_gemini(prompt: str):
    return await generate_from_text(prompt)