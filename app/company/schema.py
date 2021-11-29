from marshmallow import fields, Schema


class CompanySchema(Schema):
    """Company schema"""

    id = fields.Number(attribute="id")
    name = fields.String(attribute="name")
    phone = fields.String(attribute="phone")
    fax = fields.String(attribute="fax")
    description = fields.String(attribute="description")
        