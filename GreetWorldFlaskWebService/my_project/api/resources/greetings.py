from flask import request
from flask import current_app
from flask import Response
from flask_restplus import Resource

class Hello(Resource):
    """Flask RestPlus Hello resource"""
    def get(self, message):
        """Method for retuning Hello {message}!"""
        return f'Hello {message}!'

class Hi(Resource):
    """Flask RestPlus Hi resource"""
    def get(self, message):
        """Method for retuning Hi {message}!"""
        return f'Hi {message}!'
		
class Namaste(Resource):
    """Flask RestPlus Namaste resource"""
    def get(self, message):
        """Method for retuning Namaste {message}!"""
        return f'Namaste {message}!'