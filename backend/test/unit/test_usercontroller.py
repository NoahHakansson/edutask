from src.controllers.usercontroller import UserController

import pytest
import unittest.mock as mock

def databaseOffline(param):
    # Function to mimic if a database operation failed
    # Takes a parameter as find() does too
    raise Exception("Error: Database is not accessable")

def test_UC01():
    mockedDatabase = mock.MagicMock()
    # return dict because we expect something from a valid email
    mockedDatabase.find.return_value = [{"email":"email@email.com"}]

    sut = UserController(dao=mockedDatabase)
    validationResult = sut.get_user_by_email("mail@mail.com")
    assert validationResult == { "email": "email@email.com"}

def test_UC02():
    mockedDatabase = mock.MagicMock()
    # return empty dict because we dont expect anything from a invalid email
    # Expects an exception
    mockedDatabase.find.return_value = []

    sut = UserController(dao=mockedDatabase)
    with pytest.raises(Exception) as e_info:
        validationResult = sut.get_user_by_email("email")

def test_UC03():
    mockedDatabase = mock.MagicMock()
    # return empty dict as database will not find an entry matching the email
    # Expects an exception
    mockedDatabase.find.return_value = []

    sut = UserController(dao=mockedDatabase)
    with pytest.raises(Exception) as e_info:
        validationResult = sut.get_user_by_email("email@email.com")

def test_UC04():
    mockedDatabase = mock.MagicMock()
    # return exception as database is offline
    # Expects a database exception indicating that the database is down
    mockedDatabase.find = databaseOffline

    sut = UserController(dao=mockedDatabase)
    with pytest.raises(Exception) as e_info:
        validationResult = sut.get_user_by_email("email@email.com")


