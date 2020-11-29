from flask import Flask, jsonify

app = Flask(__name__)

from productos import productos

@app.route("/inventario")
def get_productos():
    return jsonify(productos)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)