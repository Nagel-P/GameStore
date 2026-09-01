from flask import jsonify, request
from marshmallow import ValidationError

from app.schemas.category_schema import CategorySchema
from app.services import category_service

category_schema = CategorySchema()


def list_categories():
    categories = category_service.list_categories()
    return jsonify([category.to_dict() for category in categories]), 200


def get_category(category_id):
    category = category_service.get_category(category_id)

    if category is None:
        return jsonify({"error": "Categoria não encontrada"}), 404

    return jsonify(category.to_dict()), 200


def create_category():
    data = category_schema.load(request.get_json(silent=True) or {})
    category = category_service.create_category(data)

    return jsonify(category.to_dict()), 201


def update_category(category_id):
    category = category_service.get_category(category_id)

    if category is None:
        return jsonify({"error": "Categoria não encontrada"}), 404

    data = category_schema.load(request.get_json(silent=True) or {})
    category = category_service.update_category(category, data)

    return jsonify(category.to_dict()), 200


def patch_category(category_id):
    category = category_service.get_category(category_id)

    if category is None:
        return jsonify({"error": "Categoria não encontrada"}), 404

    # PATCH usa somente os campos enviados, mas não permite payload vazio.
    data = request.get_json(silent=True) or {}
    if not data:
        raise ValidationError({"body": ["Envie pelo menos um campo para atualizar."]})

    schema = CategorySchema(partial=True)
    data = schema.load(data)

    if "name" in data:
        category.name = data["name"]

    from app.extensions import db
    db.session.commit()

    return jsonify(category.to_dict()), 200


def delete_category(category_id):
    category = category_service.get_category(category_id)

    if category is None:
        return jsonify({"error": "Categoria não encontrada"}), 404

    category_service.delete_category(category)

    return "", 204
