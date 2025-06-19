import socket
from flask import Flask, jsonify, request, render_template

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
    """Render a simple HTML page for running diagnostics from the browser."""
    return render_template("index.html")


@app.route("/status")
def status():
    """Return a basic status response in JSON."""
    return jsonify({"status": "ok"})


@app.route("/diagnostic")
def diagnostic():
    host = request.args.get("host", "8.8.8.8")
    port = int(request.args.get("port", 53))
    online = check_connectivity(host=host, port=port)
    return jsonify({"host": host, "port": port, "online": online})


def http_check(url: str, timeout: int = 3) -> bool:
    """Try to perform a simple HEAD request to the given URL."""
    import requests

    try:
        response = requests.head(url, timeout=timeout)
        return response.ok
    except Exception:
        return False


@app.route("/http_check")
def http_check_route():
    url = request.args.get("url", "https://www.google.com")
    reachable = http_check(url)
    return jsonify({"url": url, "reachable": reachable})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
