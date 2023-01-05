from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, methods=['GET', 'POST'], origins=['*'])
productos = []

@app.route("/productos", methods=['POST', 'GET'])
def gestion_productos():
    if request.method == "POST":
        productos.append(request.get_json())
        return {
            "message": "Producto creado exitosamente",
            "content": request.get_json()
            }, 201
    elif request.method == "GET":
        return {
            "message": "Estos son los productos registrados",
            "content": productos,
            }, 200               

@app.route("/productos/<int:id>", methods=["PUT", "DELETE", "GET"])
def gestion_producto(id):
    if len(productos) <= id:
        return {
            "message": "Listando el producto " + str(id),
            "content": "No existe producto"
            }, 404
    if request.method == "GET":
        return {
            "message": "Listando el producto " + str(id), 
            "content": productos[id]
            }, 200         
    elif request.method == "DELETE":
        producto_eliminado = productos[id]
        productos.pop(id)
        return {
            "message": "Se elimino el producto " + '{}' .format(producto_eliminado['nombre']),
        }, 200   
    elif request.method == "PUT":
        producto_anterior = productos[id] 
        data = request.get_json()
        productos[id] = data
        return {
            "message": "Se actulizo el producto " + '{}' .format(producto_anterior['nombre']) + " por " + '{}' .format(data['nombre']),
            "content": request.get_json()
        }, 201

@app.route("/productos/buscar")
def buscar_productos():
    print(request.args.get("nombre"))
    return "ok"

app.run(debug=True) 
 