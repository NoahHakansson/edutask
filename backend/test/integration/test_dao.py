from typing import Collection
from src.util.dao import DAO as dao
from src.util.validators import getValidator
import pytest
import mongomock
import unittest.mock as mock
from unittest.mock import patch

@pytest.fixture
def sut_todo():
    # mock mongoDB
    with patch("src.util.dao.pymongo", side_effect=mongomock.MongoClient) as mockedDatabase:
        # create DAO
        sut_todo = dao("todo")
        return sut_todo



def test_todo_test0(sut_todo):
    # mock mongoDB
    with patch("src.util.dao.pymongo", side_effect=mongomock.MongoClient) as mockedDatabase:
        # create DAO
        sut = dao("todo")

        # test
        data = {"test0" : False}
        result = sut.create(data)

        assert result == {"test": "test"}


