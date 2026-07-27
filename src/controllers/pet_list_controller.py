from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetListController():
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository

    def list(self):
        return self.__pets_repository.list_pets()
