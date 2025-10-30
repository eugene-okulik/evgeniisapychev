import requests
import allure

from endpoints.endpoint import Endpoint


@allure.step("Delete post")
class DeletePosts(Endpoint):
    def delete_post(self, post_id, headers=None):
        self.response = requests.delete(
            f"{self.url}/{post_id}",
            headers=headers
        )
