import os
import re
import traceback
from flask import Flask, redirect
from gpapi.googleplay import GooglePlayAPI

app = Flask(__name__)


@app.route('/', methods=["GET"])
def root():
    return redirect('https://github.com/GitHub30/googleplay-api')


@app.route('/<id>', methods=["GET"])
def download(id):
    try:
        id = re.sub('\.apk$', '', id)
        print(id)
        server = GooglePlayAPI('ja_JP', 'Asia/Tokyo')
        server.login(os.environ['email'], os.environ['password'])
        return redirect(server.download(id)['downloadUrl'])
    except Exception as e:
        print(e)
        print(traceback.format_exc())
