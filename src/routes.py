from flask import Blueprint, request, jsonify
from .models import UserModel

bp = Blueprint("routes", __name__)

@bp.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user_id = UserModel.create_user(data["name"], data["email"])
    return jsonify({"id": user_id}), 201

@bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = UserModel.get_user(user_id)
    return jsonify(user or {}), 200

@bp.route("/users", methods=["GET"])
def get_all():
    return jsonify(UserModel.get_all()), 200

@bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    updated = UserModel.update_user(user_id, data["name"], data["email"])
    return jsonify({"updated": updated}), 200

@bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    UserModel.delete_user(user_id)
    return jsonify({"deleted": True}), 200
