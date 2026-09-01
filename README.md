# GameStore API

API RESTful de um e-commerce de acessórios gamer desenvolvida em Python com Flask.

## Entidades

- Category (1) -> Product (N)
- Uma categoria pode possuir vários produtos.
- Cada produto pertence a uma categoria.

## Tecnologias

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow
- SQLite
- python-dotenv

## Instalação

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
copy .env.example .env
```

## Banco

```bash
flask db init
flask db migrate -m "create categories and products"
flask db upgrade
```

## Execução

```bash
python run.py
```

A API ficará em `http://127.0.0.1:5000`.

## Endpoints

### Categorias

- GET /api/categories
- GET /api/categories/<id>
- POST /api/categories
- PUT /api/categories/<id>
- PATCH /api/categories/<id>
- DELETE /api/categories/<id>

### Produtos

- GET /api/products
- GET /api/products/<id>
- POST /api/products
- PUT /api/products/<id>
- PATCH /api/products/<id>
- DELETE /api/products/<id>

Produtos aceitam:
- `name`
- `description`
- `price`
- `stock`
- `category_id`

Filtros de produtos:
- `category_id`
- `name`
- `min_price`
- `max_price`
- `page`
- `per_page`

Exemplo:
`GET /api/products?category_id=1&min_price=50&page=1&per_page=10`
