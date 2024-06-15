import pyodbc
import csv

try:
    conn = pyodbc.connect(
        # SQL Params
        driver="{SQL Server}",
        server="DESKTOP-NICO",
        database="nico_db"
    )
    print("Successful connection")
except pyodbc.Error as ex:
    print(f"Error connecting: {ex}")
    exit(1)

############ Insert Table Name ⬇⬇  ############
query_sql = "SELECT * FROM MiTabla"

try:
    cursor = conn.cursor()
    cursor.execute(query_sql)

    # Get column names
    column = [column[0] for column in cursor.description]

    # Get all the data
    datos = cursor.fetchall()

    # .csv file name
    file_csv = "exported_data.csv"

    # Write the data to the .csv file
    with open(file_csv, mode='w', newline='', encoding='utf-8') as file:
        writer_csv = csv.writer(file)

        # write colum names
        writer_csv.writerow(column)

        # write data
        for fila in datos:
            writer_csv.writerow(fila)

    print(f"Data successfully exported to {file_csv}")
except pyodbc.Error as ex:
    print(f"Error executing query: {ex}")
finally:
    if 'conn' in locals():
        conn.close()
