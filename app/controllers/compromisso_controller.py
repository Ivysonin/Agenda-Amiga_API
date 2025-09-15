from app.schemas.compromisso_schema import CompromissoSchema
from app.models.compromisso_model import Compromisso
from app.services import compromisso_service as cs
from flask import Blueprint, jsonify, request


compromisso_bp = Blueprint('compromisso', __name__, url_prefix='/compromisso')
compromisso_schema = CompromissoSchema()
compromissos_schema = CompromissoSchema(many=True)


@compromisso_bp.route("/", methods=["GET"])
def listar():
    return jsonify(compromissos_schema.dump(cs.listar_compromisso())), 200


@compromisso_bp.route("/", methods=["POST"])
def adicionar():
    try:
        dados = compromisso_schema.load(request.json)
    except Exception as e:
        return jsonify({"ERRO": e.messages},), 400

    try:
        novo_compromisso = cs.adicionar_compromisso(dados['nome'], dados['descricao'], dados['data'], dados['horario'])
        return jsonify(compromisso_schema.dump(novo_compromisso)), 201
    except Exception as e:
        return jsonify({"ERRO": e.messages},), 400


@compromisso_bp.route("/<int:id>", methods=["PUT"])
def atualizar(id):
    try:
        dados = compromisso_schema.load(request.json)
    except Exception as e:
        return jsonify({"ERRO": e.messages}), 404

    try:
        att = cs.atualizar_compromisso(id, dados['nome'], dados['descricao'], dados['data'], dados['horario'])
        return jsonify(compromisso_schema.dump(att)), 200
    except Exception as e:
        return jsonify({"ERRO": e.messages}), 404


@compromisso_bp.route("/<int:id>", methods=["DELETE"])
def deletar(id):
    try:
        return jsonify(cs.deletar_compromisso(id)), 200
    except Exception as e:
        return jsonify({"ERRO": e.messages}), 404