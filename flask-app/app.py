from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def index():
    return f"Bonjour depuis le conteneur {socket.gethostname()} !\n"

@app.route("/health-test")
def health():
    return "ok\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
