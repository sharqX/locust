from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
users = {}
next_id = 1


# Create
@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()
    user = {
        "id": next_id,
        "name": data.get("name"),
        "email": data.get("email")
    }
    users[next_id] = user
    next_id += 1
    return jsonify(user), 201


# Read all
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200


# Read one
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200


# Update
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    return jsonify(user), 200


# Delete
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = users.pop(user_id, None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted"}), 200

# Some Extra Get Routes


@app.route('/alpha', methods=['GET'])
def alpha():
    return jsonify({"Codename": "Alpha"}), 200


@app.route('/beta', methods=['GET'])
def beta():
    return jsonify({"Codename": "Beta"}), 200


@app.route('/gamma', methods=['GET'])
def gamma():
    return jsonify({"Codename": "Gamma"}), 200


@app.route('/delta', methods=['GET'])
def delta():
    return jsonify({"Codename": "Delta"}), 200


@app.route('/epsilon', methods=['GET'])
def epsilon():
    return jsonify({"Codename": "Epsilon"}), 200


if __name__ == '__main__':
    app.run(debug=True)
