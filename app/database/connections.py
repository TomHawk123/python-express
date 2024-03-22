from pymongo import MongoClient
from flask import current_app, g
from utils.dotenv_config import dotenv_config

# Load environment variables
dotenv_config()


def get_db1():
    if 'db1' not in g:
        g.db1 = MongoClient(current_app.config['DB1'])

    return g.db1


def get_db2():
    if 'db2' not in g:
        g.db2 = MongoClient(current_app.config['DB2'])

    return g.db2


def close_connection(exception):
    db1 = g.pop('db1', None)
    db2 = g.pop('db2', None)

    if db1 is not None:
        db1.close()
    if db2 is not None:
        db2.close()
