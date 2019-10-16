from ..database import DB


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
class UserRecommendationRepository(object):

    COLLECTION = "user_recommendation"

    '''
    Inserts a new user_recommendation entry
    Returns the ID of the new entry
    '''
    @staticmethod
    def insert(user_recommendation):
        # if not DB.find_one(UserRecommendation.COLLECTION, {"_id": self.id}):
        return DB.insert(collection=UserRecommendationRepository.COLLECTION, data=user_recommendation.json())

    @staticmethod
    def bulk_delete(query={}):
        DB.bulk_delete(UserRecommendationRepository.COLLECTION, query)

    @staticmethod
    def insert_many(user_recommendations):
        DB.insert_many(collection=UserRecommendationRepository.COLLECTION, data=user_recommendations)

    @staticmethod
    def find_one(query):
        return DB.find_one(UserRecommendationRepository.COLLECTION, query)

    @staticmethod
    def find_all():
        return DB.find_all(UserRecommendationRepository.COLLECTION)



