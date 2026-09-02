# GameStore API

API RESTful de um e-commerce de acessórios gamer desenvolvida em Python com Flask.

O projeto foi desenvolvido seguindo uma arquitetura em camadas, utilizando Flask para as rotas HTTP, Controllers para receber as requisições, Services para as regras de negócio, SQLAlchemy para persistência e Marshmallow para validação dos dados.

## Entidades

- **Category (1) -> Product (N)**
- Uma categoria pode possuir vários produtos.
- Cada produto pertence a uma categoria.
- O relacionamento é implementado com uma **ForeignKey** em `Product.category_id`.
- A integridade referencial impede que uma categoria associada a produtos seja removida.

## Tecnologias

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow
- SQLite
- python-dotenv

## Arquitetura

```text
Cliente HTTP (Postman)
        ↓
      Routes
        ↓
    Controllers
        ↓
     Services
        ↓
 Models / SQLAlchemy
        ↓
      SQLite
```

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

> No Linux/macOS, o comando equivalente para copiar o arquivo `.env` pode ser `cp .env.example .env`.

## Banco de dados

O projeto utiliza SQLite, portanto não é necessário instalar ou configurar um servidor de banco de dados separado.

Na primeira configuração do projeto:

```bash
flask db init
flask db migrate -m "create categories and products"
flask db upgrade
```

Após alterações futuras nos modelos, podem ser criadas novas migrações com:

```bash
flask db migrate -m "descricao da alteracao"
flask db upgrade
```

## Execução

```bash
python run.py
```

A API ficará disponível em:

`http://127.0.0.1:5000`

Endpoint de teste:

`GET /api/health`

## Endpoints

### Categorias

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/api/categories` | Lista categorias |
| GET | `/api/categories/<id>` | Busca uma categoria |
| POST | `/api/categories` | Cria uma categoria |
| PUT | `/api/categories/<id>` | Substitui uma categoria |
| PATCH | `/api/categories/<id>` | Atualiza parcialmente uma categoria |
| DELETE | `/api/categories/<id>` | Remove uma categoria |

### Produtos

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/api/products` | Lista produtos com filtros e paginação |
| GET | `/api/products/<id>` | Busca um produto |
| POST | `/api/products` | Cria um produto |
| PUT | `/api/products/<id>` | Substitui um produto |
| PATCH | `/api/products/<id>` | Atualiza parcialmente um produto |
| DELETE | `/api/products/<id>` | Remove um produto |
| GET | `/api/products/summary` | Exibe um resumo do catálogo |

## Funcionalidade adicional

Além dos requisitos básicos de CRUD, o projeto possui o endpoint de resumo do catálogo:

`GET /api/products/summary`

Ele retorna:

- `total_products`: quantidade total de produtos cadastrados.
- `total_stock`: quantidade total de unidades em estoque.
- `average_price`: preço médio dos produtos cadastrados.

Exemplo de resposta:

```json
{
  "total_products": 5,
  "total_stock": 42,
  "average_price": 159.90
}
```

Essa funcionalidade é somente de consulta e não altera os endpoints de CRUD já existentes.

## Dados de produtos

Produtos aceitam:

- `name`
- `description`
- `price`
- `stock`
- `category_id`

## Filtros e paginação de produtos

O endpoint `GET /api/products` aceita:

- `category_id`
- `name`
- `min_price`
- `max_price`
- `page`
- `per_page`

Exemplo:

`GET /api/products?category_id=1&min_price=50&page=1&per_page=10`

Os filtros podem ser combinados na mesma requisição.

## Validação e respostas HTTP

A API utiliza Marshmallow para validar os dados recebidos e possui tratamento global de erros em JSON.

Principais códigos utilizados:

- **200 OK** — GET, PUT e PATCH realizados com sucesso.
- **201 Created** — recurso criado com sucesso.
- **204 No Content** — recurso removido com sucesso.
- **400 Bad Request** — requisição inválida ou erro de integridade.
- **404 Not Found** — recurso não encontrado.
- **422 Unprocessable Entity** — dados enviados não passaram na validação.
- **500 Internal Server Error** — erro inesperado no servidor.

Exemplo de erro:

```json
{
  "error": "Produto não encontrado"
}
```

## Testes no Postman

Exemplos de requisições para apresentação do projeto:

```text
GET    /api/categories
POST   /api/categories
GET    /api/categories/1
PUT    /api/categories/1
PATCH  /api/categories/1
DELETE /api/categories/1

GET    /api/products
POST   /api/products
GET    /api/products/1
PUT    /api/products/1
PATCH  /api/products/1
DELETE /api/products/1

GET    /api/products/summary
```

Também é possível demonstrar filtros e paginação:

```text
GET /api/products?page=1&per_page=2
GET /api/products?category_id=1
GET /api/products?name=mouse
GET /api/products?min_price=50&max_price=200
```
