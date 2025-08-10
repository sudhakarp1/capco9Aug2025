import cx_Oracle
# Connection parameters
dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='free')
connection = cx_Oracle.connect(user='c##trial', password='trialtest', dsn=dsn_tns)
cursor = connection.cursor()

try:   
    # Update data in a table
    update_query = "UPDATE employees SET position = :1 WHERE id = :2"
    data = ("Senior Software Engineer", 1)

    cursor.execute(update_query, data)
    connection.commit()  # Commit the transaction

    print("Data updated successfully.")

except cx_Oracle.DatabaseError as e:
    print("Error while creating table:", e)
finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
