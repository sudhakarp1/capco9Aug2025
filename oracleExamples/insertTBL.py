import cx_Oracle
# Connection parameters
dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='free')
connection = cx_Oracle.connect(user='c##trial', password='trialtest', dsn=dsn_tns)
cursor = connection.cursor()

try:
	# Insert data into a table
	insert_query = "INSERT INTO employees (id, name, position) VALUES (:1, :2, :3)"
	data = (2, "Joe Doe", "Software Developer")

	cursor.execute(insert_query, data)
	connection.commit()  # Commit the transaction

	print("Data inserted successfully.")
except cx_Oracle.DatabaseError as e:
    print("Error while creating table:", e)
finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()