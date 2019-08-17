from flask_restplus import Namespace, fields

class Health:
    api = Namespace('health', description='Checks Recommendation Service Health')


