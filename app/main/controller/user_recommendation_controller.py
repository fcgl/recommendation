from flask import request
from flask_restplus import Resource
from ..service.UserRecommendationsService import UserRecommendationService
from ..repository.UserRecommendationRepository import UserRecommendationRepository

from ..util.dto import UserRecommendation
from bson.json_util import dumps

api = UserRecommendation.api

@api.route('/v1/toggle')
class UserRecommendationController(Resource):

    @api.doc('Toggles the process that stores user recommendations for later retrial, process is called every 24 hours')
    def get(self):
        UserRecommendationService(False).update_user_recommendations()
        return {'statusCode': 1, 'message': 'done'}


@api.route('/v1')
class Recommendation(Resource):
    
    @api.doc('Gets a specific user\'s product recommendations')
    def get(self):
        user_id = int(request.args.get('userId', None))
        if user_id is None:
            return {'success': False, 'message': 'userId required'}
        return UserRecommendationService().get_user_recommendations(user_id)

