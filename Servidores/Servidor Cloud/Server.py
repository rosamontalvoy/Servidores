from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# CORRECCIÓN: Faltaba el decorador @ antes de app.route
# Ruta para manejar la lista de películas
@app.route('/peliculas', methods=['GET', 'POST'])
def manejar_peliculas():
    archivo_json = "peliculas_limpias.json"

    try:
        if request.method == 'GET':
            # Verifica si el archivo existe
            if not os.path.exists(archivo_json):
                return jsonify({"error": "El archivo JSON no existe"}), 404

            # Abre el archivo y devuelve su contenido
            with open(archivo_json, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            return jsonify(datos)

        elif request.method == 'POST':
            # Obtiene los datos del cuerpo de la solicitud
            data = request.get_json(silent=True)

            # Verifica si los datos no están en formato JSON o si falta la clave 'Favoritas'
            if not data or "Favoritas" not in data:
                return jsonify({"error": "Formato incorrecto, se necesita la clave 'Favoritas'"}), 400

            # Si el archivo ya existe, lo carga
            if os.path.exists(archivo_json):
                with open(archivo_json, "r", encoding="utf-8") as archivo:
                    datos = json.load(archivo)
            else:
                # Si no existe, inicializa una nueva estructura
                datos = {"Favoritas": []}

            # Asegura que 'Favoritas' sea una lista y agrega las películas
            if isinstance(datos["Favoritas"], list):
                if isinstance(data["Favoritas"], list):
                    datos["Favoritas"].extend(data["Favoritas"])  # Agregar múltiples películas
                else:
                    datos["Favoritas"].append(data["Favoritas"])  # Agregar una sola película
            else:
                return jsonify({"error": "El formato del archivo JSON no es válido"}), 500

            # Guarda los cambios en el archivo JSON
            with open(archivo_json, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=4)

            return jsonify({"mensaje": "Película(s) añadida(s) correctamente"}), 201

    except json.JSONDecodeError:
        return jsonify({"error": "Error al leer el archivo JSON"}), 500
    except TimeoutError:
        # Respuesta personalizada para timeouts (por ejemplo, en un webhook)
        return jsonify({
            "fulfillmentResponse": {
                "messages": [{"text": {"text": ["Error de timeout, intenta nuevamente."]}}]
            },
            "sessionInfo": {
                "parameters": {"event": "WEBHOOK_TIMEOUT"}
            }
        }), 504
    except Exception as e:
        # Respuesta general para cualquier otro error
        return jsonify({
            "fulfillmentResponse": {
                "messages": [{"text": {"text": ["Servicio no disponible en este momento."]}}]
            },
            "sessionInfo": {
                "parameters": {"event": "WEBHOOK_UNAVAILABLE"}
            }
        }), 503

# Solo ejecuta la app si se corre directamente este archivo
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4040)
