import pyodbc as db

# Connect to SQL Server using Windows Authentication
try:
    conn = db.connect(
        driver="{SQL Server}",
        server="DESKTOP-NICO",
        database="nico_db"
    )
    print("Successful connection")
except db.Error as ex:
    print(f"Error connecting: {ex}")

# insert query
insert_query = """
INSERT INTO OtraTabla (ID, Mensaje)
SELECT ID FROM MiTabla
FROM MiTabla;
"""

# I run the insert query and commit the transaction
try:
    cursor = conn.cursor()  # I use cursor to manage the connection

    # Execute the insert query
    cursor.execute(insert_query)

    conn.commit() # Confirm the transaction
    print("Insertion completed successfully")

    # Select query to verify inserted data
    select_query = "SELECT * FROM OtraTabla;"

    cursor.execute(select_query)

    # Get the results
    result = cursor.fetchall()

    # Print results clearly and orderly
    for row in result:
        print(row)
except db.Error as ex:
    print(f"Error executing query: {ex}")
finally:
    # Close the connection whether errors occur or not.
    if 'conn' in locals():
        conn.close()