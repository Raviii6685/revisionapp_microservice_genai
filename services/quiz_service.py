from services.gemini_service import generate_from_text, generate_from_images
from utils.prompt_factory import build_quiz_prompt
from repositories.file_repo import convert_pdf_to_base64_images
import json

async def create_quiz(input_type: str, file=None, text=None, quiz_type="mcq"):
    if input_type == "text":
        prompt = build_quiz_prompt(text, quiz_type)
        result = await generate_from_text(prompt)

    elif input_type == "image":
        file_path = f"/tmp/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        base64_images = convert_pdf_to_base64_images(file_path)
        prompt = build_quiz_prompt("", quiz_type)
        result = await generate_from_images(prompt, base64_images)

    try:
        raw_text = result.get("summary", "")
        clean_text = raw_text.replace("```json", "").replace("```", "").strip()

    # Load as JSON
        quiz_json = json.loads(clean_text)

    # Return just the quiz part (or full if needed)
        return quiz_json.get("quiz", quiz_json)
    except Exception as e:
        return {
    "error": f"Failed to parse response: {str(e)}",
    "raw_output": result
                }