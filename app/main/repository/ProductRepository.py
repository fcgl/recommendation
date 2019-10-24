from ..database import DB
import pymongo
'''
User Recommendation Data
Example:
{
            'product_ids': [1,2,3,87],
            'added_on': 234234234,
            'last_updated': 23523234,
            'recommendation_index': 1-10
 }

'''
class ProductRepository(object):

    COLLECTION = "products"

    @staticmethod
    def insert(product):
        if not DB.find_one(ProductRepository.COLLECTION, {"_id": product.id}):
            id = DB.insert(collection=ProductRepository.COLLECTION, data=product.json())
            return {'id': id, 'message': 'Successfully added'}
        else:
            return {'id': None, 'message': 'Product Already Exists'}


    @staticmethod
    def find_all_by_city_id_sort_by_popularity_index(city_id, limit=30, params={}):
        return DB.find_all_by_query(
            collection=ProductRepository.COLLECTION,
            query={'cities': [city_id]},
            params=params,
            limit=limit,
            sort=[('popularity_index', pymongo.DESCENDING)]
        )

    @staticmethod
    def find_one(query):
        return DB.find_one(ProductRepository.COLLECTION, query)

