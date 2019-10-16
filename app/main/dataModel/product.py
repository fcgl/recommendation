import time

from ..database import DB

'''
Product Data
Example:
{
    “id” : 1,
    “name”: “12oz Coke”,
    “retail_price”: 1.50,
    “categories”: [
        “beverage”,
         “soda”
     ],
    “added_on”: 12342352
    “last_updated”: 12342942,
    "popularity_index": 4.32,
    "cities": [1,2,6]
}

'''
class Product(object):

    COLLECTION = "products"

    def __init__(self, id, name, retail_price, categories, cities = [], popularity_index = 0):
        self.id = id
        self.name = name
        self.retail_price = retail_price
        self.categories = categories
        self.added_on = time.time()
        self.last_updated = self.added_on
        self.popularity_index = popularity_index
        self.cities = cities

    def json(self):
        return {
            '_id': self.id,
            'name': self.name,
            'retail_price': self.retail_price,
            'categories': self.categories,
            'added_on': self.added_on,
            'last_updated': self.last_updated,
            "popularity_index": self.popularity_index,
            "cities": self.cities
        }
