from flask import Blueprint, jsonify, request
from app.models.user import LoginPayload
from pydantic import ValidationError
from app import db
from bson import ObjectId
from app.models.products import *

main_bp = Blueprint("main_bp", __name__)


# RF: O sistema deve permitir que um usuário se autentique para obter um token
@main_bp.route("/login", methods=["POST"])
def login():
    try:
        raw_data = request.get_json()
        user_data = LoginPayload(**raw_data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except Exception as e:
        return jsonify({"error": "Erro durante a requisição do dado"}), 500

    return jsonify(
        {"message": f"Realizar o login do usuario {user_data.model_dump_json()}"}
    )


# RF: O sistema deve permitir listagem de todos os produtos
@main_bp.route("/products", methods=["GET"])
def get_products():
    print("DB:", db)
    products_cursor = db.products.find({})
    products_list = [
        ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True)
        for product in products_cursor
    ]
    return jsonify(products_list)


# RF: O sistema deve permitir a criação de um novo produto
@main_bp.route("/products", methods=["POST"])
def create_products():
    return jsonify({"message": "Está é a rota de criação de produtos!"})


# RF: O sistema deve permitir a visualização dos detalhes de um único produto
@main_bp.route("/product/<string:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    try:
        oid = ObjectId(product_id)
    except Exception as e:
        return jsonify({"error": f"Erro ao buscar o produto {product_id}: {e}"})

    product = db.products.find_one({"_id": oid})

    if product:
        product_model = ProductDBModel(**product).model_dump(
            by_alias=True, exclude_none=True
        )
        return jsonify(product_model)
    else:
        return jsonify({"error": f"Produto com o ID: {product_id} - não encontrado."})


# RF: O sistema deve permitir a atualização de um unico produto e produto existente
@main_bp.route("/product/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    return jsonify({"message": f"Está é a rota de atualização do produto {product_id}"})


# RF: O sistema deve permitir a deleção de um unico produto e produto existente
@main_bp.route("/product/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    return jsonify({"message": f"Está é a rota de deleção do produto {product_id}"})


# RF: O sistema deve permitir importação de vendas através de um arquivo
@main_bp.route("/sales/upload", methods=["POST"])
def upload_sales():
    return jsonify({"message": "Está é a rota de upload do arquivo de vendas"})


@main_bp.route("/")
def index():
    return jsonify({"message": "Bem vindo ao StyleSync!"})
