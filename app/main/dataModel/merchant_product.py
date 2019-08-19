import time

from ..database import DB

'''
Merchant Product Data
Example:
 {
    “id”: 1,
    “mechant_id”: 245,
    “product_id”: 452
    “price”: {currency: “$”, “amount”: 12.45}
 }
'''
class Merchant_Product(object):

    COLLECTION = "merchant_products"

    def __init__(self, id, merchant_id, product_id, price, currency):
        self.id = id;
        self.merchant_id = merchant_id
        self.product_id = product_id
        self.price = price
        self.currency = currency
        self.added_on = time.time()
        self.last_updated = self.added_on

    def insert(self):
        if not DB.find_one(Merchant_Product.COLLECTION, {"_id": self.id}):
            DB.insert(collection=Merchant_Product.COLLECTION, data=self.json())

    def json(self):
        return {
            '_id': self.id,
            'merchant_id': self.merchant_id,
            'product_id': self.product_id,
            'price': {'currency': '$', “amount”: 12.45},
            'added_on': self.added_on,
            'last_updated': self.last_updated
        }
