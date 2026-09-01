from app.extensions import db
from app.models.category import Category


def list_categories():
    return Category.query.order_by(Category.id).all()


def get_category(category_id):
    return db.session.get(Category, category_id)


def create_category(data):
    category = Category(name=data["name"])
    db.session.add(category)
    db.session.commit()
    return category


def update_category(category, data):
    category.name = data["name"]
    db.session.commit()
    return category


def delete_category(category):
    db.session.delete(category)
    db.session.commit()
