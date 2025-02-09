from fastapi import FastAPI
from database import get_connection

# Crear una instancia de FastAPI
app = FastAPI()

# 🔹 Ruta raíz para evitar error 404 en "/"
@app.get("/")
def home():
    return {"mensaje": "¡Bienvenido a la API de películas con FastAPI!"}

# 🔹 Ruta para "/movies"
# 🔹 Endpoint para obtener todas las películas desde la base de datos
@app.get("/movies")
def obtener_peliculas():
    conexion = get_connection()  # Conectar a la base de datos
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, title, release_year, genre, director, cast FROM movies;")  # Consulta SQL
            peliculas = cursor.fetchall()  # Obtener todos los registros
        return peliculas  # Devolver en formato JSON
    finally:
        conexion.close()  # Cerrar la conexión después de usarla