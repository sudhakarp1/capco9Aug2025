import cx_Oracle
# Connection parameters
dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='free')
connection = cx_Oracle.connect(user='c##trial', password='trialtest', dsn=dsn_tns)
cursor = connection.cursor()

try:   
    # Fetch data from a table
    select_query = "SELECT * FROM employees WHERE id = :id"
    cursor.execute(select_query, {"id": 1})

    # Fetch one row
    row = cursor.fetchone()
    print("Single Row:", row)

    # Fetch all rows
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for r in rows:
        print(r)
except cx_Oracle.DatabaseError as e:
    print("Error while creating table:", e)
finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
