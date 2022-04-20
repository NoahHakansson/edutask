import collections
from typing import Collection
from src.util.dao import DAO as dao
import pytest
import unittest.mock as mock
from test.utils.testDatabase import testDatabase

collections = testDatabase.getDatabase()

def test_todo_test0():
    # test
    sut = dao("task")
    sut.collection = collections['task']
    

    assert {} == {"test": "test"}

def test_todo_test1():
    # test
    data = {5 : None}
    

    assert data == {"test": "test"}


