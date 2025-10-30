import pytest

DATA = [
    {
        "data": {"Column1": "Изменил с помощью PUT", "Column2": True, "Column3": 2},
        "name": "Изменил с помощью PUT",
    }
]

PATCH_DATA = [
    {"name": "Изменил с помощью PATCH"}
]


@pytest.mark.parametrize("data", DATA)
def test_put_obj(created_and_deleted_post, put_post_endpoint, data):
    put_post_endpoint.put_post(created_and_deleted_post, data)
    put_post_endpoint.check_name(data["name"])
    put_post_endpoint.check_data(data["data"])


@pytest.mark.parametrize("data", PATCH_DATA)
def test_patch_obj(created_and_deleted_post, patch_post_endpoint, data):
    patch_post_endpoint.patch_post(created_and_deleted_post, data)
    patch_post_endpoint.check_name(data["name"])
