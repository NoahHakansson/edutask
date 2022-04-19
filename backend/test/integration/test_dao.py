from typing import Collection
from src.util.dao import DAO as dao
from src.util.validators import getValidator
import pytest
import mongomock
import unittest.mock as mock
from unittest.mock import patch

MOCK_URL = "mongomock://localhost"

@pytest.fixture
def sut():
    # mock mongoDB
    with patch("src.util.dao.pymongo", side_effect=mongomock.MongoClient) as mockedDatabase:
        # create DAO
        sut = dao("todo")
        sut.collection
        return sut



@pytest.mark.staging
def test_todo_test0(sut):
    # test
    data = {"test0" : False}
    result = sut.create(data)

    assert result == {"test": "test"}


