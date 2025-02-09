import pymysql

# Configuración de la conexión a MariaDB
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="movie_catalog",
        cursorclass=pymysql.cursors.DictCursor  # Para obtener los datos en formato diccionario
    )
