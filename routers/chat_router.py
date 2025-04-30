from fastapi import APIRouter, Form
from services.chat_service import chat_with_gemini

router = APIRouter()

@router.post("/ask")
async def ask_gemini(prompt: str = Form(...)):
    return await chat_with_gemini(prompt)