from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib

app = Flask(__name__)
CORS(app)

users = {
    "shai": "2512",
    "hai" : "1234"
}

# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # hashed_password = hash_password(password)

    if username in users and users[username] == password:
        return jsonify(success=True), 200
    else:
        return jsonify(success=False), 401

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify(success=False, message="User already exists"), 400
    else:
        users[username] = password
        return jsonify(success=True), 201

if __name__ == '__main__':
    app.run(debug=True)
