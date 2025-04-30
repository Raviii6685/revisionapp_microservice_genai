from fastapi import APIRouter, UploadFile, File, Form
from services.quiz_service import create_quiz

router = APIRouter()

@router.post("/generate")
async def generate_quiz(
        input_type: str = Form(...),       # 'text' or 'image'
        quiz_type: str = Form("mcq"),      # 'mcq' or 'qa'
        text: str = Form(None),
        file: UploadFile = File(None)
):
    return await create_quiz(input_type=input_type, file=file, text=text, quiz_type=quiz_type)