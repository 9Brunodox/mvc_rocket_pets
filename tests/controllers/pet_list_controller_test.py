from src.models.sqlite.entities.pets import PetsTable
from  src.controllers.pets_list_controller import PetsListController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(id=4, name="Buddy", type="Dog"),
            PetsTable(id=47, name="Mittens", type="Cat"),
        ]

def test_list_pets():
    mock_repository = MockPetsRepository()
    controller = PetsListController(mock_repository)
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