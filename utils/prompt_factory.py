def build_quiz_prompt(text: str, quiz_type: str = "combo"):
    return f"""
You are a quiz generator. Create a comprehensive quiz from the following notes. Use the exact format mentioned.

Text:
{text}

🎯 Output format (JSON only):
{{
  "quiz": {{
    "mcq": [
      {{
        "question": "",
        "answer": ""
      }}
    ],
    "short_answer": [
      {{
        "question": "",
        "answer": ""
      }}
    ],
    "fill_in_the_blanks": [
      {{
        "question": "",
        "answer": ""
      }}
    ],
    "true_false": [
      {{
        "question": "",
        "answer": ""
      }}
    ]
  }}
}}

✨ Generate exactly:
- 10 MCQs (with options and correct answer)
- 5 Short answer questions
- 10 Fill in the blanks
- 5 True/False

Return ONLY valid JSON response.
"""

def build_summary_prompt(text: str):
    return f"""
    Summarize the following content in bullet points for active recall and quick revision:

    {text}

    Format:
    - Point 1
    - Point 2
    - ...
    """