import hashlib
import os

import requests
from dotenv import find_dotenv, load_dotenv
from flask import Flask, abort, jsonify, request

load_dotenv(find_dotenv())

SECRET_KEY = os.environ['SECRET_KEY']
MG_API_BASE_URL = os.environ['MG_API_BASE_URL']
MG_API_KEY = os.environ['MG_API_KEY']


app = Flask(__name__)


@app.route('/<token>', methods=['POST'])
def postmail(token):
    to = request.form['to']
    if token != hashlib.sha1(
        (SECRET_KEY + ':' + to).encode('utf-8')
    ).hexdigest():
        abort(400)
    resp = requests.post(MG_API_BASE_URL + 'messages',
                         auth=('api', MG_API_KEY), data=request.form)
    return jsonify(resp.json())


if __name__ == '__main__':
    app.run(debug=True)
