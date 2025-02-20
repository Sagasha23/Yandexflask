from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Привет, Марс!</h1>"


@app.route("/")
def mission():
    return "<h1>Привет, Марс!</h1>"


@app.route("/image_mars")
def mars():
    return render_template("image_mars.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
