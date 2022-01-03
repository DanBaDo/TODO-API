from flask import Flask, jsonify, request

todos = [ { "label": "My first task", "done": False } ]

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
  global todos
  todos.append(request.json)
  return  jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)