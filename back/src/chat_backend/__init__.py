from importlib.metadata import version

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from fastapi import FastAPI
from .models import MessageRequest


def create_app() -> FastAPI:
    app = FastAPI(title="chat-backend", version=version("chat_backend"))

    origins = ["http://localhost:5173"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/healthcheck")
    async def healthcheck():
        return {"status": "success"}

    @app.post("/")
    async def chat(request: MessageRequest) -> JSONResponse:
        return JSONResponse({"message": "Agent response"})

    return app


if __name__ == "__main__":
    uvicorn.run(create_app())
