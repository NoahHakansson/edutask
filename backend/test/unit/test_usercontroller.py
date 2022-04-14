from src.controllers.usercontroller import UserController

import pytest
import unittest.mock as mock

def test_usercontroller_invalid_email_format():
    mockedDatabase = mock.MagicMock()
    # return empty dict because we dont expect anything from a invalid email
    mockedDatabase.find.return_value = []

    sut = UserController(dao=mockedDatabase)
    validationResult = sut.get_user_by_email("mail")

    assert validationResult == "test"

def test_usercontroller_valid_email_format():
    mockedDatabase = mock.MagicMock()
    # return dict because we expect something from a valid email
    mockedDatabase.find.return_value = [{"email":"mail@mail.com"}]

    sut = UserController(dao=mockedDatabase)
    validationResult = sut.get_user_by_email("mail@mail.com")
    assert validationResult == { "email": "mail@mail.com"}

