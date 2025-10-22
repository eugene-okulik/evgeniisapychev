import pytest
import requests
import allure


@allure.feature("start_game")
@allure.story("Posts")
@pytest.mark.medium
def test_put_obj(create_obj, base_url, every_test):
    with allure.step("Prepare PUT request data"):
        body = {
            "data": {
                "Column1": "Измененное имя с помощью PUT",
                "Column2": False,
                "Column3": 1,
            },
            "name": "Урок 20, измененное имя с помощью PUT",
        }
        headers = {"Content-Type": "application/json"}

    with allure.step("Send PUT request"):
        response = requests.put(
            f"{base_url}/object/{create_obj}", json=body, headers=headers
        ).json()

    with allure.step("Verify updated data fields"):
        assert response["data"] == {
            "Column1": "Измененное имя с помощью PUT",
            "Column2": False,
            "Column3": 1,
        }, "Проверил data после PUT — все корректно"

    with allure.step("Verify updated name field"):
        assert (
            response["name"] == "Урок 20, измененное имя с помощью PUT"
        ), "Проверил name после PUT — все корректно"


@allure.feature("end_game")
@allure.story("Create_post")
@pytest.mark.critical
def test_patch_obj(create_obj, base_url, every_test):
    with allure.step("Prepare PATCH data"):
        body = {"name": "Изменили только имя с помощью PATCH"}
        headers = {"Content-Type": "application/json"}

    with allure.step("Send PATCH request"):
        response = requests.patch(
            f"{base_url}/object/{create_obj}", json=body, headers=headers
        ).json()

    with allure.step("Verify updated name after PATCH"):
        assert (
            response["name"] == "Изменили только имя с помощью PATC"
        ), "Проверил name после PATCH — все корректно"
