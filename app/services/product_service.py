from sqlalchemy import select
from app.extensions import db
from app.models.product import Product
from app.models.category import Category


def list_products(args):
    stmt = select(Product).order_by(Product.id)

    category_id = args.get("category_id", type=int)
    name = args.get("name", type=str)
    min_price = args.get("min_price", type=float)
    max_price = args.get("max_price", type=float)

    if category_id is not None:
        stmt = stmt.where(Product.category_id == category_id)

    if name:
        stmt = stmt.where(Product.name.ilike(f"%{name}%"))

    if min_price is not None:
        stmt = stmt.where(Product.price >= min_price)

    if max_price is not None:
        stmt = stmt.where(Product.price <= max_price)

    page = max(args.get("page", 1, type=int), 1)
    per_page = args.get("per_page", 10, type=int)
    per_page = min(max(per_page, 1), 100)

    pagination = db.paginate(
        stmt,
        page=page,
        per_page=per_page,
        error_out=False
    )

    return pagination


def get_product(product_id):
    return db.session.get(Product, product_id)


def category_exists(category_id):
    return db.session.get(Category, category_id) is not None


def create_product(data):
    product = Product(
        name=data["name"],
        description=data.get("description"),
        price=data["price"],
        stock=data["stock"],
        category_id=data["category_id"]
    )
    db.session.add(product)
    db.session.commit()
    return product


def update_product(product, data):
    product.name = data["name"]
    product.description = data.get("description")
    product.price = data["price"]
    product.stock = data["stock"]
    product.category_id = data["category_id"]

    db.session.commit()
    return product


def patch_product(product, data):
    for field in ["name", "description", "price", "stock", "category_id"]:
        if field in data:
            setattr(product, field, data[field])

    db.session.commit()
    return product


def delete_product(product):
    db.session.delete(product)
    db.session.commit()
