import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.repositories.people_repository import PeopleRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="This test is skipped because it requires a database connection.")
def test_list_pets():
    pets_repository = PetsRepository(db_connection_handler)
    response_pets_list = pets_repository.list_pets()
    print(response_pets_list)
    assert response_pets_list is not None

@pytest.mark.skip(reason="This test is skipped because it requires a database connection.")
def test_delete_pet():
    pets_repository = PetsRepository(db_connection_handler)
    name = "goldfish"
    response_delete_pet = pets_repository.delete_pet(name)
    assert response_delete_pet == f"Pet {name} deleted successfully."

@pytest.mark.skip(reason="This test is skipped because it requires a database connection.")
def test_insert_person():
    person_data = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 1
    }
    people_repository = PeopleRepository(db_connection_handler)
    people_repository.insert_person(**person_data)

def test_get_person():
    person_id = 1

    people_repository = PeopleRepository(db_connection_handler)
    response = people_repository.get_person(person_id)
    assert response is not None
    print(response)
