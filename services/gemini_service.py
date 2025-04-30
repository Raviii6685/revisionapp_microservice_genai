from utils.helpers import send_request_to_gemini

async def generate_from_text(prompt: str):
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }
    return send_request_to_gemini(payload)

async def generate_from_images(prompt: str, base64_images: list):
    parts = [{"text": prompt}] + [
        {
            "inline_data": {
                "mime_type": "image/png",
                "data": img
            }
        } for img in base64_images
    ]
    payload = {"contents": [{"parts": parts}]}
    return send_request_to_gemini(payload)