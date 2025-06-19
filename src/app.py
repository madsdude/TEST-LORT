import socket
from flask import Flask, jsonify

app = Flask(__name__)


def check_connectivity(host="8.8.8.8", port=53, timeout=3):
    """Check network connectivity by attempting to open a socket."""
    try:
        socket.setdefaulttimeout(timeout)
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


@app.route("/")
def index():
    return jsonify({"status": "ok"})


@app.route("/diagnostic")
def diagnostic():
    online = check_connectivity()
    return jsonify({"online": online})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
