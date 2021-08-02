from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import DataRequired

class fillForm(FlaskForm):
    quest = BooleanField('¿Desea usar relleno?')
    medidar = StringField('Medida del Relleno', default="default")
    cantidad = FloatField('cantidad del Relleno', default=0)
    nombre = StringField('nombre del Relleno', default=0)