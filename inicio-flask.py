from flask import Flask, request
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = ""
API_URL = "/static/swagger.json"

swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Inventario"
    }
)

app = Flask(__name__)
app.register_blueprint(swagger_blueprint)




CORS(app, methods=['GET', 'POST', 'DELETE', 'PUT'], origins=['*'])
productos = []

@app.route("/productos", methods=['POST', 'GET'])
def gestion_productos():
    print(request.method)
    if request.method == "POST":
        print(request.get_json())
        productos.append(request.get_json())
        return {
            "message": "Producto creado exitosamente",
            "content": request.get_json()
            }, 201
    elif request.method == "GET":
        print(request) 
        print(productos)
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
        print(id)
        print(productos)
        print(productos[id])
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


app.run(debug=True) 
 
