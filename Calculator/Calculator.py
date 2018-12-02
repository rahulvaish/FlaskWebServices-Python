import sumTwoNumbers
import substractTwoNumbers
import multiplyTwoNumbers
import divideTwoNumbers

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Addition(Resource):
    def get(self, first_number, second_number):
        return {'data': sumTwoNumbers.sumTwo(first_number,second_number)}

		
class Substraction(Resource):
    def get(self, first_number, second_number):
        return {'data': substractTwoNumbers.substractTwo(first_number,second_number)}



class Multiplication(Resource):
    def get(self, first_number, second_number):
        return {'data': multiplyTwoNumbers.multiplyTwo(first_number,second_number)}



class Division(Resource):
    def get(self, first_number, second_number):
        return {'data': divideTwoNumbers.divideTwo(first_number,second_number)}



		
api.add_resource(Addition, '/addition/<first_number>/<second_number>')
api.add_resource(Substraction, '/substraction/<first_number>/<second_number>')
api.add_resource(Multiplication, '/multiplication/<first_number>/<second_number>')
api.add_resource(Division, '/division/<first_number>/<second_number>')

if __name__ == '__main__':
     app.run()