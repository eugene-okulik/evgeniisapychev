import requests
import pytest


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


@pytest.fixture()
def create_obj(base_url):
    body = {
        "data": {
            "Column1": "Для фикстуры",
            "Column2": "Для фикстуры1",
            "Column3": "Для фикстуры3",
        },
        "name": "EvgeniiSapychev",
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{base_url}/object", json=body, headers=headers)
    post_id = response.json()["id"]
    yield post_id
    response = requests.delete(f"{base_url}/object/{post_id}")


@pytest.mark.parametrize(
    "parametr",
    [
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
    ],
)
def test_create_obj(parametr, base_url, every_test, start_srop):
    body = parametr
    headers = {"Content-Type": "application/json"}
    post_response = requests.post(f"{base_url}/object", json=body, headers=headers)
    post_response = post_response.json()
    post_id = post_response["id"]

    assert post_response["data"] == body["data"], "Data из параметров = созданному"
    assert post_response["name"] == body["name"], "Name из параметров = созданному"

    requests.delete(f"{base_url}/object/{post_id}")
    get_response = requests.get(f"{base_url}/object/{post_id}")
    assert get_response.status_code == 404, "Объект не существует"


def test_clear_create_obj(create_obj, base_url, every_test):
    response = requests.delete(f"{base_url}/object/{create_obj}")
    assert response.status_code == 200
    get_response = requests.get(f"{base_url}/object/{create_obj}")
    assert get_response.status_code == 404, "Объект не существует"


@pytest.mark.medium
def test_put_obj(create_obj, base_url, every_test):
    body = {
        "data": {
            "Column1": "Измененное имя с помощью PUT",
            "Column2": False,
            "Column3": 1,
        },
        "name": "Урок 20, измененное имя с помощью PUT",
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f"{base_url}/object/{create_obj}", json=body, headers=headers
    ).json()

    assert response["data"] == {
        "Column1": "Измененное имя с помощью PUT",
        "Column2": False,
        "Column3": 1,
    }, "Проверил data после PUT — все корректно"
    assert (
        response["name"] == "Урок 20, измененное имя с помощью PUT"
    ), "Проверил name после PUT — все корректно"


@pytest.mark.critical
def test_patch_obj(create_obj, base_url, every_test):
    body = {"name": "Изменили только имя с помощью PATCH"}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f"{base_url}/object/{create_obj}", json=body, headers=headers
    ).json()

    assert (
        response["name"] == "Изменили только имя с помощью PATCH"
    ), "Проверил name после PATCH — все корректно"
