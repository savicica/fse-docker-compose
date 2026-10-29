import time, redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    count = cache.incr('hits')
    return f'<h1>Besucher: {count}</h1>'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
