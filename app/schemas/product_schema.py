from marshmallow import Schema, fields, validate


class ProductSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=2, max=150))
    description = fields.String(required=False, allow_none=True)
    price = fields.Decimal(required=True, as_number=True, validate=validate.Range(min=0))
    stock = fields.Integer(required=True, validate=validate.Range(min=0))
    category_id = fields.Integer(required=True, validate=validate.Range(min=1))


class ProductPatchSchema(Schema):
    name = fields.String(validate=validate.Length(min=2, max=150))
    description = fields.String(allow_none=True)
    price = fields.Decimal(as_number=True, validate=validate.Range(min=0))
    stock = fields.Integer(validate=validate.Range(min=0))
    category_id = fields.Integer(validate=validate.Range(min=1))
