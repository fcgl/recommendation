from flask import request
from flask_restplus import Resource
from ..dataModel.category import Category
from ..dataModel.merchant import Merchant
from ..database import DB
from bson.json_util import dumps
import json
from bson.objectid import ObjectId

from ..util.dto import DevEndpoint
from ..dataModel.user import User
from ..dataModel.product import Product
from ..repository.UserRepository import UserRepository
from ..repository.ProductRepository import ProductRepository

api = DevEndpoint.api

@api.route('/v1/category')
@api.doc(params={'id': 'Category ID', 'name': 'Category Name'})
class CategoryAPI(Resource):
    @api.doc('Gets all the categories in the database')
    def get(self):
        """Gets all the categories in the categories collection"""
        categories = DB.find_all("categories")
        return dumps(categories)

    @api.doc('Adds a category to the database')
    def post(self):
        """Adds category to the database."""
        id = request.args.get('id', '')
        name = request.args.get('name', '')
        new_category = Category(id, name)
        new_category.insert()
        return ({'message': 'Successfully Added'}, 200)

@api.route('/v1/merchant')
@api.doc(params={'id': 'Merchant ID', 'name': 'Merchant Name', 'location': 'Merchant Address'})
class MerchantAPI(Resource):
    @api.doc('Gets all the merchants in the database')
    def get(self):
        """Gets all the categories in the categories collection"""
        merchants = DB.find_all("merchants")
        return dumps(merchants)

    @api.doc('Adds a merchant to the database')
    def post(self):
        """Adds merchant to the database."""
        id = request.args.get('id', '')
        name = request.args.get('name', '')
        location = request.args.get('location', '')
        new_merchant = Merchant(id, name, location)
        new_merchant.insert()
        return ({'message': 'Successfully Added'}, 200)


@api.route('/v1/product')
class ProductAPI(Resource):
    @api.doc('Gets all the products in the database')
    def get(self):
        """Gets all the products in the products collection"""
        products = DB.find_all(ProductRepository.COLLECTION)
        return dumps(products)


@api.route('/v1/merchant_category')
class MerchantCategoryAPI(Resource):
    @api.doc('Gets all the merchant categories in the database')
    def get(self):
        """Gets all the products in the products collection"""
        merchant_categories = DB.find_all("merchant_categories")
        return dumps(merchant_categories)


@api.route('/v1/merchant_product')
class MerchantProductAPI(Resource):
    @api.doc('Gets all the merchant products in the database')
    def get(self):
        """Gets all the merchant products in the merchant products collection"""
        merchant_categories = DB.find_all("merchant_products")
        return dumps(merchant_categories)

@api.route('/v1/user')
class UserAPI(Resource):
    @api.doc('Gets all the Users in the database')
    def get(self):
        """Gets all the users in the user collection"""
        users = DB.find_all(UserRepository.COLLECTION)
        return dumps(users)

@api.route('/v1/populate_data')
class DataPopulation(Resource):

    @api.doc('Populate some initial data for testing purposes on Development')
    def get(self):
        DB.bulk_delete(ProductRepository.COLLECTION)
        DB.bulk_delete(UserRepository.COLLECTION)
        user1 =  User(1, 22, 'Peru', '100$', 1)
        user2 =  User(2, 22, 'Peru', '100$', 1)

        product1 = Product(1, 'coca cola 12oz', 12.30, ['beverage', 'soda'], [1], 2.6)
        product2 = Product(2, 'doritoz family size', 2.30, ['snack', 'chip'], [1], 4.6)
        product3 = Product(3, 'greek yogurt', 5.30, ['snack', 'dairy'], [1], 5.6)

        user1 = UserRepository.insert(user1)
        user2 = UserRepository.insert(user2)
        product1 = ProductRepository.insert(product1)
        product2 = ProductRepository.insert(product2)
        product3 = ProductRepository.insert(product3)

        created_users = [user1, user2]
        created_products = [product1, product2, product3]
        return {
                   'message': 'Successfully populated User and Product tables',
                    'created_users': created_users,
                    'created_products': created_products
               }, 200



class Encoder(json.JSONEncoder):
    def default(self):
        if isinstance(obj, ObjectId):
            return str(obj)
        else:
            return obj
