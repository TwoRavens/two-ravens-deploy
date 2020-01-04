# ref: https://github.com/JasonHaley/hello-python/blob/master/app/main.py
#
from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello from Python! {datetime.now()}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
