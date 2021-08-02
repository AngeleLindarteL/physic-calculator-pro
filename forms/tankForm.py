from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired

class tankForm(FlaskForm):
    medida = StringField('medida', validators=[DataRequired()])
    diametro = FloatField('diametro', validators=[DataRequired()])
    alto = FloatField('alto', validators=[DataRequired()])