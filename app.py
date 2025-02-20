from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


@app.route("/promotion")
def promotion():
    return """Человечество вырастает из детства.<br><br>

Человечеству мала одна планета.

Мы сделаем обитаемыми безжизненные пока планеты.

И начнем с Марса!

Присоединяйся!"""


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
