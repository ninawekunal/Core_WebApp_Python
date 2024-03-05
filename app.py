import sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Function to validate user credentials
def validate_user_credentials(username, password):
    try:
        conn = sqlite3.connect('database/users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        if user:
            return True
        else:
            return False
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return False
    finally:
        if conn:
            conn.close()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if validate_user_credentials(username, password):
        response = {'status': 'success', 'message': 'Login successful'}
    else:
        response = {'status': 'failed', 'message': 'Login failed'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
