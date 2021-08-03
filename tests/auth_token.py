from typing import Any
from fastapi import status
from config.config_loader import settings
from fastapi.testclient import TestClient
from main import sponsokit_search_ui

client = TestClient(sponsokit_search_ui)


def test_read_main():
    response = client.get(f"{settings.API_V1_STR}/generate_auth_token",
                          headers={"content-type": "application/json"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() != None
