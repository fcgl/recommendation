import time

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

The purpose of this data model is to store recommendations for a subgroup of users with similar qualities that
with a high probability are likely to purchase similar items
'''
class UserRecommendation(object):

    COLLECTION = "user_recommendation"

    def __init__(self, product_ids = [], recommendation_index = 0):
        self.product_ids = product_ids
        self.recommendation_index = recommendation_index
        self.added_on = time.time()
        self.last_updated = self.added_on

    def json(self):
        return {
            'product_ids': self.product_ids,
            'added_on': self.added_on,
            'last_updated': self.last_updated,
            'recommendation_index': self.recommendation_index
        }
