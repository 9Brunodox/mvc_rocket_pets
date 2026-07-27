from .interfaces.pets_delete_controller import PetsDeleteControllerInterface
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetsDeleteController(PetsDeleteControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository

    def delete(self, name: str) -> None:
        self.__pets_repository.delete_pet(name)