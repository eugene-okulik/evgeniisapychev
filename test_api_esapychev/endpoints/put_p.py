import requests
import allure

from endpoints.endpoint import Endpoint


@allure.step("Put post")
class PutObj(Endpoint):
    def put_obj(self, post_id, payload, headers=None):
        self.response = requests.put(
            f"{self.url}/{post_id}",
            json=payload,
            headers=headers
        )
        self.post_response = self.response.json()
        return self.response
