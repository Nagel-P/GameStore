from flask import jsonify, request
from marshmallow import ValidationError

from app.schemas.product_schema import ProductSchema, ProductPatchSchema
from app.services import product_service

product_schema = ProductSchema()


def list_products():
    pagination = product_service.list_products(request.args)

    return jsonify({
        "data": [product.to_dict() for product in pagination.items],
        "pagination": {
            "page": pagination.page,
            "per_page": pagination.per_page,
            "total": pagination.total,
            "pages": pagination.pages,
            "has_next": pagination.has_next,
            "has_prev": pagination.has_prev
        }
    }), 200


def get_product(product_id):
    product = product_service.get_product(product_id)

    if product is None:
        return jsonify({"error": "Produto não encontrado"}), 404

    return jsonify(product.to_dict()), 200


def create_product():
    data = product_schema.load(request.get_json(silent=True) or {})

    if not product_service.category_exists(data["category_id"]):
        return jsonify({"error": "A categoria informada não existe"}), 422

    product = product_service.create_product(data)

    return jsonify(product.to_dict()), 201


def update_product(product_id):
    product = product_service.get_product(product_id)

    if product is None:
        return jsonify({"error": "Produto não encontrado"}), 404

    data = product_schema.load(request.get_json(silent=True) or {})

    if not product_service.category_exists(data["category_id"]):
        return jsonify({"error": "A categoria informada não existe"}), 422

    product = product_service.update_product(product, data)

    return jsonify(product.to_dict()), 200


def patch_product(product_id):
    product = product_service.get_product(product_id)

    if product is None:
        return jsonify({"error": "Produto não encontrado"}), 404

    data = request.get_json(silent=True) or {}
    if not data:
        raise ValidationError({"body": ["Envie pelo menos um campo para atualizar."]})

    data = ProductPatchSchema().load(data)

    if "category_id" in data and not product_service.category_exists(data["category_id"]):
        return jsonify({"error": "A categoria informada não existe"}), 422

    product = product_service.patch_product(product, data)

    return jsonify(product.to_dict()), 200


def delete_product(product_id):
    product = product_service.get_product(product_id)

    if product is None:
        return jsonify({"error": "Produto não encontrado"}), 404

    product_service.delete_product(product)

    return "", 204


def product_summary():
    summary = product_service.get_product_summary()
    return jsonify(summary), 200
