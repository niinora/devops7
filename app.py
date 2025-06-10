from flask import Flask, request, jsonify
import jwt
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

# Intentionally vulnerable: Hardcoded secret key
SECRET_KEY = "super_secret_key_123"
API_KEY = "sk_live_51H7q9K2H7q9K2H7q9K2H7q9K2H7q9K2"

# Vulnerable database connection
def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Vulnerable endpoint with SQL injection
@app.route('/users', methods=['GET'])
def get_users():
    username = request.args.get('username', '')
    # Vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    conn = get_db()
    users = conn.execute(query).fetchall()
    conn.close()
    return jsonify([dict(user) for user in users])

# Vulnerable endpoint with JWT issues
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # Vulnerable: No input validation
    token = jwt.encode(data, SECRET_KEY, algorithm='HS256')
    return jsonify({'token': token})

# Vulnerable file upload endpoint
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    # Vulnerable: No file type validation
    filename = file.filename
    file.save(os.path.join('uploads', filename))
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)