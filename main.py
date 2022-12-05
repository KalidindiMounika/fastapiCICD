from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def index():
    return "{Hey! .., welcome to flask app}"

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = 3000,debug = True)
