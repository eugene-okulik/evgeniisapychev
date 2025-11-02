import pytest

from endpoints.create_p import CreateObj
from endpoints.delete_p import DeleteObj
from endpoints.patch_p import PatchObj
from endpoints.put_p import PutObj


@pytest.fixture()
def created_endpoint():
    return CreateObj()


@pytest.fixture()
def delete_endpoint():
    return DeleteObj()


@pytest.fixture()
def patch_endpoint():
    return PatchObj()


@pytest.fixture()
def put_endpoint():
    return PutObj()


@pytest.fixture()
def temporary_post(created_endpoint, delete_endpoint):
    payload = {
        "data": {
            "Column1": "Удалим с помощью DELETE и изменим с помощью PATCH и PUT",
            "Column2": False,
            "Column3": 1,
        },
        "name": "Урок 22, УУдалим с помощью DELETE и изменим с помощью PATCH и PUT",
    }
    created_endpoint.create_new_obj(payload)
    post_id = created_endpoint.post_id
    yield post_id
    delete_endpoint.delete_obj(post_id)


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
