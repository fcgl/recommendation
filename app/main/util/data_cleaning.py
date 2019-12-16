from ..dataModel.user_recommendation import UserRecommendation
from ..dataModel.category import Category
from ..dataModel.merchant_category import Merchant_Category
from ..dataModel.merchant_product import Merchant_Product
from ..dataModel.merchant import Merchant
from ..dataModel.product import Product
from ..dataModel.user_purchase import UserPurchase
from ..datkaModel.user import User

from ..database import DB

import numpy as np
import pandas as pd

def read_mongo(db, collection,no_id=True):
    """ Read from Mongo and Store into DataFrame """

    # Connect to MongoDB - For that we are making a call to the DB class which gives us the database connection and gives helper functions for that.

    # Make a query to the specific DB and Collection
    data = db.find_all(collection)
    # Expand the user_data mongo field and construct the DataFrame
    df =  pd.DataFrame(list(data))


    # Delete the _id from the dataframe as it is of no use for other collection.
    # The user_id is the only thing required else the id generated in each of the other collection is of no use.
    if no_id:
        del df['id']
        # need to take care of the added_on and last_updated tables also.

    return df


class DataProcessing(object):
    def __init__(self):
        
        self.user_df          = read_mongo(DB, User.COLLECTION , no_id= False)
        self.user_purchase_df = read_mongo(DB, UserPurchase.COLLECTION , no_id=True) # Not sure abt the no_id here if there are mutliple entries for the same user
        self.product_df       = read_mongo(DB, Product.COLLECTION, no_id=False)
        self.merchant_df      = read_mongo(DB, Merchant.COLLECTION, no_id=False)
        self.merchant_prod_df = read_mongo(DB, Merchant_Product.COLLECTION, no_id=True)
        self.merchant_cat_df  = read_mongo(DB, Merchant_Category.COLLECTION, no_id=True)
        self.category_df      = read_mongo(DB , Category.COLLECTION, no_id=False)
        # the user_recommenation dataframe could be used for something like the toggling task or something.
        self.user_rec_df      = read_mongo(DB, UserRecommendation.COLLECTION, no_id=True)


    def start(self):

        """
        The last updated data or added_on doesn't make any useful contribution to the data unless we need to just check if the 
        item is available in the shop or not while recommending so we will just use those column fields for just an affirmation 
        the item is available at the recommended shop.
        """
        self.user_df.drop(['added_on', 'last_updated'], inplace=True)
        self.user_purchase_df.drop(['added_on', 'last_updated'], inplace=True)
        self.product_df.drop(['added_on' , 'last_updated'] , inplace=True)
        self.merchant_df.drop(['added_on' , 'last_updated'] , inplace=True)
        self.merchant_prod_df.drop(['added_on' , 'last_updated'] , inplace=True)
        self.merchant_cat_df.drop(['added_on' , 'last_updated'] , inplace=True)
        self.category_df.drop(['added_on' , 'last_updated'] , inplace=True)

        # self.user_rec_df.drop(['added_on' , 'last_updated'] , inplace=True)

        """
        Age column has a NaN and some very high values. In my view ages below 5 and above 90 do not make much sense, 
        and hence, these are being replaced with NaNs.
        All the NaNs are then replaced with mean value of Age, and its data type is set as int.
        """

        self.user_df.loc[(self.user_df.age > 90)|(self.user_df.age<5) ,'age' ] = np.nan 
        self.user_df.age = self.user_df.fillna( self.user_df.age.mean() )
        self.user_df.age = self.user_df.age.astype(np.int32)


        # we need to make sure the items that the user givves are also present in our database.

        """
        The explicit purchase_count represented by 1–10 and implicit represented by 0 will have to be segregated now
        """
        purchase_count_explicit = self.user_purchase_df[self.user_purchase_df.purchase_count !=0]
        purchase_count_implicit = self.user_purchase_df[self.user_purchase_df.purchase_count ==0]

        users_explicit  = self.user_df[self.user_df.id.isin(purchase_count_explicit.user_id)]
        users_implicit  = self.user_df[self.user_df.id.isin(purchase_count_implicit.user_id)]


        return purchase_count_explicit, purchase_count_implicit, \
            users_explicit, users_implicit


