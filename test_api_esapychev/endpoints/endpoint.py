import requests
import allure


class Endpoint:
    url = "http://objapi.course.qa-practice.com/object"
    response = None
    post_response = None
    headers = {"Content-Type": "application/json"}

    @allure.step("Compare the data parameters and the created one")
    def check_data(self, data):
        assert self.post_response["data"] == data, "Data из параметров != созданному"

    @allure.step("Compare the name parameters and the created one")
    def check_name(self, data):
        assert self.post_response["name"] == data, "Name из параметров != созданному"

    @allure.step("Check that the post has been deleted")
    def check_is_deleted(self, post_id, headers=None):
        self.response = requests.get(f"{self.url}/{post_id}", headers=headers)
        assert self.response.status_code == 404, "Объект не существует"
