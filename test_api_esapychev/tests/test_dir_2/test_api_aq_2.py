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
def test_put_obj(temporary_post, put_endpoint, data):
    put_endpoint.put_obj(temporary_post, data)
    put_endpoint.check_name(data["name"])
    put_endpoint.check_data(data["data"])
    put_endpoint.check_status_code(temporary_post)


@pytest.mark.parametrize("data", PATCH_DATA)
def test_patch_obj(temporary_post, patch_endpoint, data):
    patch_endpoint.patch_obj(temporary_post, data)
    patch_endpoint.check_name(data["name"])
    patch_endpoint.check_status_code(temporary_post)
