from typing import List, Dict
from .interfaces.pets_list_controller import PetsListControllerInterface
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetsListController(PetsListControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository

    def list(self) -> Dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response

    def __get_pets_in_db(self) -> List[PetsTable]:
        pets = self.__pets_repository.list_pets()
        return pets

    def __format_response(self, pets: List[PetsTable]) -> Dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({
                "id": pet.id,
                "name": pet.name,
                "type": pet.type,
            })
        return {
            "data": {
                "type": "pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets
            }
        }

