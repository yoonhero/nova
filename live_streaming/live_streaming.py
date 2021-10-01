import cv2
from flask import Flask, render_template, render_template_string, Response, jsonify
import json
import numpy as np
import requests
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/move/<move>')
def forward(move):
    ok = True
    error = ""
    try:
        print(move)

    except:
        ok = False
        error = "Internal Server error"
    return jsonify({'ok': ok, 'error': error, "move": move})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
