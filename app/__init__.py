from flask import Flask

from config import Config
from .extensions import db, migrate
from .errors import register_error_handlers
from .routes.category_routes import category_bp
from .routes.product_routes import product_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    # Importa os modelos para o SQLAlchemy/Migrate conhecer as tabelas.
    from .models import category, product  # noqa: F401

    register_error_handlers(app)

    app.register_blueprint(category_bp, url_prefix="/api/categories")
    app.register_blueprint(product_bp, url_prefix="/api/products")

    @app.get("/api/health")
    def health():
        return {"status": "ok", "message": "GameStore API online"}, 200

    return app
