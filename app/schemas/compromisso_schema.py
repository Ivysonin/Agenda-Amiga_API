from marshmallow import Schema, fields, validates, ValidationError
from datetime import date


class CompromissoSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    descricao = fields.Str(required=True)
    data = fields.Date(required=True) # Formato: ISO 8601
    horario = fields.Str(required=True)


    @validates("data")
    def validate_data(self, value, **kwargs):
        if value < date.today():
            raise ValidationError("A data do compromisso deve ser no futuro.")