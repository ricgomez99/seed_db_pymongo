import certifi
from pymongo import MongoClient


def create_connection(url: str | None, db_name: str):
    client = MongoClient(url, tls=True, tlsCAFile=certifi.where())
    return client[db_name]