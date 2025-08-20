import requests 


def create_obj():
    body = {
        "data": {'!json_111': '!one_1', '!json_211': '!two_2', '!json_311': 3},
        "name": "Lesson_19_hello"
        }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers).json()
    assert response['data'] == {'!json_111': '!one_1', '!json_211': '!two_2', '!json_311': 3} , 'Data incorrect'
    assert response['name'] == "Lesson_19_hello", 'Name incorrect'
    return response['id']
    

def clear_create_obj(create_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{create_id}')
    print('Объект удален')


def put_obj():
    create_id = create_obj()
    body = {
        "data": {'json_111': 'one_1', 'json_211': 'two_2', 'json_311': 3},
        "name": "Lesson_19_bye"
        }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{create_id}', json=body, headers=headers).json()
    assert response['data'] == {'json_111': 'one_1', 'json_211': 'two_2', 'json_311': 3}
    assert response['name'] == "Lesson_19_bye", 'Name incorrect'
    clear_create_obj(create_id)


def patch_obj():
    create_id = create_obj()
    body = {
        "data": {'patch_1': 'p1', 'patch=2': 'p2', 'patch_3': 3},
        'name': 'Lesson_19_path'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{create_id}', json=body, headers=headers).json()
    clear_create_obj(create_id)
