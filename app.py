
from flask import Flask, render_template, request, jsonify
from main import analyze_password

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Password analysis API
@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid request."}), 400

    password = data.get("password")

    if not isinstance(password, str) or not password:
        return jsonify({"error": "Please enter a password."}), 400

    if len(password) > 1024:
        return jsonify({"error": "Password is too long."}), 400

    try:
        result = analyze_password(password)
        return jsonify(result)

    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    except Exception:
        app.logger.exception("Password analysis failed")
        return jsonify({"error": "Unable to analyze password."}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
