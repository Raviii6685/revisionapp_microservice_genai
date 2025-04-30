import requests
import json

def send_request_to_gemini(payload):
    api_key = "AIzaSyB_WJfY05zPt-mYKH5lhdlMI7RATUPDJMI"  # Replace with actual key
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()
        output_text = result["candidates"][0]["content"]["parts"][0]["text"]
        return {"status_code": 200, "summary": output_text}
    else:
        return {"status_code": response.status_code, "message": response.text}