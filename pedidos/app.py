import os

from flask import Flask, jsonify
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "pedidos.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Pedido(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    id_cliente = db.Column(db.Integer, unique=False, nullable=True)
    id_producto = db.Column(db.Integer, unique=False, nullable=True)
    cantidad = db.Column(db.String(80), unique=False, nullable=True)
    nom_product = db.Column(db.String(80), unique=False, nullable=True)
    precio_uni = db.Column(db.Float, unique=False, nullable=True)
    precio_tot= db.Column(db.Float, unique=False, nullable=True)

    def __repr__(self):
        return "<id_pedido: {}>".format(self.id_pedido)


@app.route("/pedidos", methods=["GET", "POST"])
def pedidos():
    pedidos = None
    if request.form:
        try:
            pedido = Pedido(id=request.form.get("id_pedido"),
                            id_cliente = request.form.get("id_cliente"),
                            id_producto = request.form.get("id_producto"),
                            cantidad = request.form.get("cantidad"),
                            nom_product = request.form.get("nom_product"),
                            precio_uni = request.form.get("precio_uni"),
                            precio_tot = request.form.get("precio_tot"))
            db.session.add(pedido)
            db.session.commit()
            return {"Success": "Pedido creado satisfactoriamente"} 
        except Exception as e:
            print("Failed to add pedido")
            print(e)
    pedidos = [{'id':p.id, 'cliente':p.id_cliente, 'producto':p.id_producto, 'cantidad':p.cantidad, 
    'nom_produc':p.nom_product, 'precio_u':p.precio_uni, 'preciot':p.precio_tot} for p in Pedido.query.all()]  #{"Error": "fallllllloooo"} 
    return jsonify (pedidos)

if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', debug=True)

# @app.route("/update", methods=["POST"])
# def update():
#     try:
#         newtitle = request.form.get("nuevo_pedido")
#         oldtitle = request.form.get("oldtitle")
#         book = Pedido.query.filter_by(title=oldtitle).first()
#         book.title = newtitle
#         db.session.commit()
#     except Exception as e:
#         print("Couldn't update book title")
#         print(e)
#     return redirect("/")


# @app.route("/delete", methods=["POST"])
# def delete():
#     title = request.form.get("title")
#     book = Pedido.query.filter_by(title=title).first()
#     db.session.delete(book)
#     db.session.commit()
#     return redirect("/")

