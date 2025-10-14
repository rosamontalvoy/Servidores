from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/serverpeliculas', methods=['GET', 'POST'])
def server_peliculas():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({"message": "Received data", "data": data}), 201
    elif request.method == 'GET':
        return jsonify({"message": "Hello from server_peliculas!"})
    else:
        return jsonify({"message": "Method not allowed"}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
