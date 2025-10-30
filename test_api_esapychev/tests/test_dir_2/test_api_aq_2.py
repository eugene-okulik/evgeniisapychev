import pytest

DATA = [
    {
        "data": {"Column1": "Имя 1", "Column2": True, "Column3": 3},
        "name": "neEvgeniiSapychev",
    },
    {
        "data": {"Column1": "Имя 2", "Column2": False, "Column3": 3},
        "name": "sovsemNeEvgeniiSapychev",
    },
    {ы
        "data": {"Column1": "Имя 3", "Column2": True, "Column3": 3},
        "name": "EvgeniiSapychev",
    },
]


@pytest.mark.parametrize("data", DATA)
def test_create_obj(created_post_endpoint, data, delete_post_endpoint, start_srop, every_test):
    created_post_endpoint.create_new_post(payload=data)
    created_post_endpoint.check_data(data["data"])
    created_post_endpoint.check_name(data["name"])
    delete_post_endpoint.delete_post(created_post_endpoint.post_id)


@pytest.mark.parametrize("data", DATA)
def test_patch_obj(put_and_patch_endpoint, put_post_endpoint, data, every_test):
    put_post_endpoint.put_post(put_and_patch_endpoint, data)
    put_post_endpoint.check_name(data["name"])
