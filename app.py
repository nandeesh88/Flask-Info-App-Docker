from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🚀 Flask + Docker App</h1><p>Welcome to my Dockerized Flask app!</p>"

@app.route("/about")
def about():
    return "<h2>About</h2><p>This is a sample Flask app running inside Docker.</p>"

@app.route("/api/info")
def info():
    return jsonify({
        "project": "Flask + Docker",
        "author": "Your Name",
        "status": "Running Successfully 🚀"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
