import requests
import allure

from endpoints.endpoint import Endpoint


@allure.step("Create new post")
class CreateObj(Endpoint):
    def create_new_obj(self, payload, headers=None):
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.post_response = self.response.json()
        self.post_id = self.post_response['id']
