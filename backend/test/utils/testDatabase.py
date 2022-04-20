# coding=utf-8
import os

import pymongo
from dotenv import dotenv_values

# create a data access object
from src.util.validators import getValidator

import json
from bson import json_util
from bson.objectid import ObjectId
collections = {}

class testDatabase:

    def getDatabase():
         # load the local mongo URL (something like mongodb://localhost:27017)
            LOCAL_MONGO_URL = dotenv_values('.env').get('MONGO_URL')
            # check out of the environment (which can be overridden by the docker-compose file) also specifies an URL, and use that instead if it exists
            MONGO_URL = os.environ.get('MONGO_URL', LOCAL_MONGO_URL)

            # connect to the MongoDB and select the appropriate database
            client = pymongo.MongoClient(MONGO_URL)
            database = client.edutask
            # Todo scheme
            if "test_todo" not in database.list_collection_names():
                validator = getValidator("todo")
                database.create_collection("test_todo", validator=validator)
            # task scheme
            if "test_task" not in database.list_collection_names():
                validator = getValidator("task")
                database.create_collection("test_task", validator=validator)
            # user scheme
            if "test_user" not in database.list_collection_names():
                validator = getValidator("user")
                database.create_collection("test_user", validator=validator)
            # video scheme
            if "test_video" not in database.list_collection_names():
                validator = getValidator("video")
                database.create_collection("test_video", validator=validator)
            # add all collections to dict array
            collections = {"todo": database["test_todo"], "task":database['test_task'], "user":database['test_user'], "video":database['test_video']}
            
            
            return collections

    def clearDatabase():
        # load the local mongo URL (something like mongodb://localhost:27017)
        LOCAL_MONGO_URL = dotenv_values('.env').get('MONGO_URL')
        # check out of the environment (which can be overridden by the docker-compose file) also specifies an URL, and use that instead if it exists
        MONGO_URL = os.environ.get('MONGO_URL', LOCAL_MONGO_URL)
            # connect to the MongoDB and select the appropriate database
        client = pymongo.MongoClient(MONGO_URL)
        database = client.edutask
        database.drop_collection('test_todo')
        database.drop_collection('test_task')
        database.drop_collection('test_user')
        database.drop_collection('test_video')

