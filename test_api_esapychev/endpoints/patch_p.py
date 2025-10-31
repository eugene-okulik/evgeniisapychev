import requests
import allure

from endpoints.endpoint import Endpoint


@allure.step("Patch post")
class PatchPost(Endpoint):
    def patch_post(self, post_id, payload, headers=None):
        self.response = requests.patch(
            f"{self.url}/{post_id}",
            json=payload,
            headers=headers
        )
        self.post_response = self.response.json()
        return self.response
