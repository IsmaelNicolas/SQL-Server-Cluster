import asyncio
import concurrent.futures
from fastapi import FastAPI
import pyodbc
import json


app = FastAPI()

# Configura los detalles de la conexión
server = '127.0.0.1'  # Dirección IP o nombre de host donde se encuentra Nginx
database = 'test'  # Nombre de la base de datos
username = 'sa'  # Nombre de usuario para la autenticación
password = 'YourStrongPassword1'  # Contraseña para la autenticación

# Crea la cadena de conexión
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Ruta para ingresar un producto
@app.post("/products")
async def create_product(product: dict):
    # Establece la conexión
    conn = pyodbc.connect(conn_str)

    # Crea un cursor para ejecutar consultas
    cursor = conn.cursor()

    # Inserta un nuevo registro en la tabla "product"
    cursor.execute("INSERT INTO schema_test.product (id, name, value) VALUES (?, ?, ?)", product['id'], product['name'], product['value'])
    conn.commit()

    # Cierra el cursor y la conexión
    cursor.close()
    conn.close()

    return {"message": "Producto creado exitosamente"}

# Función asincrónica para leer los productos
async def fetch_products():
    # Establece la conexión
    conn = pyodbc.connect(conn_str)

    # Crea un cursor para ejecutar consultas
    cursor = conn.cursor()

    # Realiza una consulta para obtener los registros de la tabla "product"
    cursor.execute("SELECT id, name, value FROM schema_test.product")
    rows = cursor.fetchall()

    # Convertir las tuplas en diccionarios
    products = []
    for row in rows:
        product = {
            "id": row[0],
            "name": row[1],
            "value": row[2]
        }
        products.append(product)

    # Cierra el cursor y la conexión
    cursor.close()
    conn.close()

    return products

@app.get("/products")
async def read_products():
    # Establece la conexión
    conn = pyodbc.connect(conn_str)

    # Crea un cursor para ejecutar consultas
    cursor = conn.cursor()

    # Realiza una consulta para obtener los registros de la tabla "product"
    cursor.execute("SELECT id, name, value FROM schema_test.product")
    rows = cursor.fetchall()

    # Convertir las tuplas en diccionarios
    products = []
    for row in rows:
        product = {
            "id": row[0],
            "name": row[1],
            "value": row[2]
        }
        products.append(product)

    # Cierra el cursor y la conexión
    cursor.close()
    conn.close()

    return products



