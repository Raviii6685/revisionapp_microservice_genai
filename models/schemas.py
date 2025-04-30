from pydantic import BaseModel

# Define request and response models using Pydantic
class TextRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    summary: str