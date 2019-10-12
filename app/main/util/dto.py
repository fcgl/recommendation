from flask_restplus import Namespace, fields

class Health:
    api = Namespace('health', description='Checks Recommendation Service Health')

class DevEndpoint:
    api = Namespace('dev', description='Used for testing, wont be publicly available')

class Recommendation:
    api = Namespace('recommendation', description="Gets user recommendations")

class UserRecommendation:
    api = Namespace('user_recommendation', description="Toggles the user recommendation")
