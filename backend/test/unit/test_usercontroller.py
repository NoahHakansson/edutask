from src.controllers.usercontroller import UserController

import pytest
import unittest.mock as mock

def test_usercontroller_invalid_email_format():
    mockedUserController = mock.MagicMock()
    # return empty dict because we dont expect anything from a invalid email
    mockedUserController.get.return_value = {}

    sut = UserController(dao=mockedUserController)
    validationResult = sut.get_user_by_email("mail")

    assert validationResult == "test"


