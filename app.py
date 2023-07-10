from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pyodbc

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Reemplaza "*" con el origen permitido de tu cliente HTML
    allow_methods=["*"],
    allow_headers=["*"],
)


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

# Ruta para actualizar un producto
@app.put("/products/{product_id}")
async def update_product(product_id: int, product: dict):
    # Establece la conexión
    conn = pyodbc.connect(conn_str)

    # Crea un cursor para ejecutar consultas
    cursor = conn.cursor()

    # Actualiza el registro en la tabla "product"
    cursor.execute("UPDATE schema_test.product SET name = ?, value = ? WHERE id = ?", product['name'], product['value'], product_id)
    conn.commit()

    # Cierra el cursor y la conexión
    cursor.close()
    conn.close()

    return {"message": "Producto actualizado exitosamente"}

# Ruta para eliminar un producto
@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    # Establece la conexión
    conn = pyodbc.connect(conn_str)

    # Crea un cursor para ejecutar consultas
    cursor = conn.cursor()

    # Elimina el registro de la tabla "product"
    cursor.execute("DELETE FROM schema_test.product WHERE id = ?", product_id)
    conn.commit()

    # Cierra el cursor y la conexión
    cursor.close()
    conn.close()

    return {"message": "Producto eliminado exitosamente"}

# Ruta para buscar un producto por ID
@app.get("/products/{product_id}")
async def search_product(product_id: int):
    # Establece la conexión
    conn = pyodbc.connect(conn_str)

    # Crea un cursor para ejecutar consultas
    cursor = conn.cursor()

    # Realiza una consulta para obtener el registro de la tabla "product" por ID
    cursor.execute("SELECT id, name, value FROM schema_test.product WHERE id = ?", product_id)
    row = cursor.fetchone()

    if row is None:
        # Cierra el cursor y la conexión
        cursor.close()
        conn.close()
        return {"message": "Producto no encontrado"}

    # Convierte la tupla en un diccionario
    product = {
        "id": row[0],
        "name": row[1],
        "value": row[2]
    }

    # Cierra el cursor y la conexión
    cursor.close()
    conn.close()

    return product

# Ruta para obtener todos los productos
@app.get("/products")
async def read_products():
    # Establece la conexión
    conn = pyodbc.connect(conn_str)

    # Crea un cursor para ejecutar consultas
    cursor = conn.cursor()

    # Realiza una consulta para obtener todos los registros de la tabla "product"
    cursor.execute("SELECT id, name, value FROM schema_test.product")
    rows = cursor.fetchall()

    # Convierte las tuplas en diccionarios
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
