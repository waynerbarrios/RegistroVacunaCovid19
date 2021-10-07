from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class FormLogin(FlaskForm):
    nombre= StringField("Nombre", validators=[DataRequired(), Length(min=2, max=30)])

    correo= StringField("Correo", validators=[DataRequired(), Length(min=2, max=30)])

    mensaje= StringField("Enviar Mensaje", validators=[DataRequired(), Length(min=2, max=80)])

    boton= SubmitField('Enviar')