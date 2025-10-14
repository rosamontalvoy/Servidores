# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt requirements.txt
COPY server.py server.py

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que se ejecutará la app
EXPOSE 8080

# Comando para ejecutar el servidor Flask
CMD ["python", "server.py"]
