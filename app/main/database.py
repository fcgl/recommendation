import pymongo

'''
Creates a database connection and introduces helper functions that call pymongo functions
'''
class DB(object):

    URI = "mongodb://mongodb:27017/"
    DB_NAME = "recommendation"

    @staticmethod
    def __init__():
        # connecting to the database.
        client = pymongo.MongoClient(DB.URI)
        DB.DATABASE = client[DB.DB_NAME]

    @staticmethod
    def insert(collection, data):
        result = DB.DATABASE[collection].insert_one(data)
        return result.inserted_id

    @staticmethod
    def find_one(collection, query):
        return DB.DATABASE[collection].find_one(query)

    @staticmethod
    def find_all(collection):
        return DB.DATABASE[collection].find({})

    @staticmethod
    def bulk_insert(collection,data):
        DB.DATABASE[collection].insert_many(data)

    @staticmethod
    def bulk_delete(collection, query = {}):
        DB.DATABASE[collection].delete_many(query)

    @staticmethod
    def find_all_by_query(collection, query, limit, sort=[], params={}):
        return DB.DATABASE[collection].find(query, params).sort(sort).limit(limit)

    @staticmethod
    def insert_many(collection, data):
        DB.DATABASE[collection].insert_many(data)

    @staticmethod
    def update(collection, query, new_values):
        DB.DATABASE[collection].update_one(query, new_values)

    @staticmethod
    def update_many(collection, query, new_values):
        DB.DATABASE[collection].update_many(query, new_values)