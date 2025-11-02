from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, Opus Lab! This Flask app is containerized by me Sarra!."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
