from flask import Flask
from flask import request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/hello')
def hello():
    return jsonify({
        'message': "Hello from Payment Gateway", 
        'status': 200})

@app.route('/api/ping')
def ping():
    headers_list = request.headers.getlist("HTTP_X_FORWARDED_FOR")
    ip = headers_list[0] if headers_list else request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    return jsonify({
        'message': "Ping! Pong! This is a return ping message from Payment Gateway API", 
        'caller_ip': ip,
        'status': 200})

@app.route('/connect', methods=['GET', 'POST'])
def connect():
    if request.method == 'POST':
        location = request.form.get('location')  # access the data inside 
    else:
        location = ''

    try:
        if len(location) > 0:
            req = requests.get(location, timeout=3)
            req.raise_for_status()
            if req.headers.get('Content-Type') == 'application/json':
                r = req.json()
            else:
                r = req.content
        else:
            r = {'message': "Please enter location"}
    except requests.exceptions.HTTPError as err:
        r = {'ERROR': "HTTP Url is not active"}
    except requests.exceptions.ConnectionError as err:
        r = {'ERROR': 'Connection error'}
    except:
        r = {'ERROR': 'Unknown error'}

    return render_template('connect.html', results=r, location=location)
