from typing import Collection
from src.util.dao import DAO as dao
from src.util.validators import getValidator
import pytest
import mongomock
import unittest.mock as mock
from unittest.mock import patch

MOCK_URL = "mock url goes here"

# @pytest.fixture
# def sut():
#     # Mocks the actual database url that we connect to with MOCK_URL constant above
#     with patch("src.util.dao.os", autospec=True) as mockedDAO:
#         mockedDAO.environ.get.return_value = MOCK_URL
#         # create DAO
#         sut = dao("todo")
#         sut.collection
#         return sut

@pytest.fixture
def sut():
    # mock mongoDB
    with patch("src.util.dao.pymongo", side_effect=mongomock.MongoClient) as mockedDatabase:
        # create DAO
        sut = dao("todo")
        sut.collection
        return sut



def test_todo_test0(sut):
    # test
    data = {"test0" : False}
    result = sut.create(data)

    assert result == {"test": "test"}

def test_todo_test1(sut):
    # test
    data = {5 : None}
    result = sut.create(data)

    assert result == {"test": "test"}

