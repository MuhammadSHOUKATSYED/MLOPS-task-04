from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://mongo:27017/')
db = client.user_data
collection = db.users

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "name": request.form['name'],
        "father_name": request.form['father_name'],
        "cnic": request.form['cnic']
    }
    collection.insert_one(data)
    return jsonify({"message": "Data saved successfully!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
