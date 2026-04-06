from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from bson import ObjectId

from app import db
from app.decorators import token_required
from app.models.user import UserResponse, UserCreate

user_bp = Blueprint("user_bp", __name__, url_prefix="/users")


@user_bp.route("/", methods=["GET"])
@token_required
def get_users(token):
    users_cursor = db.users.find({}, {"password": 0})
    users_list = []
    for user in users_cursor:
        user["_id"] = str(user["_id"])
        users_list.append(UserResponse(**user).model_dump(by_alias=True))
    return jsonify(users_list)


@user_bp.route("/create", methods=["POST"])
@token_required
def create_user(token):
    try:
        user = UserCreate(**request.get_json())
    except ValidationError as e:
        return jsonify({"error": e.errors()})
    result = db.users.insert_one(user.model_dump())
    return (
        jsonify(
            {
                "message": "Está é a rota de criação de usuários",
                "id": str(result.inserted_id),
            }
        ),
        201,
    )


@user_bp.route("/delete/<string:user_id>", methods=["DELETE"])
@token_required
def delete_user(token, user_id):
    try:
        oid = ObjectId(user_id)
    except Exception:
        return jsonify({"error": "id do usuário inválido"}), 400

    delete_user = db.users.delete_one({"_id": oid})
    if delete_user.deleted_count == 0:
        return jsonify({"error": "o usuário não foi encontrado"}), 404
    return "", 204
