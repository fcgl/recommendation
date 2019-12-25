from ..database import DB
from ..dataModel.user_recommendation import UserRecommendation
from ..repository.ProductRepository import ProductRepository
from ..repository.UserRecommendationRepository import UserRecommendationRepository
from ..repository.UserRepository import UserRepository

from ..util.data_cleaning import DataProcessing
import pandas as pd

class UserRecommendationService(object):

    def __init__(self, recommendation_active = False , process='purchase_count'):
        self.recommendation_active = recommendation_active
        self.process = process


    def update_user_recommendations(self):
        if self.recommendation_active:
            self._machine_learning_process()
        else:
            self._generic_process()



    '''
    Queries for the most popular items in a given city. Inserts one entry to the
    user_recommendation database collection per city. Updates every User's recommendation_id
    to that of the inserted user_recommendation entry
    This is the generic recommnedation which is based on the popilar items in the given city.   
    '''
    def _generic_process(self):
        #TODO: Change logic so that the entire process is not commited unless everything is ran correctly (in case of errors)
        UserRecommendationRepository.bulk_delete()
        list_of_cities = self._get_list_of_cities()
        for city in list_of_cities:
            #TODO: Update so that we run the update for every 1000 users. Will help to keep the RAM usage low
            # list_of_city_users = self._get_all_city_users(city)
            self._set_user_recommendation(city)


    '''
    Calls a function that begins the recommendation algorithm process 
    Should insert new recommendations in the user_recommendation database collection
    and update a User's recommendation_id.
    '''
    def _machine_learning_process(self):
        purchase_count_explicit, purchase_count_implicit,users_explicit, users_implicit = DataProcessing.start()

        if self.process =='purchase_count':
            purchase_count = pd.Dataframe(purchase_count_explicit.groupby(['product_id'])['purchased_count'].sum())
            top10 = purchase_count.sort_values('purchase_count' , ascending=False).head(10)
        
        UserRecommendationRepository.bulk_delete()
        UserRecommendationRepository.insert(top10)
                    
        return UserRecommendationRepository        


    '''
    Takes in a user_id
    Returns a list of product_ids recommended to a user
    '''
    def get_user_recommendations(self, user_id):
        user = UserRepository.find_one({'_id': user_id})
        if user is None:
            return {'message': 'user not found', 'product_ids': [], 'success': False, 'userId': user_id}
        recommendation_id = user['recommendation_id']
        user_recommendation = UserRecommendationRepository.find_one({'_id': recommendation_id})
        if user_recommendation is None:
            return {'message': 'no recommendations found', 'product_ids': [], 'success': True}
        product_ids = user_recommendation['product_ids']
        products = []
        for product_id in product_ids:
            current_product = ProductRepository.find_one({'_id': product_id['_id']})
            if current_product:
                products.append(current_product)
        return {'success': True, 'message': 'Found recommended product ids', 'products': products}


    '''
    Returns list of cities from userInteraction API request
    '''
    def _get_list_of_cities(self):
        #TODO: update this to make an API request
        return [1]

    '''
    Returns a list of Users from a specific city
    TODO: Add pagination to avoid memory issues
    '''
    def _get_all_city_users(self, city_id, page = 0, size = 0):
        return UserRepository.find_all_by_city_id()

    def get_most_popular_by_city(self, city_id, limit=30):
        return ProductRepository.find_all_by_city_id_sort_by_popularity_index(city_id, limit)

    def _set_user_recommendation(self, city):
        #TODO: Update so that we run the update for every 1000 users. Will help to keep the RAM usage low
        # list_of_city_users = self._get_all_city_users(city)
        list_of_popular_city_products = list(self.get_most_popular_by_city(city))
        user_recommendation = UserRecommendation(product_ids = list_of_popular_city_products, recommendation_index = 0)
        user_recommendation_id = UserRecommendationRepository.insert(user_recommendation)
        UserRepository.update_many({'city_id': city}, {"$set": {'recommendation_id': user_recommendation_id}})
