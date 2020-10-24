from os import getenv
from dotenv import load_dotenv

import pymongo

from .models import *

load_dotenv()
client = pymongo.MongoClient(getenv("MONGO_HOST"), int(getenv("MONGO_PORT")))


def save_model_in_database(model):
    collection = client[model.database_name][model.collection_name]

    if collection.find_one(vars(model)) is not None:
        raise Exception("Already in database")
    else:
        collection.insert_one(vars(model))


def find_one_in_client(object):
    for database_name in client.list_database_names():
        database = client[database_name]

        for collection_name in database.list_collection_names():
            collection = database[collection_name]

            object_from_db = collection.find_one(object)

            if object_from_db is not None:
                return object_from_db
    return None


def find_one_in_standart_database(object):
    collection = client[DatabaseObject().database_name][DatabaseObject().collection_name]
    return collection.find_one(object)
