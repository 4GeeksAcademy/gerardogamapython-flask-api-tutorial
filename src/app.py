from flask import Flask, jsonify, request


todos = [{ "label": "Sample", "done": True }]

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    
    request_body = request.get_json()
    if not request_body:
        return flask.abort(400, description="Empty request body")
    label = request_body.get('label')
    if not label:
        return flask.abort(400, description="Label is required")
    new_todo = {"label": label, "done": False}
    todos.append(new_todo)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    
    del todos[position]
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)