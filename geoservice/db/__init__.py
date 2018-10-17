import os

from pymongo import MongoClient

current_client = None


def client():

    global current_client

    if not current_client:
        current_client = MongoClient(os.getenv('MONGO_DB_URI'))

    return current_client
