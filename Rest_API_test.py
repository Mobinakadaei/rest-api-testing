from requests import get
from Rest_API_test_variable import *


def get_animal_facts(animal_type=valid_animals[0], amount=random_test_amount):
    params = {}
    if animal_type:
        params['animal_type'] = animal_type
    if amount:
        params['amount'] = amount
    response = get(url=end_point, params=params)
    return response


def test_animal_facts_status_code(animal_type=valid_animals[0], amount=random_test_amount):
    status_code = get_animal_facts(animal_type, amount).status_code
    assert status_code == 200


def test_animal_type_is_none(animal_type=None):
    """
        Test the response when animal_type parameter is not included
    """
    response = get_animal_facts(animal_type=animal_type).json()
    for item in response:
        assert item['type'] == "cat", f"Expected type '{animal_type}', but got '{item['type']}'"


def test_animal_type_is_empty(animal_type=""):
    """
        Test the response when animal_type parameter is set to null
    """
    response = get_animal_facts(animal_type=animal_type).json()
    for item in response:
        assert item['type'] == "cat", f"Expected type '{animal_type}', but got '{item['type']}'"


def test_animal_type_is_not_in_the_list(animal_type="lion"):
    """
        Test the response when animal_type parameter is not set to a valid animal name.
    """
    response = get_animal_facts(animal_type=animal_type).json()
    assert response == []


def test_animal_type_is_in_valid_list():
    """
        Test the response when animal_type parameter is set to valid animals names.
    """
    for animal_type in valid_animals:
        response = get_animal_facts(animal_type=animal_type).json()
        for item in response:
            assert item['type'] == animal_type, f"Expected type '{animal_type}', but got '{item['type']}'"


def test_animal_type_and_amount_field_is_null(animal_type=None, amount=None):
    """
        Test the response when amount parameter and animal_type parameter is set to null
    """
    response = get_animal_facts(animal_type=animal_type, amount=amount).json()
    assert response["type"] == "cat"
    if isinstance(response, dict):
        response = [response]
    assert len(response) == 1


def test_amount_field_is_none(amount=None):
    """
        Test the response when amount parameter is not included
    """
    response = get_animal_facts(amount=amount).json()
    if isinstance(response, dict):
        response = [response]
    assert len(response) == 1


def test_amount_field_is_zero(amount="0"):
    """
        Test the response when amount parameter is set to zero
    """
    response = get_animal_facts(amount=amount).json()
    assert response == []


def test_amount_field_is_empty(amount=""):
    """
        Test the response when amount parameter is set to null
    """
    response = get_animal_facts(amount=amount).json()
    if isinstance(response, dict):
        response = [response]
    assert len(response) == 1


def test_amount_field_has_normal_value(amount="5"):
    """
        Test the response when amount parameter is set to a random normal value
    """
    response = get_animal_facts(amount=amount).json()
    assert str(len(response)) == amount


def test_amount_field_has_max_value(amount=maximum_value):
    """
        Test the response when amount parameter is set to maximum valid value
    """
    response = get_animal_facts(amount=amount).json()
    assert str(len(response)) == amount


def test_amount_field_has_more_than_max_value(amount=bigger_than_maximum_value):
    """
        Test the response when amount parameter is set to a number bigger than valid value
    """
    response = get_animal_facts(amount=amount).json()
    assert response["message"] == "Limited to 500 facts at a time"






