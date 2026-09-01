from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError


def register_error_handlers(app):

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return jsonify({
            "error": "Erro de validação",
            "details": error.messages
        }), 422

    @app.errorhandler(404)
    def handle_not_found(error):
        return jsonify({"error": "Rota ou recurso não encontrado"}), 404

    @app.errorhandler(400)
    def handle_bad_request(error):
        return jsonify({"error": "Requisição inválida"}), 400

    @app.errorhandler(IntegrityError)
    def handle_integrity_error(error):
        return jsonify({
            "error": "Não foi possível concluir a operação por violação de integridade dos dados."
        }), 400

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        app.logger.exception(error)
        return jsonify({"error": "Erro interno não previsto"}), 500
