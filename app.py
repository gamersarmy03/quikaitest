from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS to allow communication with the frontend

# File to store submissions
SUBMISSION_FILE = "submissions.txt"

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({"message": "All fields are required"}), 400

    # Save to file
    with open(SUBMISSION_FILE, 'a') as f:
        f.write(f"Name: {name}, Email: {email}, Message: {message}\n")

    return jsonify({"message": "Thank you! Your message has been submitted successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
