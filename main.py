from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routes import routes
app = FastAPI(title="Chat API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

for route in routes:
    app.include_router(route)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)