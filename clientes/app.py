from flask import Flask, jsonify

app = Flask(__name__)

from clientes import clientes

@app.route("/clientes")
def get_clientes():
    return jsonify(clientes)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)