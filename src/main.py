import pyodbc as db

# Conectar a SQL Server usando la autenticación de Windows
try:
    conexion = db.connect(
        driver="{SQL Server}",
        server="DESKTOP-NICO",
        database="nico_db"
    )
    print("Conexión exitosa")
except db.Error as ex:
    print(f"Error al conectar: {ex}")

# Consulta de inserción
insert_query = """
INSERT INTO OtraTabla (ID, Mensaje)
SELECT ID, Mensaje
FROM MiTabla;
"""

# Ejecuto la consulta de inserción y confirmo la transacción
try:
    cursor = conexion.cursor()  # Utilizo cursor para manejar la conexión

    # Ejecutar la consulta de inserción
    cursor.execute(insert_query)

    # Confirmar la transacción
    conexion.commit()  # Con commit confirmo la transacción
    print("Inserción realizada con éxito")

    # Consulta de selección para verificar los datos insertados
    select_query = "SELECT ID, Mensaje FROM OtraTabla;"

    cursor.execute(select_query)

    # Obtener los resultados
    result = cursor.fetchall()

    # Imprimir los resultados de manera clara y ordenada
    for row in result:
        print(row)
except db.Error as ex:
    print(f"Error al ejecutar la consulta: {ex}")
finally:
    # Cerrar la conexión aunque ocurran errores o no.
    if 'conexion' in locals():
        conexion.close()
