from collections.abc import Iterator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from chat_backend import create_app


@pytest.fixture
def app() -> Iterator[FastAPI]:
    app = create_app()
    yield app


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    return TestClient(app)
