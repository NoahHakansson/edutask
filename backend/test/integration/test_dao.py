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
def sut():
    # Fixture to return todo SUT
    # create test collection
    collection = testDatabase.getCollection()
    # create DAO and set it up with the test collection
    sut = dao("todo") # todo just to create dao object. \
    # Collection will be replaced below
    sut.collection = collection
    yield sut
    # clear database after test is run
    testDatabase.clearDatabase()

##################
##### Tests #####
################

def test_create_only_required(sut):
    # test
    data = {"string-prop":"test-string"}
    result = sut.create(data)

    assert result["string-prop"] == data["string-prop"]
    
def test_create_without_required(sut):
    # test should throw Exception
    with pytest.raises(Exception) as e_info:
        data = {"boolean-prop":False}
        sut.create(data)

def test_create_duplicate_entry_of_string_prop(sut):
    # test should throw Exception
    data = {"string-prop":"already-existing-string"}
    sut.create(data)
    with pytest.raises(Exception) as e_info:
        data = {"string-prop":"already-existing-string"}
        sut.create(data)

def test_create_both_fields_comply_bson_type(sut):
    # test should throw Exception
    data = {"string-prop":"this-is-a-string", "boolean-prop":True}
    result = sut.create(data)

    assert result["string-prop"] == data["string-prop"] \
        and result["boolean-prop"] == data["boolean-prop"] 

def test_create_string_field_not_comply_bson_type(sut):
    # test should throw Exception
    with pytest.raises(Exception) as e_info:
        data = {"string-prop":1234, "boolean-prop":True}
        sut.create(data)

def test_create_boolean_field_not_comply_bson_type(sut):
    # test should throw Exception
    with pytest.raises(Exception) as e_info:
        data = {"string-prop":"this-is-a-string", "boolean-prop":1234}
        sut.create(data)


