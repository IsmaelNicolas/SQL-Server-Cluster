import pyodbc

# Configura los detalles de la conexión
server = '127.0.0.1'  # Dirección IP o nombre de host donde se encuentra Nginx
database = 'test'  # Nombre de la base de datos
username = 'sa'  # Nombre de usuario para la autenticación
password = 'YourStrongPassword1'  # Contraseña para la autenticación

# Crea la cadena de conexión
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Establece la conexión
conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      f"Server={server};"
                      f"Database={database};"
                      f"UID={username};"
                      f"PWD={password};")

# Crea un cursor para ejecutar consultas
cursor = conn.cursor()

# Inserta un nuevo registro en la tabla "product"
new_product = {
    'id': int(input("Ingresa id: ")),
    'name': input("Ingresa name: "),
    'value': float(input("Ingresa value: "))
}
cursor.execute("INSERT INTO schema_test.product (id, name, value) VALUES (?, ?, ?)", new_product['id'], new_product['name'], new_product['value'])
conn.commit()
print("Registro insertado con éxito.")

# Realiza una consulta para obtener los registros de la tabla "product"
cursor.execute("SELECT id, name, value FROM schema_test.product")
rows = cursor.fetchall()
print("Registros en la tabla 'product':")
for row in rows:
    print(f"ID: {row.id}, Name: {row.name}, Value: {row.value}")

# Cierra el cursor y la conexión
cursor.close()
conn.close()