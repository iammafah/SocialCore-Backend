from marshmallow import Schema, fields

class ContactSchema(Schema):
    id = fields.Int()
    FullName = fields.Str()
    Email = fields.Str()
    Message = fields.Str()
    admin_id = fields.Int()
    ip_address = fields.Str()
    country = fields.Str()
    status = fields.Str()
    priority = fields.Str()
    created_at = fields.DateTime()
    token = fields.Str(required=True)
