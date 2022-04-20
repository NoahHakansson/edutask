import collections
from typing import Collection
from src.util.dao import DAO as dao
import pytest
import unittest.mock as mock
from test.utils.initTestCollections import testDatabase

sut = testDatabase
collections = sut.getDatabase()

def test_todo_test0():
    # test
    data = {"test0" : False}
    

    assert data == {"test": "test"}

def test_todo_test1():
    # test
    data = {5 : None}
    

    assert data == {"test": "test"}

sut.clearDatabase()

