from marshmallow import Schema, fields, validate   # Marshmallow schema and field validators

class ContactSchema(Schema):                       # Schema for validating contact form data
    FullName = fields.String(
        required=True,
        validate=validate.Length(min=3, max=100)
    )                                         # Sender full name
    Email = fields.Email(required=True)       # Validates email format
    Message = fields.String(required=True)    # Message content
    

    
