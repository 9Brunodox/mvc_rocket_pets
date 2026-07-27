from src.controllers.person_finder_controller import PersonFinderController

class MockPerson():
    def __init__(self, first_name: str, last_name: str, age: int, pet_id: int, pet_type: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pet_id = pet_id
        self.pet_type = pet_type

class MockPeopleRepository:
    def get_person(self, person_id: int):
        return MockPerson(
            first_name="John",
            last_name="Doe",
            age=30,
            pet_id=12,
            pet_type="Dog"
        )

def test_find():
    controller = PersonFinderController(MockPeopleRepository())
    response = controller.find(123)

    expected_response = {
        "data": {
            "type": "person",
            "count": 1,
            "attributes": {
                "first_name": "John",
                "last_name": "Doe",
                "age": 30,
                "pet_id": 12,
                "pet_type": "Dog"
            }
        }
    }

    assert response == expected_response
