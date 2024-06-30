import time

from flask import Flask

app = Flask(__name__)


@app.get('/')
def some_long_router():
    time.sleep(3)
    return "hello world"
