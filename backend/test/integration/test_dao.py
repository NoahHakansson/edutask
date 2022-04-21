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

def task_sut():
    # Fixture to return task SUT
    # create test collections
    collections = testDatabase.getDatabase()
    # create DAO and set it up with the test collection
    sut = dao("task")
    sut.collection = collections["task"]
    yield sut
    # clear database after test is run
    testDatabase.clearDatabase()

def user_sut():
    # Fixture to return user SUT
    # create test collections
    collections = testDatabase.getDatabase()
    # create DAO and set it up with the test collection
    sut = dao("user")
    sut.collection = collections["user"]
    yield sut
    # clear database after test is run
    testDatabase.clearDatabase()

def video_sut():
    # Fixture to return video SUT
    # create test collections
    collections = testDatabase.getDatabase()
    # create DAO and set it up with the test collection
    sut = dao("video")
    sut.collection = collections["video"]
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

def test_task_test0(task_sut):
    # test
    data = {"description":"test0"}
    result = task_sut.create(data)

    assert result == {"test": "test"}

def test_task_test1(task_sut):
    # test
    data = {"description":"test1", "done": False}
    result = task_sut.create(data)

    assert result == {"test": "test"}

def test_task_test2(task_sut):
    # test
    data = {"description":5, "done": False}
    result = task_sut.create(data)

    assert result == {"test": "test"}

def test_user_test0(user_sut):
    # test
    data = {"description":"test0"}
    result = user_sut.create(data)

    assert result == {"test": "test"}

def test_user_test1(user_sut):
    # test
    data = {"description":"test1", "done": False}
    result = user_sut.create(data)

    assert result == {"test": "test"}

def test_user_test2(user_sut):
    # test
    data = {"description":5, "done": False}
    result = user_sut.create(data)

    assert result == {"test": "test"}

def test_video_test0(video_sut):
    # test
    data = {"description":"test0"}
    result = video_sut.create(data)

    assert result == {"test": "test"}

def test_todo_test1(video_sut):
    # test
    data = {"description":"test1", "done": False}
    result = video_sut.create(data)

    assert result == {"test": "test"}

def test_todo_test2(video_sut):
    # test
    data = {"description":5, "done": False}
    result = video_sut.create(data)

    assert result == {"test": "test"}

