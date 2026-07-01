from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.repositories.pets_repository import PetsRepository

class MockConnection:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],
                    [
                        PetsTable(name="dog", type="dog"),
                        PetsTable(name="cat", type="cat"),
                    ],
                )
            ]
        )

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_value, traceback): pass

class MockConnectionNoResult:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No Result Found")
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_value, traceback): pass

def test_list_pets():
    mock_connection = MockConnection()
    pets_repository = PetsRepository(mock_connection)
    response_pets_list = pets_repository.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response_pets_list is not None
    assert response_pets_list[0].name == "dog"

def test_delete_pet():
    mock_connection = MockConnection()
    pets_repository = PetsRepository(mock_connection)

    pets_repository.delete_pet("dog")

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.query().filter_by.assert_called_once_with(name="dog")
    mock_connection.session.delete.assert_called_once()

def test_list_pets_no_result():
    mock_connection = MockConnectionNoResult()
    pets_repository = PetsRepository(mock_connection)
    response_pets_list = pets_repository.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response_pets_list == []

def test_delete_pet_no_result():
    mock_connection = MockConnectionNoResult()
    pets_repository = PetsRepository(mock_connection)

    with pytest.raises(Exception):
        pets_repository.delete_pet("dog")

    mock_connection.session.rollback.assert_called_once()
