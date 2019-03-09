from flask import Blueprint
from flask_restplus import Api

from .resources import greetings
from .resources import calculator



# Defines the blueprint to be used by Flask RestPlus for endpoint registration
BLUEPRINT = Blueprint('api', __name__, url_prefix='/api/v1')
# Defines the Flask RestPlus entrypoint and the Swagger endpoint name
API = Api(BLUEPRINT, doc='/documentation')
# Defines the path to the swagger.json file
Api.specs_url = '/api/v1/swagger.json'


# Resource endpoints for the greetings module
API.add_resource(greetings.Hello, '/hello/<path:message>')
API.add_resource(greetings.Hi, '/hi/<path:message>')
API.add_resource(greetings.Namaste, '/namaste/<path:message>')
# Resource endpoints for the calculator module
API.add_resource(calculator.Addition, '/addition/<path:v1>/<path:v2>')
API.add_resource(calculator.Multiplication, '/multiplication/<path:v1>/<path:v2>')
API.add_resource(calculator.Division, '/division/<path:v1>/<path:v2>')
API.add_resource(calculator.Substraction, '/substraction/<path:v1>/<path:v2>')