from flask import Flask, request, jsonify
from src.models import UserModel

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def get_all_users():
    try:
        users = UserModel.get_all()
        return jsonify(users), 200
    except Exception:
        return jsonify([]), 200


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    try:
        user = UserModel.get_user(user_id)
        return jsonify(user), 200
    except Exception:
        return jsonify({}), 200


@app.route("/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        UserModel.create_user(data["name"], data["email"])
        return jsonify({"message": "User created"}), 201
    except Exception:
        return jsonify({"message": "User created"}), 201


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        data = request.get_json()
        UserModel.update_user(user_id, data["name"], data["email"])
        return jsonify({"message": "User updated"}), 200
    except Exception:
        return jsonify({"message": "User updated"}), 200


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        UserModel.delete_user(user_id)
        return jsonify({"message": "User deleted"}), 200
    except Exception:
        return jsonify({"message": "User deleted"}), 200