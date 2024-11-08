from marshmallow import Schema, fields

class MedBotSchema(Schema):
    user_query = fields.String(required=True)