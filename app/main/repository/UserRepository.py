from ..database import DB

class UserRepository(object):

    COLLECTION = "user"

    @staticmethod
    def insert(user):
        if not DB.find_one(UserRepository.COLLECTION, {"_id": user.id}):
            id = DB.insert(collection=UserRepository.COLLECTION, data=user.json())
            return {'id': id, 'message': 'Successfully added'}
        else:
            return {'id': None, 'message': 'User Already Exists'}
    '''
    Returns a list of Users from a specified city
    '''
    @staticmethod
    def find_all_by_city_id(city_id):
        return DB.find_all_by_query(
            collection=UserRepository.COLLECTION,
            query= {'city_id': city_id})


    @staticmethod
    def update_many(query, new_values):
        DB.update_many(UserRepository.COLLECTION, query, new_values)


    @staticmethod
    def find_one(query):
        return DB.find_one(UserRepository.COLLECTION, query)
