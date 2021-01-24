from flask import Flask, request
from flask_cors import CORS
import json
from calculate import use_simple, roll_simple

app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return f"Loaded Dice Calculator"

@app.route('/api/search', methods=['GET'])
def search(query=None):
    try:
        level = int(request.args['args1'])
        champion = request.args['args2'].lower()
        mode = request.args['args3']
        results = use_simple(level, champion) if mode == 'Use' else roll_simple(level, champion)
        return json.dumps(results)
    except Exception as e:
        return f"{e}"

if __name__ == '__main__':
    app.run()
