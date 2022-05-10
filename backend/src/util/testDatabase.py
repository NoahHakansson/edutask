# coding=utf-8
import os

import pymongo
from dotenv import dotenv_values

# create a data access object
from src.util.validators import getValidator

import json
from bson import json_util
from bson.objectid import ObjectId

collection = None

class testDatabase:

    def getCollection():
         # load the local mongo URL (something like mongodb://localhost:27017)
            LOCAL_MONGO_URL = dotenv_values('.env').get('MONGO_URL')
            # check out of the environment (which can be overridden by the docker-compose file) also specifies an URL, and use that instead if it exists
            MONGO_URL = os.environ.get('MONGO_URL', LOCAL_MONGO_URL)

            # connect to the MongoDB and select the appropriate database
            client = pymongo.MongoClient(MONGO_URL)
            database = client.edutask
            # scheme
            if "test_collection" not in database.list_collection_names():
                validator = getValidator("testValidator")
                database.create_collection("test_collection", validator=validator)
            # add all collections to dict array
            collection = database["test_collection"]
            
            
            return collection

    def clearDatabase():
        # load the local mongo URL (something like mongodb://localhost:27017)
        LOCAL_MONGO_URL = dotenv_values('.env').get('MONGO_URL')
        # check out of the environment (which can be overridden by the docker-compose file) also specifies an URL, and use that instead if it exists
        MONGO_URL = os.environ.get('MONGO_URL', LOCAL_MONGO_URL)
            # connect to the MongoDB and select the appropriate database
        client = pymongo.MongoClient(MONGO_URL)
        database = client.edutask
        database.drop_collection('test_collection')

