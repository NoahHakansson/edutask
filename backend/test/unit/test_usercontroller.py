from src.controllers.usercontroller import UserController

import pytest
import unittest.mock as mock

def test_usercontroller_invalid_email_format0():
    mockedDatabase = mock.MagicMock()
    mockedDatabase.find.return_value = [{"email":"mail@mail.com"}]

    sut = UserController(dao=mockedDatabase)
    with pytest.raises(Exception) as e_info:
        validationResult = sut.get_user_by_email("mail")

def test_usercontroller_invalid_email_format1():
    mockedDatabase = mock.MagicMock()
    # return empty dict because we dont expect anything from a invalid email
    mockedDatabase.find.return_value = [{"email":"mail@mail.com"}]

    sut = UserController(dao=mockedDatabase)
    with pytest.raises(Exception) as e_info:
        validationResult = sut.get_user_by_email("mail@")

def test_usercontroller_invalid_email_format2():
    mockedDatabase = mock.MagicMock()
    # return empty dict because we dont expect anything from a invalid email
    mockedDatabase.find.return_value = [{"email":"mail@mail.com"}]

    sut = UserController(dao=mockedDatabase)
    with pytest.raises(Exception) as e_info:
        validationResult = sut.get_user_by_email("mail@mail")

def test_usercontroller_valid_email_format():
    mockedDatabase = mock.MagicMock()
    # return dict because we expect something from a valid email
    mockedDatabase.find.return_value = [{"email":"mail@mail.com"}]

    sut = UserController(dao=mockedDatabase)
    validationResult = sut.get_user_by_email("mail@mail.com")
    assert validationResult == { "email": "mail@mail.com"}

def test_usercontroller_not_in_database_format0():
    mockedDatabase = mock.MagicMock()
    # return empty dict because email is not in database
    mockedDatabase.find.return_value = []

    sut = UserController(dao=mockedDatabase)
    with pytest.raises(Exception) as e_info:
        validationResult = sut.get_user_by_email("mail@mail.com")

