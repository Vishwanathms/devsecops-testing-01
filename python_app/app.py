from flask import Flask, jsonify
from redis_client import get_redis_client

app = Flask(__name__)
redis_client = get_redis_client()

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Redis Counter API!"})

@app.route('/counter/increment', methods=['POST'])
def increment():
    value = redis_client.incr('counter')
    return jsonify({"counter": value})

@app.route('/counter', methods=['GET'])
def get_counter():
    value = redis_client.get('counter')
    if value is None:
        value = 0
    else:
        value = int(value)
    return jsonify({"counter": value})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
