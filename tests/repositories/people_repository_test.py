# pylint: disable=duplicate-code

from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.repositories.people_repository import PeopleRepository

class MockConnection:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PeopleTable)],
                    [
                        PeopleTable(first_name="John", last_name="Doe", age=30, pet_id=1),
                        PeopleTable(first_name="Jane", last_name="Smith", age=25, pet_id=2),
                    ]
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

def test_insert_person():
    mock_connection = MockConnection()
    people_repository = PeopleRepository(mock_connection)

    people_repository.insert_person(first_name="John", last_name="Doe", age=30, pet_id=1)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()

def test_list_peoples():
    mock_connection = MockConnection()
    people_repository = PeopleRepository(mock_connection)
    response_peoples_list = people_repository.list_peoples()

    mock_connection.session.query.assert_called_once_with(PeopleTable)
    mock_connection.session.all.assert_called_once()

    assert response_peoples_list is not None
    assert response_peoples_list[0].first_name == "John"

def test_list_peoples_no_result():
    mock_connection = MockConnectionNoResult()
    people_repository = PeopleRepository(mock_connection)
    response_peoples_list = people_repository.list_peoples()

    mock_connection.session.query.assert_called_once_with(PeopleTable)
    mock_connection.session.all.assert_not_called()

    assert response_peoples_list == []

def test_delete_person():
    mock_connection = MockConnection()
    people_repository = PeopleRepository(mock_connection)

    people_repository.delete_person("John")

    mock_connection.session.query.assert_called_once_with(PeopleTable)
    mock_connection.session.query().filter_by.assert_called_once_with(name="John")
    mock_connection.session.delete.assert_called_once()

def test_delete_person_no_result():
    mock_connection = MockConnectionNoResult()
    people_repository = PeopleRepository(mock_connection)

    with pytest.raises(Exception):
        people_repository.delete_person("John")

    mock_connection.session.rollback.assert_called_once()
