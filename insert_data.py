import pyodbc

# Configura los detalles de la conexión
server = '127.0.0.1'  # Dirección IP o nombre de host donde se encuentra SQL Server
database = 'test'  # Nombre de la base de datos
username = 'sa'  # Nombre de usuario para la autenticación
password = 'YourStrongPassword1'  # Contraseña para la autenticación

# Crea la cadena de conexión
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Lee los valores del archivo
file_path = 'datos.txt'  # Ruta al archivo de datos
data = []
with open(file_path, 'r') as file:
    for line in file:
        values = line.strip().split(',')
        if len(values) == 3:
            data.append(values)
            print(values)

# Establece la conexión
conn = pyodbc.connect(conn_str)

# Crea un cursor para ejecutar consultas
cursor = conn.cursor()

# Realiza las inserciones en la base de datos
for values in data:
    id = values[0]
    name = values[1]
    value = values[2]
    cursor.execute("INSERT INTO schema_test.product (id, name, value) VALUES (?, ?, ?)", id, name, value)
    conn.commit()   
    cursor.execute("SELECT 1")

# Guarda los cambios en la base de datos

# Cierra el cursor y la conexión
cursor.close()
conn.close()

print("Inserciones realizadas con éxito.")
