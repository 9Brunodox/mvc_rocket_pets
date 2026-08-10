from typing import List # Para python 3.8 ou inferior
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface

class PeopleRepository(PeopleRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.db_connection = db_connection

    def insert_person(self, first_name:str, last_name: str, age: int, pet_id: int) -> None:
        with self.db_connection as db:
            try:
                person_data = PeopleTable(
                    first_name=first_name,
                    last_name=last_name,
                    age=age,
                    pet_id=pet_id
                )
                db.session.add(person_data)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e

    def list_peoples(self) -> List:
        with self.db_connection as db:
            try:
                peoples = db.session.query(PeopleTable).all()
                return peoples
            except NoResultFound:
                return []

    def delete_person(self, name: str) -> None:
        with self.db_connection as db:
            try:
                person = db.session.query(PeopleTable).filter_by(name=name).first()
                db.session.delete(person)
                db.session.commit()
                return f"person {name} deleted successfully."
            except Exception as e:
                db.session.rollback()
                raise e

    def get_person(self, person_id: int) -> PeopleTable:
        with self.db_connection as db:
            try:
                person = (
                    db.session
                    .query(PeopleTable)
                    .join(PetsTable, PetsTable.id == PeopleTable.pet_id)
                    .filter(PeopleTable.id == person_id)
                    .with_entities(
                        PeopleTable.first_name,
                        PeopleTable.last_name,
                        PeopleTable.age,
                        PeopleTable.pet_id,
                        PetsTable.name.label("pet_name"),
                        PetsTable.type.label("pet_type")
                        )
                    .one()
                )
                return person
            except NoResultFound:
                return None
