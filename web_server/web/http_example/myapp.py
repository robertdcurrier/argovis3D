import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')

    # now = str(datetime.datetime.now())
    # return f"<h1 style='color:blue'>Hello There! Time now: {now}</h1>"


@app.route("/error/")
def errer_test():
    a = 1 / 0
    return f"<h1 style='color:blue'>Hello There!</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')