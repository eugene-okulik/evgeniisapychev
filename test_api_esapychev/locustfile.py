from locust import task, HttpUser
from endpoints.endpoint import Endpoint
import random


class LocustTest(HttpUser):
    base_url = "/object"

    @task(1)
    def on_start(self):
        payload = {
            "data": {
                "Column1": "Имя 1",
                "Column2": True,
                "Column3": 3
            },
            "name": "neEvgeniiSapychev",
        }
        self_response = self.client.post(
            self.base_url,
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        self.obj_id = self_response.json()["id"]

    @task(3)
    def update_object_put(self):
        payload = {
            "data": {
                "Column1": "Имя 1",
                "Column2": True,
                "Column3": 3
            },
            "name": "neEvgeniiSapychev",
        }
        self.client.put(
            f"{self.base_url}/{self.obj_id}",
            json=payload,
            headers=Endpoint.headers
        )

    @task(1)
    def update_object_patch(self):
        payload = {"name": f"Patch_{random.randint(1, 100)}"}
        self.client.patch(
            f"{self.base_url}/{self.obj_id}",
            json=payload,
            headers=Endpoint.headers
        )

    @task(1)
    def delete_object(self):
        self.client.delete(
            f"{self.base_url}/{self.obj_id}",
            headers={"Content-Type": "application/json"}
        )
