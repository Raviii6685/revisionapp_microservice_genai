from fastapi import FastAPI
from routers.quiz_router import router as quiz_router
from routers.summarize_router import router as summarize_router
from routers.chat_router import router as chat_router

app = FastAPI(title="Gemini Assistant:")

app.include_router(quiz_router, prefix="/quiz", tags=["Quiz"])
app.include_router(summarize_router, prefix="/summary", tags=["Summary"])
app.include_router(chat_router, prefix="/chat", tags=["Chat"])