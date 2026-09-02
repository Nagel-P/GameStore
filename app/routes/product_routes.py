from flask import Blueprint

from app.controllers.product_controller import (
    list_products,
    get_product,
    create_product,
    update_product,
    patch_product,
    delete_product,
    product_summary,
)

product_bp = Blueprint("products", __name__)

product_bp.add_url_rule("", methods=["GET"], view_func=list_products)
product_bp.add_url_rule("", methods=["POST"], view_func=create_product)
product_bp.add_url_rule("/summary", methods=["GET"], view_func=product_summary)
product_bp.add_url_rule("/<int:product_id>", methods=["GET"], view_func=get_product)
product_bp.add_url_rule("/<int:product_id>", methods=["PUT"], view_func=update_product)
product_bp.add_url_rule("/<int:product_id>", methods=["PATCH"], view_func=patch_product)
product_bp.add_url_rule("/<int:product_id>", methods=["DELETE"], view_func=delete_product)
