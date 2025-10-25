import json
import os

# 1. Ruta automática al archivo JSON (misma carpeta que este script)
ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_json = os.path.join(ruta_actual, "listadopeliculasrepes.json")

# 2. Cargar el archivo JSON
with open(ruta_json, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 3. Obtener la lista de películas
favoritas = data.get("Favoritas", [])

# 4. Eliminar duplicados manteniendo el orden original
favoritas_unicas = []
vistas = set()
for titulo in favoritas:
    if titulo not in vistas:
        vistas.add(titulo)
        favoritas_unicas.append(titulo)

# 5. Guardar el resultado limpio en el mismo archivo o en otro nuevo
ruta_salida = os.path.join(ruta_actual, "peliculas_limpias.json")
with open(ruta_salida, 'w', encoding='utf-8') as f:
    json.dump({"Favoritas": favoritas_unicas}, f, ensure_ascii=False, indent=4)

print(f"Películas filtradas y guardadas en: {ruta_salida}")
print(f"Total sin duplicados: {len(favoritas_unicas)}")

