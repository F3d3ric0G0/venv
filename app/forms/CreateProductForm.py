from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,  SubmitField
from wtforms.validators import data_required, Length

class CreateProductForm(FlaskForm):
    skuProducto = StringField('Codigo SKU:', validators=[ 
        data_required(),
        Length(max=10)
    ])

    nombreProducto = StringField('Nombre:', validators=[ 
        data_required()
    ])

    descripcionProducto = TextAreaField('Descripcion:', validators=[ 
        data_required()
    ])

    urlProducto = StringField('URL imagen:', validators=[ 
        data_required()
    ])

    precioProducto = StringField('Precio:', validators=[ 
        data_required()
    ])

    submitCrearProducto = SubmitField('Registrar producto')