import pytest
import requests


@pytest.fixture()
def base_url():
    return "http://objapi.course.qa-practice.com"


@pytest.fixture(scope="session")
def start_srop():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(scope="function")
def every_test():
    print("before test")
    yield
    print("after test")


@pytest.fixture(
    params=[
        {
            "data": {"Column1": "Имя 1", "Column2": True, "Column3": 3},
            "name": "neEvgeniiSapychev",
        },
        {
            "data": {"Column1": "Имя 2", "Column2": False, "Column3": 3},
            "name": "sovsemNeEvgeniiSapychev",
        },
        {
            "data": {"Column1": "Имя 3", "Column2": True, "Column3": 3},
            "name": "EvgeniiSapychev",
        },
    ]
)
def create_obj(request, base_url):
    body = request.param
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{base_url}/object", json=body, headers=headers)
    post_id = response.json()["id"]
    yield post_id
    requests.delete(f"{base_url}/object/{post_id}")
