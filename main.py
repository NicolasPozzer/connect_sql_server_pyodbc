import pyodbc as DB #Nombramos como DB

# Definir los parámetros de conexión
driver = "{SQL Server}"
server = "DESKTOP-NICO"
database = "nico_db"

# Conectar a SQL Server usando la autenticación de Windows
try:
    conexion = DB.connect(
        driver=driver,
        server=server,
        database=database,
        trusted_connection='yes'
    )
    print("Conexión exitosa")
except DB.Error as ex:
    print(f"Error al conectar: {ex}")

# Crear una consulta
consulta = "SELECT Mensaje FROM MiTabla"

#Ejecutamos la consulta y guardamos en una variable -> result
try:
    result = conexion.execute(consulta)

    # Recorrer para mostrar mensaje
    for Mensaje in result:
        print(Mensaje)
except DB.Error as ex:
    print(f"Error al ejecutar la consulta: {ex}")
finally:
    # Cerrar la conexión
    if 'conexion' in locals():
        conexion.close()
