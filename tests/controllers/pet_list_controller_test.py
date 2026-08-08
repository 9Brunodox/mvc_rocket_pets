from src.models.sqlite.entities.pets import PetsTable
from  src.controllers.pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(id=4, name="Buddy", type="Dog"),
            PetsTable(id=47, name="Mittens", type="Cat"),
        ]

def test_list_pets():
    mock_repository = MockPetsRepository()
    controller = PetListerController(mock_repository)
    response = controller.list()

    expected_response = {
        "data": {
            "type": "pets",
            "count":  2,
            "attributes": [
                {
                    "id": 4,
                    "name": "Buddy",
                    "type": "Dog"
                },
                {
                    "id": 47,
                    "name": "Mittens",
                    "type": "Cat"
                }
            ]
        }
    }

    assert response == expected_response