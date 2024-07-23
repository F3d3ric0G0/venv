from flask import Flask, request, render_template, redirect, session, url_for, flash
from flask import abort
from flask_sqlalchemy import SQLAlchemy

from forms.CreateProductForm import CreateProductForm
from forms.ContactForm import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'esto es una clave segura'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

# Modelo Productos
class Producto(db.Model):
    __tablename__ = 'Productos'
    id_producto = db.Column(db.Integer, primary_key=True)
    sku_producto = db.Column(db.String(10), nullable=False)
    nombre_producto = db.Column(db.String(39), nullable=False)
    descripcion_producto = db.Column(db.String(250), nullable=False)
    url_producto = db.Column(db.String(250), nullable=False)
    precio_producto = db.Column(db.Float, nullable=False)

# crear tablas 
with app.app_context():
    db.create_all()

# rutas
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/detalles")
def detalles_producto():
    return render_template('detallesproducto.html')


@app.route("/productos")
def productos():

    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)

@app.route("/nosotros")
def nosotros():
    return render_template('nosotros.html')

# -------------------------------------------------------------------------
@app.route("/contacto", methods=['GET', 'POST'])
def contacto():

    form = ContactForm()

    if form.validate_on_submit():
        nombre_viejo = session.get('nombre-contacto')

        if nombre_viejo is not None and nombre_viejo != form.nombreContact.data:
            session['nombre-contacto'] = form.nombreContact.data
            form.nombreContact.data = ''
            flash('El nombre fue actualizado correctamente')
            return redirect(url_for("contacto"))
        
    return render_template('contacto.html', form=form, nombre=session.get('nombre-contacto'))

@app.route("/carrito")
def cart():
    return render_template('carrito.html')

@app.route("/login")
def login():
    return render_template('login.html')

# administrar productos - CRUD
@app.route("/admin")
def admin():
    productos = Producto.query.all()
    return render_template('admin/admin-productos.html', productos=productos)

# formulario para registrar un producto
@app.route("/registrar-producto", methods=['GET', 'POST'])
def registrar_producto():
    registro = CreateProductForm()

    if request.method == 'POST' and registro.validate_on_submit():
        nuevo_producto = Producto(
            sku_producto=registro.skuProducto.data,
            nombre_producto=registro.nombreProducto.data,
            descripcion_producto=registro.descripcionProducto.data,
            url_producto=registro.urlProducto.data,
            precio_producto= float(registro.precioProducto.data)
        )
        db.session.add(nuevo_producto)
        db.session.commit()

        flash(f"Producto {nuevo_producto.sku_producto} creado correctamente.")
        return redirect(url_for("productos"))
    elif request.method == 'POST' :
        flash("Error. Por favor revise los datos del formulario")
    
    return render_template('./admin/registrar-producto.html', form=registro)

if __name__ == "__main__":
    app.run(debug=True)