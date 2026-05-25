from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Simple HTML Frontend (no templates folder needed)
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kubernetes Todo App - Azure AKS</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f4f7f9; }
        h1 { color: #2c3e50; }
        input { padding: 12px; width: 350px; font-size: 16px; }
        button { padding: 12px 24px; background: #3498db; color: white; border: none; font-size: 16px; cursor: pointer; }
        button:hover { background: #2980b9; }
        ul { list-style: none; padding: 0; }
        li { background: white; margin: 10px 0; padding: 15px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
    </style>
</head>
<body>
    <h1>🚀 Kubernetes Todo App on Azure AKS</h1>
    <p><strong>Tech Stack:</strong> Python Flask + PostgreSQL + Docker + AKS</p>
    
    <input type="text" id="task" placeholder="What needs to be done?" />
    <button onclick="addTodo()">Add Todo</button>

    <h2>My Todos</h2>
    <ul id="todoList"></ul>

    <script>
        async function loadTodos() {
            const res = await fetch('/todos');
            const todos = await res.json();
            const list = document.getElementById('todoList');
            list.innerHTML = '';
            todos.forEach(t => {
                list.innerHTML += `<li>✅ ${t.task}</li>`;
            });
        }

        async function addTodo() {
            const input = document.getElementById('task');
            const task = input.value.trim();
            if (!task) return;
            
            await fetch('/todos', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ task: task })
            });
            input.value = '';
            loadTodos();
        }

        // Load todos on page load
        window.onload = loadTodos;
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([{'id': t.id, 'task': t.task, 'completed': t.completed} for t in todos])

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo = Todo(task=data['task'])
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'id': new_todo.id, 'task': new_todo.task}), 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)