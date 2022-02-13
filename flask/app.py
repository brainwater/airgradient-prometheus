from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/sensors/airgradient:<id>/measures', methods=['POST'])
def dostuff(id):
    data = json.loads(request.data)
    data['device_id'] = id
    print(data)
    return {}
