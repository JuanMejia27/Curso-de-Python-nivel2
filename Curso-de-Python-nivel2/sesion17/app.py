#Sesion17
'''from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [{"id": 1, "title": "Tarea 1", "done": False}, {"id": 2, "title": "Tarea 2", "done": True},]

@app.route("/") #Ruta de home definida con el mensaje mostrado en el return
def home():
    return "Api rest con flask"

@app.route("/tasks", methods = ["GET"]) #Ruta para el metodo GET
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks2", methods = ["POST"])
def create_task():
    if not request.is_json:
        return jsonify({"error": "Ivalid JSON", "data": request.data.decode()}), 
    400
    title = request.json.get("title")
    if not title:
        return jsonify({"error": "Title is required"}), 400
    new_task = {
        "id": len(tasks) + 1,
        "title": request.json["title"],
        "done": False,
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route("/task/<int:task_id>", methods = ["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id" == task_id]), None)
    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404
    task["title"] = request.json.get("title", task["title"])
    task["done"] = request.json.get("done", task["done"])
    return jsonify(task)

@app.route("/tasks/<init:task_id>", methods = ["DELETE"])
def delete_task(task_id):
    global tasks
    taks =[t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Tarea eliminada"})

if __name__ == "__main__":
    app.run(debug=True)'''
#////////////////////////////////////////////////////////////
#Sesion18
'''from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/") #Ruta de home definida con el mensaje mostrado en el return
def home():
    return "Pagina principal"

@app.route("/about")
def about():
    return "Acerca de"

@app.route("/contact")
def contact():
    return "Esta pagina es de contacto"

if __name__ == "__main__":
    app.run(debug=True)'''

'''from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [{"id": 1, "title": "Tarea 1", "done": False}, 
         {"id": 2, "title": "Tarea 2", "done": True},
         ]

@app.route("/") #Ruta de home definida con el mensaje mostrado en el return
def home():
    return "Api rest con flask"

@app.route("/tasks", methods = ["GET", "POST"]) #Ruta para el metodo GET
def greet():
    if request.method == "POST":
        name = request.json.get("name", "Desconocido")
        return f"Hola! {name}", 201
    else:
        return "Usa oista para enviar tu nombre"

@app.route("/tasks2", methods = ["POST"])
def create_task():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON", "data": request.data.decode()}), 
    400
    title = request.json.get("title")
    if not title:
        return jsonify({"error": "Title is required"}), 400
    
    new_task = {
        "id": len(tasks) + 1,
        "title": request.json["title"],
        "done": False,
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route("/task/<int:task_id>", methods = ["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404
    task["title"] = request.json.get("title", task["title"])
    task["done"] = request.json.get("done", task["done"])
    return jsonify(task)

@app.route("/tasks/<ini:task_id>", methods = ["DELETE"])
def delete_task(task_id):
    global tasks
    tasks =[t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Tarea eliminada"})

if __name__ == "__main__":
    app.run(debug=True)'''

#Sesion19
#Validacion de acceso
from flask import Flask, jsonify, request

app = Flask(__name__)

'''users = {
    "user1": {"password": "pass1", "token": "token1"},
    "user2": {"password": "pass2", "token": "token2"},
    }'''

'''TOKEN = "1234qwerty" #Contraseña
#Metodo protegido con contraseña
@app.route("/protected", methods = ["GET"])
def ruta_protegida():
    token = request.headers.get("Authorization")
    if token == f"Bearer {TOKEN}":
        return jsonify({"message": "Acceso concedido"})
    else:
        return jsonify({"error": "Acceso denegado"}), 401'''

'''@app.route("/login", methods = ["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    if user and user["password"] == password:
        return jsonify({"token": user["token"]})
    else:
        return jsonify({"error": "Credenciales invalidas"}), 401'''

user = {
    "user1": {"password": "pass1", "token": "token1"}
    }

@app.route("/protected", methods = {"GET"})
def protected_route():
    token = request.headers.get("Authorization")
    if token and any(user["token"] == token.split()[-1] for user in user.values()):
        return jsonify({"message": "Accesoconcedido"})
    else:
        return jsonify({"Error": "Acceso denegado"}), 401

if __name__ == "__main__":
    app.run(debug=True)