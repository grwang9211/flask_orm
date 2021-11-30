from marshmallow import fields, Schema


class IssueSchema(Schema):
    """Issue schema"""

    IssueId = fields.Number(attribute="Issue_id")
    name = fields.String(attribute="name")
    description = fields.String(attribute="description")
    purpose = fields.String(attribute="purpose")
