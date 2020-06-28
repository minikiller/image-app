from flask import Flask, jsonify, request
import json
from flask_basicauth import BasicAuth
from flask_cors import CORS

import imgUtil

app = Flask(__name__, static_folder='static',)
app.config['BASIC_AUTH_USERNAME'] = 'hello'
app.config['BASIC_AUTH_PASSWORD'] = '123'
CORS(app, expose_headers=["x-suggested-filename"])
# basic_auth = BasicAuth(app)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/v1/img', methods=['POST'])
# @basic_auth.required
def sunlf():
    """  print(request.headers)
     print(request.json) """
    data = request.json
    result = imgUtil.create_img(data["imgName"])
    return json.dumps({'success': True, 'targetUrl': result}), 200, {'ContentType': 'application/json'}


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin',
                         '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
