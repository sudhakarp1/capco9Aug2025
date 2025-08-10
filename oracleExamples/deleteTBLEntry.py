import cx_Oracle
# Connection parameters
dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='free')
connection = cx_Oracle.connect(user='c##trial', password='trialtest', dsn=dsn_tns)
cursor = connection.cursor()

try:   
    # Delete data from a table
    delete_query = "DELETE FROM employees WHERE id = :1"
    cursor.execute(delete_query, (1,))

    connection.commit()  # Commit the transaction

    print("Data deleted successfully.")
except cx_Oracle.DatabaseError as e:
    print("Error while creating table:", e)
finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
