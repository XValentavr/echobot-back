from fastapi import APIRouter
from starlette.status import HTTP_200_OK

from app.routes.schemas import BaseResponse

dev_router = APIRouter(prefix="/dev", tags=["dev"])


@dev_router.get("/health", response_model=BaseResponse)
def health_check() -> BaseResponse:
    return BaseResponse(status=HTTP_200_OK, message="OK")

@dev_router.get("/", response_model=BaseResponse)
def root() -> BaseResponse:
    return BaseResponse(status=HTTP_200_OK, message="Welcome to the API!")
