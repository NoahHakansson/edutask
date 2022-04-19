from typing import Collection
import pytest
from src.util.dao import DAO as dao
from pytest_mock_resources import create_mongo_fixture
from src.util.validators import getValidator
import unittest.mock as mock
from unittest.mock import patch

def test_todo_test0():
    # return empty dict because we dont expect anything from a invalid email
    mongo = create_mongo_fixture()
    validator = getValidator("todo")
    sut = dao("todo")
    sut.collection = mongo['todo']

    data = {"test0" : False}
    result = sut.create(data)

    assert result == {"test": "test"}

