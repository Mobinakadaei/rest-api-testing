from requests import get


def get_animal_facts(animal_type="cat", amount="2"):
    end_point = "https://cat-fact.herokuapp.com/facts/random"
    params = {}
    if animal_type:
        params['animal_type'] = animal_type
    if amount:
        params['amount'] = amount
    response = get(url=end_point, params=params)
    return response


def test_animal_facts_status_code(animal_type="cat", amount="2"):
    status_code = get_animal_facts(animal_type, amount).status_code
    assert status_code == 200


def test_animal_type_is_none(animal_type=None):
    response = get_animal_facts(animal_type=animal_type).json()
    for item in response:
        assert item['type'] == "cat", f"Expected type '{animal_type}', but got '{item['type']}'"


def test_animal_type_is_empty(animal_type=""):
    response = get_animal_facts(animal_type=animal_type).json()
    for item in response:
        assert item['type'] == "cat", f"Expected type '{animal_type}', but got '{item['type']}'"


def test_animal_type_is_not_in_the_list(animal_type="lion"):
    response = get_animal_facts(animal_type=animal_type).json()
    assert response == []


def test_animal_type_is_cat(animal_type="cat"):
    response = get_animal_facts(animal_type=animal_type).json()
    for item in response:
        assert item['type'] == animal_type, f"Expected type '{animal_type}', but got '{item['type']}'"


def test_animal_type_is_dog(animal_type="dog"):
    response = get_animal_facts(animal_type=animal_type).json()
    for item in response:
        assert item['type'] == animal_type, f"Expected type '{animal_type}', but got '{item['type']}'"


def test_animal_type_is_snail(animal_type="snail"):
    response = get_animal_facts(animal_type=animal_type).json()
    for item in response:
        assert item['type'] == animal_type, f"Expected type '{animal_type}', but got '{item['type']}'"


def test_animal_type_is_horse(animal_type="snail"):
    response = get_animal_facts(animal_type=animal_type).json()
    for item in response:
        assert item['type'] == animal_type, f"Expected type '{animal_type}', but got '{item['type']}'"


def test_animal_type_and_amount_field_is_null(animal_type=None, amount=None):
    response = get_animal_facts(animal_type=animal_type, amount=amount).json()
    assert response["type"] == "cat"
    if isinstance(response, dict):
        response = [response]
    assert len(response) == 1


def test_amount_field_is_none(amount=None):
    response = get_animal_facts(amount=amount).json()
    if isinstance(response, dict):
        response = [response]
    assert len(response) == 1


def test_amount_field_is_zero(amount="0"):
    response = get_animal_facts(amount=amount).json()
    assert response == []


def test_amount_field_is_empty(amount=""):
    response = get_animal_facts(amount=amount).json()
    if isinstance(response, dict):
        response = [response]
    assert len(response) == 1


def test_amount_field_has_normal_value(amount="5"):
    response = get_animal_facts(amount=amount).json()
    assert str(len(response)) == amount


def test_amount_field_has_max_value(amount="500"):
    response = get_animal_facts(amount=amount).json()
    assert str(len(response)) == amount


def test_amount_field_has_more_than_max_value(amount="504"):
    response = get_animal_facts(amount=amount).json()
    assert response["message"] == "Limited to 500 facts at a time"






