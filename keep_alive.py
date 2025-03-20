from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host="0.0.0.0", port=5000)

Thread(target=run).start()
