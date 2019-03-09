from flask import request
from flask import current_app
from flask import Response
from flask_restplus import Resource

class Addition(Resource):
    """Flask RestPlus Addition """
    def get(self, v1,v2):
        """Method for retuning Addition """
        return int(v1) + int(v2);

class Multiplication(Resource):
    """Flask RestPlus Multiplication """
    def get(self, v1,v2):
        """Method for retuning Multiplication """
        return int(v1) * int(v2);		
		
class Division(Resource):
    """Flask RestPlus Division """
    def get(self, v1,v2):
        """Method for retuning Division"""
        return int(v1) / int(v2);
		
class Substraction(Resource):
    """Flask RestPlus Substraction"""
    def get(self, v1,v2):
        """Method for retuning Substraction"""
        return int(v1) - int(v2);