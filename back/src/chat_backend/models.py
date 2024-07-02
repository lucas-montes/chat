from __future__ import annotations

from enum import Enum
import itertools
from fastapi import HTTPException
from pydantic import BaseModel, field_validator


class Authors(Enum):
    Client = "Client"
    Agent = "Agent"


class Message(BaseModel):
    message: str
    author: Authors


class MessageRequest(BaseModel):
    message: str
    history: list[Message]

    @field_validator("history", mode="after")
    @classmethod
    def validate_history(cls, history: list[Message]) -> list[Message]:
        if len(history) == 1:
            message = next(iter(history))
            if message.author != Authors.Client:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid chat history",
                )
        elif any(f.author == s.author for (f, s) in itertools.pairwise(history)):
            raise HTTPException(
                status_code=400,
                detail="Invalid chat history",
            )
        return history
