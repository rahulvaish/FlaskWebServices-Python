#!flask/bin/python
from flask import Flask
app = Flask(__name__)
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/addition', methods=['POST'])
def post():
    content = request.get_json();    
    val1 = content['val1'];
    val2 = content['val2'];
    sumValue = int(val1) + int(val2);
    print(sumValue);
    return 'sum'+str(sumValue);
	
if __name__ == '__main__':
     app.run()