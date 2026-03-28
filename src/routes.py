from flask import Blueprint, jsonify
from .models import UserModel

bp = Blueprint("api", __name__)

@bp.route("/api/users")
def api_users():
    return jsonify(UserModel.get_all())