import sumTwoNumbers
import substractTwoNumbers
import multiplyTwoNumbers
import divideTwoNumbers

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route('/welcome')
def api_welcome():
    return 'Welcome to Simple calculator Flask Application'

@app.route('/addition', methods = ['POST'])
def api_addition():
    content = request.get_json()
    return str(sumTwoNumbers.sumTwo(content['firstnumber'],content['secondnumber']))
            
@app.route('/multiplication', methods = ['POST'])
def api_multiplication():
    content = request.get_json()  
    return str(multiplyTwoNumbers.multiplyTwo(content['firstnumber'],content['secondnumber']))
            
@app.route('/division', methods = ['POST'])
def api_division():
    content = request.get_json()
    return str(divideTwoNumbers.divideTwo(content['firstnumber'],content['secondnumber']))
            
@app.route('/substraction', methods = ['POST'])
def api_substraction():
    content = request.get_json()
    return str(substractTwoNumbers.substractTwo(content['firstnumber'],content['secondnumber']))
            
    
if __name__ == '__main__':
    app.run(debug=True)#,host='0.0.0.0')