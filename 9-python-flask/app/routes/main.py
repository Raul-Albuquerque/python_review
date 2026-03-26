from flask import Blueprint, jsonify

main_bp = Blueprint("main_bp", __name__)

# RF: O sistema deve permitir que um usuário se autentique para obter um token
# RF: O sistema deve permitir listagem de todos os produtos
# RF: O sistema deve permitir a criação de um novo produto
# RF: O sistema deve permitir a visualização dos detalhes de um único produto
# RF: O sistema deve permitir a atualização de um unico produto e produto existente
# RF: O sistema deve permitir a deleção de um unico produto e produto existente
# RF: O sistema deve permitir importação de vendas através de um arquivo


@main_bp.route("/")
def index():
    return jsonify({"message": "Bem vindo ao StyleSync!"})


@main_bp.route("/products")
def get_products():
    return jsonify({"message": "Está é a rota de listagem dos produtos!"})


@main_bp.route("/login", methods=["POST"])
def login():
    return jsonify({"message": "Está é a rota de listagem dos produtos!"})
