import time

from ..database import DB

'''
User Data
Example:
{
    “_id”: 2,
    “nationality”: 3,
    "age": 22,
    “average_spent”: 24.37,
    “added_on”: 12342352
    “last_updated”: 12342942,
    "city_id": 1
    "recommendation_id": 1
 }



'''
class User(object):

    COLLECTION = "user"

    def __init__(self, user_id, age, nationality, average_spent, city_id):
        self.id = user_id
        self.recommendation_id = 0
        self.age = age
        self.user_id = user_id
        self.nationality = nationality
        self.average_spent = average_spent
        self.added_on = time.time()
        self.last_updated = self.added_on
        self.city_id = city_id

    def json(self):
        return {
            '_id': self.id,
            'nationality': self.nationality,
            'age': self.age,
            'average_spent': self.average_spent,
            'added_on': self.added_on,
            'last_updated': self.last_updated,
            'recommendation_id': self.recommendation_id,
            'city_id': self.city_id
        }

    def get_id(self):
        self.getId()

    def set_id(self, id):
        self.id = id
