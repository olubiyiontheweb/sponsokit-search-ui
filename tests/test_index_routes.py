from fastapi import status
from config.config_loader import settings
from fastapi.testclient import TestClient
from main import sponsokit_search_ui

client = TestClient(sponsokit_search_ui)


def test_index_route():
    """
    Test the index route. 
    """
    response = client.get("/", headers={"content-type": "application/json"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json(
    ) == f"{settings.DESCRIPTION} Visit /api/v1/docs for more details."


def test_unknown_routes():
    """ 
    Test routes that are not defined in the router.
    """
    response = client.get("/unknown_endpoint",
                          headers={"content-type": "application/json"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Not Found"}
