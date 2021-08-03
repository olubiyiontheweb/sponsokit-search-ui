from fastapi import status
from config.config_loader import settings
from fastapi.testclient import TestClient
from main import sponsokit_search_ui

client = TestClient(sponsokit_search_ui)


def test_influencer_search_route():
    response = client.get("/", headers={"content-type": "application/json"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json(
    ) == f"{settings.DESCRIPTION} Visit /api/v1/docs for more details."


def test_search_influencer_with_json():
    response = client.get("/", headers={"content-type": "application/json"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json(
    ) == f"{settings.DESCRIPTION} Visit /api/v1/docs for more details."
