import collections
from typing import Collection
from src.util.dao import DAO as dao
import pytest
import unittest.mock as mock
from src.util.testDatabase import testDatabase


#######################
###### Fixtures ######
#####################
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

@pytest.fixture
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

@pytest.fixture
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

@pytest.fixture
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

##################
##### Tests #####
################

# user SUT
def test_user_test0(user_sut):
    # test
    data = {"firstName":"test", "lastName":"test", "email": "test"}
    result = user_sut.create(data)

    assert result["firstName"] == data["firstName"] \
        and result["lastName"] == data["lastName"] \
        and result["email"] == data["email"]

def test_user_test1(user_sut):
    # test should throw Exception
    with pytest.raises(Exception) as e_info:
        data = {"firstname":5, "lastname":"test", "email": "test"}
        result = user_sut.create(data)


def test_user_test2(user_sut):
    # test should throw Exception
    with pytest.raises(Exception) as e_info:
        data = {"lastname":"test", "email": "test"}
        result = user_sut.create(data)


# task SUT
def test_task_test0(task_sut):
    # test
    data = {"title":"title","description":"test0"}
    result = task_sut.create(data)

    assert result["title"] == data["title"] \
        and result["description"] == data["description"]

def test_task_test1(task_sut):
    # test should throw Exception
    with pytest.raises(Exception) as e_info:
        data = {"description":"test1"}
        result = task_sut.create(data)


def test_task_test2(task_sut):
    # test should throw Exception
    with pytest.raises(Exception) as e_info:
        data = {"title":5,"description":5}
        result = task_sut.create(data)


# todo SUT
def test_todo_test0(todo_sut):
    # test
    data = {"description":"test0"}
    result = todo_sut.create(data)

    assert result["description"] == data["description"] 

def test_todo_test1(todo_sut):
    # test
    data = {"description":"test1", "done": False}
    result = todo_sut.create(data)

    assert result["description"] == data["description"] \
        and result["done"] == data["done"]

def test_todo_test2(todo_sut):
    # test should throw Exception
    with pytest.raises(Exception) as e_info:
        data = {"description":5, "done": False}
        result = todo_sut.create(data)


# video SUT
def test_video_test0(video_sut):
    # test
    data = {"url":"test"}
    result = video_sut.create(data)

    assert result["url"] == data["url"]

def test_video_test1(video_sut):
    # test should throw Exception
    with pytest.raises(Exception) as e_info:
        data = {"url": 5}
        result = video_sut.create(data)

# test uniqueItems flag / duplicate item
def test_uniqueItems_task0(task_sut):
    # test should throw Exception

    data = {"title":"title","description":"test0"}
    result = task_sut.create(data)

    # try to insert/create duplicate entry
    with pytest.raises(Exception) as e_info:
        data = {"title":"title","description":"test0"}
        result = task_sut.create(data)

