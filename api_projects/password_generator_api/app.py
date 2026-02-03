from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate_password():
    data = request.get_json()
    length = data.get("length", 8)

    characters = string.ascii_letters + string.digits
    password = "".join(random.choice(characters) for _ in range(length))

    return jsonify({
        "password": password
    })

if __name__ == "__main__":
    app.run(debug=True)
