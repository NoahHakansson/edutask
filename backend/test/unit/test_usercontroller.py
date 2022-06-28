from src.controllers.usercontroller import UserController

import pytest
from _pytest.capture import capfd
import unittest.mock as mock

def database_offline():
    # Function to mimic if a database operation failed
    # Takes a parameter as find() does too
    raise Exception("Error: Database is not accessable")

def database_operation_failed():
    # Function to mimic if a database operation failed
    # Takes a parameter as find does too
    raise Exception("Error: Database operation failed")

def test_valid_email():
    mockedDatabase = mock.MagicMock()
    # return dict because we expect something from a valid email
    mockedDatabase.find.return_value = [{"email":"email@email.com"}]

    sut = UserController(dao=mockedDatabase)
    validationResult = sut.get_user_by_email("email@email.com")
    assert validationResult == { "email": "email@email.com"}

def test_warning_on_multiple_users(capsys):
    mockedDatabase = mock.MagicMock()
    # return two users with same email
    mockedDatabase.find.return_value = \
            [{"email":"email@email.com"}, {"email":"email@email.com"}]

    sut = UserController(dao=mockedDatabase)
    sut.get_user_by_email("email@email.com")
    # capture stdout so we can catch the warning printed by get_user_by_email
    out, err = capsys.readouterr()
    assert "Error: more than one user found with mail" in out

def test_email_missing_substring1():
    mockedDatabase = mock.MagicMock()
    # return empty dict because we dont expect anything from a invalid email
    # Expects an exception
    mockedDatabase.find.return_value = []

    sut = UserController(dao=mockedDatabase)
    with pytest.raises(Exception) as e_info:
        sut.get_user_by_email("@email.com")

def test_email_missing_substring2():
    mockedDatabase = mock.MagicMock()
    # return empty dict because we dont expect anything from a invalid email
    # Expects an exception
    mockedDatabase.find.return_value = []

    sut = UserController(dao=mockedDatabase)
    with pytest.raises(Exception) as e_info:
        sut.get_user_by_email("email@.com")

def test_email_missing_substring3():
    mockedDatabase = mock.MagicMock()
    # return empty dict because we dont expect anything from a invalid email
    # Expects an exception
    mockedDatabase.find.return_value = []

    sut = UserController(dao=mockedDatabase)
    with pytest.raises(Exception) as e_info:
        sut.get_user_by_email("email@email.")

def test_email_missing_at_sign():
    mockedDatabase = mock.MagicMock()
    # return empty dict because we dont expect anything from a invalid email
    # Expects an exception
    mockedDatabase.find.return_value = []

    sut = UserController(dao=mockedDatabase)
    with pytest.raises(Exception) as e_info:
        sut.get_user_by_email("emailemail.com")

def test_email_missing_dot_after_domain():
    mockedDatabase = mock.MagicMock()
    # return empty dict because we dont expect anything from a invalid email
    # Expects an exception
    mockedDatabase.find.return_value = []

    sut = UserController(dao=mockedDatabase)
    with pytest.raises(Exception) as e_info:
        sut.get_user_by_email("email@emailcom")

def test_email_not_found():
    mockedDatabase = mock.MagicMock()
    # return empty dict as database will not find an entry matching the email
    # Expects an exception
    mockedDatabase.find.return_value = []

    sut = UserController(dao=mockedDatabase)
    with pytest.raises(Exception) as e_info:
        sut.get_user_by_email("email@email.com")

def test_database_offline():
    mockedDatabase = mock.MagicMock()
    # database operation fails
    # return exception as database is offline
    # Expects a database exception indicating that the database is down
    mockedDatabase.find = database_offline

    sut = UserController(dao=mockedDatabase)
    with pytest.raises(Exception) as e_info:
        sut.get_user_by_email("email@email.com")

def test_database_operation_fails():
    mockedDatabase = mock.MagicMock()
    # database operation fails
    # return exception as database is offline
    # Expects a database exception indicating that the database is down
    mockedDatabase.find = database_operation_failed

    sut = UserController(dao=mockedDatabase)
    with pytest.raises(Exception) as e_info:
        sut.get_user_by_email("email@email.com")

