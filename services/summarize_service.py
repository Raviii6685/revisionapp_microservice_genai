from services.gemini_service import generate_from_text, generate_from_images
from utils.prompt_factory import build_summary_prompt
from repositories.file_repo import convert_pdf_to_base64_images

async def summarize_notes(input_type: str, file=None, text=None):
    if input_type == "text":
        prompt = build_summary_prompt(text)
        return await generate_from_text(prompt)

    elif input_type == "image":
        file_path = f"/tmp/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        base64_images = convert_pdf_to_base64_images(file_path)
        prompt = build_summary_prompt("")
        return await generate_from_images(prompt, base64_images)