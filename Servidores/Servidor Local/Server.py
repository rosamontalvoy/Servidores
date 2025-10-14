from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        return jsonify({"mensaje": "Este endpoint solo acepta POST con JSON"}), 200

    if not request.is_json:
        return jsonify({"error": "El contenido debe ser JSON"}), 415  # Error si no es JSON

    data = request.get_json()  # Mejor usar request.get_json() para evitar errores
    print("Solicitud recibida:", data)

    return jsonify({
        "fulfillmentText": "Hola desde el webhook en Flask"
    })

# Inicia el servidor en el puerto 4040
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4040)
