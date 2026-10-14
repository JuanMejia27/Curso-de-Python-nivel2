from flask import Flask, jsonify, request

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

@app.route("/task/<int:task_id", methods = ["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id" == task_id]), None)
    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404
    task["title"] = request.json.get("title", task["title"])
    task["done"] = request.json.get("done", task["done"])
    return jsonify(task)

if __name__ == "__main__":
    app.run(debug=True)