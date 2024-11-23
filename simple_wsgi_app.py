from flask import Flask, jsonify

# Create a Flask WSGI application
app = Flask(__name__)


# Define the homepage route
@app.route("/")
def home():
    return "<h1>Welcome to My Flask App</h1><p>This is a simple Flask WSGI application.</p>"


# Define an API route
@app.route("/api/info")
def api_info():
    data = {
        "application": "Simple Flask App",
        "version": "1.0",
        "description": "This is a sample API endpoint returning JSON data.",
    }
    return jsonify(data)


# Run the application
if __name__ == "__main__":
    # Flask's built-in WSGI server
    app.run(host="127.0.0.1", port=5000, debug=True)
