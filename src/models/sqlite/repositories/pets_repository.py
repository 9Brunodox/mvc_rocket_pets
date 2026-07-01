from typing import List # Para python 3.8 ou inferior
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable

class PetsRepository:
    def __init__(self, db_connection) -> None:
        self.db_connection = db_connection

    def list_pets(self) -> List:
        with self.db_connection as db:
            try:
                pets = db.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []

    def delete_pet(self, name: str) -> None:
        with self.db_connection as db:
            try:
                pet = db.session.query(PetsTable).filter_by(name=name).first()
                db.session.delete(pet)
                db.session.commit()
                return f"Pet {name} deleted successfully."
            except Exception as e:
                db.session.rollback()
                raise e
