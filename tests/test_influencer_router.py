import pytest
from httpx import AsyncClient
from fastapi import status
from config.config_loader import settings
from fastapi.testclient import TestClient
from main import sponsokit_search_ui

client = TestClient(sponsokit_search_ui)

search_text = "messy"
min_follower_count = 0
max_follower_count = 10000
page_no = 3
token = "6wgg9cbSHmWVvGgv_wXPLypenwAKI70cZjGP9y3JEV8"
base_url = "http://test"


def test_influencer_search_route_without_page_number():
    response = client.post(f"{settings.API_V1_STR}/search?search_text={search_text}&min_follower_count={min_follower_count}&max_follower_count={max_follower_count}",
                           headers={"content-type": "application/json"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() != None


def test_influencer_search_route_without_token():
    response = client.post(f"{settings.API_V1_STR}/search/{page_no}?search_text={search_text}&min_follower_count={min_follower_count}&max_follower_count={max_follower_count}",
                           headers={"content-type": "application/json"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() != None


def test_influencer_search_route_without_token_and_parameters():
    response = client.post(f"{settings.API_V1_STR}/search/{page_no}",
                           headers={"content-type": "application/json"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() != None


@pytest.mark.asyncio
async def test_influencer_search_route_with_token_and_parameters():
    async with AsyncClient(app=sponsokit_search_ui, base_url=base_url) as clientX:
        response = await clientX.post(f"{settings.API_V1_STR}/search/{page_no}?token={token}&search_text={search_text}&min_follower_count={min_follower_count}&max_follower_count={max_follower_count}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() != None


def test_influencer_search_route_max_follower_count():

    response = client.post(url=f"{settings.API_V1_STR}/search/{page_no}?token={token}&search_text={search_text}&min_follower_count={min_follower_count}&max_follower_count={max_follower_count}",
                           headers={"content-type": "application/json"})
    pytest.set_trace()
    assert response.status_code == status.HTTP_200_OK
    assert response.json()[1]["follower_count"] <= max_follower_count


def test_influencer_search_route_min_follower_count():

    response = client.post(f"{settings.API_V1_STR}/search/{page_no}?token={token}&search_text={search_text}&min_follower_count={min_follower_count}&max_follower_count={max_follower_count}",
                           headers={"content-type": "application/json"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json()[1]["follower_count"] >= min_follower_count


def test_influencer_search_route_with_token_parameters_and_get():

    response = client.get(f"{settings.API_V1_STR}/search/{page_no}?token={token}&search_text={search_text}&min_follower_count={min_follower_count}&max_follower_count={max_follower_count}",
                          headers={"content-type": "application/json"})
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert response.json() != None


def test_influencer_search_with_json_without_page_number():
    response = client.post(f"{settings.API_V1_STR}/search_with_json/",
                           headers={"content-type": "application/json"},
                           json={"search_text": search_text, "follower_count": {
                               "min_count": min_follower_count,
                               "max_count": max_follower_count},
                               "token": token})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() != None


def test_search_influencer_with_json_without_token():
    response = client.post(f"{settings.API_V1_STR}/search_with_json/{page_no}",
                           headers={"content-type": "application/json"},
                           json={"search_text": search_text, "follower_count": {
                               "min_count": min_follower_count,
                               "max_count": max_follower_count}})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() != None


def test_search_influencer_with_json_without_token_and_parameters():
    response = client.post(f"{settings.API_V1_STR}/search_with_json/{page_no}",
                           headers={"content-type": "application/json"},
                           json={})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() != None


def test_influencer_search_with_json_with_token_and_parameters():
    response = client.post(f"{settings.API_V1_STR}/search_with_json/{page_no}",
                           headers={"content-type": "application/json"},
                           json={"search_text": search_text, "follower_count": {
                               "min_count": min_follower_count,
                               "max_count": max_follower_count},
                               "token": token})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() != None


def test_influencer_search_with_json_with_token_parameters_and_get():

    response = client.get(f"{settings.API_V1_STR}/search_with_json/{page_no}?token={token}&search_text={search_text}&min_follower_count={min_follower_count}&max_follower_count={max_follower_count}",
                          headers={"content-type": "application/json"})
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert response.json() != None
