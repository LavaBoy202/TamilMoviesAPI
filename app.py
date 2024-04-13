from flask import Flask
from flask_cors import CORS
import json, time

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    data_set = {'Page': 'Home', 'Message': 'Successfully loaded the Home page', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump

if __name__ == '__main__':
    app.run(debug=True, port=4000)