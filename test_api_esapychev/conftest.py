import pytest
import allure

from endpoints.create_p import CreatePosts
from endpoints.delete_p import DeletePosts
from endpoints.patch_p import PatchPost
from endpoints.put_p import PutPost


@pytest.fixture()
def created_post_endpoint():
    return CreatePosts()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePosts()


@pytest.fixture()
def patch_post_endpoint():
    return PatchPost()


@pytest.fixture()
def put_post_endpoint():
    return PutPost()


@pytest.fixture()
def put_and_patch_endpoint(created_post_endpoint, delete_post_endpoint):
    payload = {
        "data": {
            "Column1": "Удалим с помощью DELETE и изменим с помощью PATCH и PUT",
            "Column2": False,
            "Column3": 1,
        },
        "name": "Урок 22, УУдалим с помощью DELETE и изменим с помощью PATCH и PUT",
    }
    created_post_endpoint.create_new_post(payload)
    post_id = created_post_endpoint.post_id
    yield post_id
    delete_post_endpoint.delete_post(post_id)


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
