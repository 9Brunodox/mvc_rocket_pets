from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface

class PersonCreatorController:
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def create(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self.__people_repository.insert_person(first_name, last_name, age, pet_id)
