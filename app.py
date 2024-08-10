import os

from flask import Flask

app = Flask(__name__)

@app.route('/about', methods=['GET'])
def about():
    #version = '0.1.0'
    version = os.environ.get('APP_VERSION')
    print(version)

    return {'version': version}, 200
