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
    {
        "data": {"Column1": "Имя 3", "Column2": True, "Column3": 3},
        "name": "EvgeniiSapychev",
    },
]


@pytest.mark.parametrize("data", DATA)
def test_create_obj(created_endpoint, data, delete_endpoint, start_srop, every_test):
    created_endpoint.create_new_obj(payload=data)
    created_endpoint.check_data(data["data"])
    created_endpoint.check_name(data["name"])
    created_endpoint.check_status_code(created_endpoint.post_id)
    delete_endpoint.delete_obj(created_endpoint.post_id)


def test_delete_obj(temporary_post, delete_endpoint, every_test):
    delete_endpoint.delete_obj(temporary_post)
    delete_endpoint.check_is_deleted(temporary_post)
