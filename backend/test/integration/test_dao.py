from typing import Collection
from src.util.dao import DAO as dao
from src.util.validators import getValidator
import pytest
import mongomock
import unittest.mock as mock
from unittest.mock import patch

def test_todo_test0():
    # mock mongoDB
    mockedDatabase = mongomock.MongoClient().db
    collection_name = "todo"
    validator = getValidator(collection_name)
    mockedDatabase.create_collection(collection_name)

    # create DAO
    sut = dao("todo")
    # set SUT collection to the mocked collection
    sut.collection = mockedDatabase[collection_name]

    data = {"test0" : False}
    result = sut.create(data)

    assert result == {"test": "test"}

