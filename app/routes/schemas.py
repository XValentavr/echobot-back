from sqlmodel import SQLModel


class ChatRequest(SQLModel, table=False):
    message: str


class ChatResponse(SQLModel, table=False):
    reply: str


class BaseResponse(ChatRequest):
    status: int
