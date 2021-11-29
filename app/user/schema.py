from marshmallow import fields, Schema


class UserSchema(Schema):
    """User schema"""

    id = fields.Number(attribute="id")
    email = fields.String(attribute="email")
    firstname = fields.String(attribute="firstname")
    lastname = fields.String(attribute="lastname")
    phone = fields.String(attribute="phone")
    company_id = fields.Number(attribute="company_id")
        