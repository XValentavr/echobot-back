from fastapi import APIRouter

from app.routes.schemas import ChatResponse, ChatRequest

chat_router = APIRouter(prefix="/chat", tags=["chat"])


@chat_router.post("/", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest) -> ChatResponse:
    return ChatResponse(reply=f"You said: {request.message}")
