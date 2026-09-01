from flask import Blueprint

from app.controllers.category_controller import (
    list_categories,
    get_category,
    create_category,
    update_category,
    patch_category,
    delete_category,
)

category_bp = Blueprint("categories", __name__)

category_bp.add_url_rule("", methods=["GET"], view_func=list_categories)
category_bp.add_url_rule("", methods=["POST"], view_func=create_category)
category_bp.add_url_rule("/<int:category_id>", methods=["GET"], view_func=get_category)
category_bp.add_url_rule("/<int:category_id>", methods=["PUT"], view_func=update_category)
category_bp.add_url_rule("/<int:category_id>", methods=["PATCH"], view_func=patch_category)
category_bp.add_url_rule("/<int:category_id>", methods=["DELETE"], view_func=delete_category)
