import pyodbc as db # Lo nombro como DB

# Defino los parámetros de conexión y
# Conecto a SQL Server usando la autenticación de Windows
try:
    conexion = db.connect(
        driver="{SQL Server}",
        server="DESKTOP-NICO",
        database="nico_db",
        trusted_connection="yes"# Es para conectarse desde Windows
    )
    print("Conexión exitosa")
except db.Error as ex:
    print(f"Error al conectar: {ex}")

# CONSULTAS..
insertar = "INSERT INTO MiTabla (ID, Mensaje) VALUES (5, '5to Elemento');"
consulta = "SELECT * FROM MiTabla;"


# Ejecuto la consulta de inserción y confirmo la transacción
try:
    cursor = conexion.cursor() #Utilizo cursor para manejar la conexion
    cursor.execute(insertar)
    #conexion.commit()  #Con commit confirmo la transacción si no lo implemento puedo ver como va a quedar
    print("Inserción realizada con éxito")

    # Ejecutar la consulta de selección y guardar en una variable -> result
    cursor.execute(consulta)
    result = cursor.fetchall()

    #print(result) Imprimir de forma simple pero en una sola linea.
    # Recorrer e imprimir de manera clara y ordenada.
    for row in result:
        print(row)
except db.Error as ex:
    print(f"Error al ejecutar la consulta: {ex}")

finally:
    # Cerrar la conexión Aunque ocurran errores o no.
    if 'conexion' in locals():
        conexion.close()