from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField,  SubmitField
from wtforms.validators import data_required

class ContactForm(FlaskForm):
    nombreContact = StringField('Nombre completo:', validators=[ 
        data_required()
    ])
    
    mailContact = EmailField('Correo electronico:', validators=[
        data_required()
    ])

    telefonoContact = StringField('Telefono:', validators=[
        data_required()
    ])

    mensajeContact = TextAreaField('Mensaje:', validators=[
        data_required()
    ])

    submitContact = SubmitField('Enviar')