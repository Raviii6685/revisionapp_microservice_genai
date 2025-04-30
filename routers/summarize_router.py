from fastapi import APIRouter, UploadFile, File, Form
from services.summarize_service import summarize_notes

router = APIRouter()

@router.post("/summarize")
async def summarize_handler(
        input_type: str = Form(...),       # 'text' or 'image'
        text: str = Form(None),
        file: UploadFile = File(None)
):
    return await summarize_notes(input_type=input_type, file=file, text=text)