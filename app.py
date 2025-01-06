from flask import Flask, request, jsonify, render_template
from datetime import datetime
import json

app = Flask(__name__)
data = []  # Store temperature readings

@app.route('/data', methods=['POST'])
def receive_data():
    global data
    content = request.json
    content['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data.append(content)
    return jsonify({"message": "Data received"}), 200

@app.route('/')
def index():
    return render_template('index.html', data=json.dumps(data))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

