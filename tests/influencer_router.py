from fastapi import status
from config.config_loader import settings
from fastapi.testclient import TestClient
from main import sponsokit_search_ui

client = TestClient(sponsokit_search_ui)

channel_display_name = ""


def test_influencer_search_route_without_token():
    response = client.get(f"{settings.API_V1_STR}/search?channel_display_name={channel_display_name}",
                          headers={"content-type": "application/json"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() != None


def test_influencer_search_route_without_token_and_parameters():
    response = client.get(f"{settings.API_V1_STR}/search",
                          headers={"content-type": "application/json"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() != None


class test_influencer_search:

    def test_auth_token_generation(self):
        response = client.get(f"{settings.API_V1_STR}/generate_auth_token",
                              headers={"content-type": "application/json"})

        if response.status_code == status.HTTP_200_OK:
            return response.json()["token"]

    def test_influencer_search_route_with_token_and_channel_name(self):
        self.token = self.test_auth_token_generation()
        response = client.get(f"{settings.API_V1_STR}/search?channel_display_name={channel_display_name}?",
                              headers={"content-type": "application/json"})
        assert response.status_code == status.HTTP_200_OK
        assert response.json() != None


def test_search_influencer_with_json_without_token():
    response = client.get(f"{settings.API_V1_STR}/search_with_json",
                          headers={"content-type": "application/json"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() != None


def test_search_influencer_with_json_without_token_and_parameters():
    response = client.get(f"{settings.API_V1_STR}/search_with_json",
                          headers={"content-type": "application/json"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() != None


class test_influencer_search_with_json:
    def test_auth_token_generation(self):
        response = client.get(f"{settings.API_V1_STR}/generate_auth_token",
                              headers={"content-type": "application/json"})

        if response.status_code == status.HTTP_200_OK:
            return response.json()["token"]

    def test_influencer_search_with_json_with_token_and_channel_name(self):
        self.token = self.test_auth_token_generation()
        response = client.get(f"{settings.API_V1_STR}/search_with_json",
                              headers={"content-type": "application/json"})
        assert response.status_code == status.HTTP_200_OK
        assert response.json() != None


def test_influencer_search_with_json_with_token_and_channel_name():
    init = test_influencer_search_with_json()
    init.test_auth_token_generation()
    init.test_influencer_search_route_with_token_and_channel_name()
