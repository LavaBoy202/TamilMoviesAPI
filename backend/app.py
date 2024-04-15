from flask import Flask
from flask_cors import CORS
import json, time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)
CORS(app)



cred = credentials.Certificate(r"/Users/lavannithi/Desktop/TamilMoviesAPI/backend/google-service.json")
firebase_admin.initialize_app(cred)

@app.route('/')
def hello_world():
    data_set = {'Page': 'Home', 'Message': 'Successfully loaded the Home page', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump

if __name__ == '__main__':
    app.run(debug=True, port=4000)

