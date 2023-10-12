import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    now = str(datetime.datetime.now())
    return f"<h1 style='color:blue'>Hello There! Time now: {now}</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')