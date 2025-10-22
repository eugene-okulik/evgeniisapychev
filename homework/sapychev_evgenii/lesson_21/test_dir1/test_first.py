import pytest
import requests
import allure

@allure.feature("start_game")
@allure.story("Posts")
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
    with allure.step("Prepare test data"):
        body = parametr
        headers = {"Content-Type": "application/json"}

    with allure.step("Create post"):
        post_response = requests.post(f"{base_url}/object", json=body, headers=headers)
        post_response = post_response.json()

    with allure.step("Assign id to a variable"):
        post_id = post_response["id"]

    with allure.step("Compare the data parameters and the created one"):
        assert post_response["data"] == body["data"], "Data из параметров != созданному"

    with allure.step("Compare the name parameters and the created one"):
        assert post_response["name"] == body["name"], "Name из параметров != созданному"

    with allure.step("Delete post"):
        requests.delete(f"{base_url}/object/{post_id}")

    with allure.step("Check that the request code is 404"):
        get_response = requests.get(f"{base_url}/object/{post_id}")
        assert get_response.status_code == 404, "Объект не существует"


@allure.feature("end_game")
@allure.story("Delete_post")
def test_clear_create_obj(create_obj, base_url, every_test):
    with allure.step("Delete post"):
        response = requests.delete(f"{base_url}/object/{create_obj}")
        assert response.status_code == 200, "Удаление должно вернуть код 200"

    with allure.step("Check that the request code is 404"):
        get_response = requests.get(f"{base_url}/object/{create_obj}")
        assert get_response.status_code == 404, "Объект не существует"
