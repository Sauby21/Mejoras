from utils.ma import ma
from marshmallow import fields
from models.servicio import Servicio

class ServicioSchema(ma.SQLAlchemySchema):
    id_servicio = fields.Integer()
    descripcion = fields.String()
    class Meta:
        model = Servicio
        fields = ('id_servicio', 'descripcion')

servicio_schema = ServicioSchema()
servicios_schema = ServicioSchema(many=True)