from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"id": 1, "task": "Learn Flask", "done": True},
    {"id": 2, "task": "Build a cool app", "done": False},
]

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    new_todo = {
        "id": len(todos) + 1,
        "task": request.json["task"],
        "done": False,
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = next((todo for todo in todos if todo["id"] == todo_id), None)
    if todo:
        return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404

@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = next((todo for todo in todos if todo["id"] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    todo["task"] = request.json.get("task", todo["task"])
    todo["done"] = request.json.get("done", todo["done"])
    return jsonify(todo)

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo["id"] != todo_id]
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
