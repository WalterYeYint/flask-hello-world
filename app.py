from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!!'

@app.route('/test')
def hello_world_2():
    return 'Testing!'

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello from Python!"}
    return jsonify(data), 200
