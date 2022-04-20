import collections
from typing import Collection
from src.util.dao import DAO as dao
import pytest
import unittest.mock as mock
from src.util.testDatabase import testDatabase


@pytest.fixture
def todo_sut():
    # Fixture to return todo SUT
    # create test collections
    collections = testDatabase.getDatabase()
    # create DAO and set it up with the test collection
    sut = dao("todo")
    sut.collection = collections["todo"]
    yield sut
    # clear database after test is run
    testDatabase.clearDatabase()

def test_todo_test0(todo_sut):
    # test
    data = {"description":"test0"}
    result = todo_sut.create(data)

    assert result == {"test": "test"}

def test_todo_test1(todo_sut):
    # test
    data = {"description":"test1", "done": False}
    result = todo_sut.create(data)

    assert result == {"test": "test"}

def test_todo_test2(todo_sut):
    # test
    data = {"description":5, "done": False}
    result = todo_sut.create(data)

    assert result == {"test": "test"}


