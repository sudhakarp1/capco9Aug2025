import cx_Oracle

# Connection parameters
dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='free')
conn = cx_Oracle.connect(user='c##trial', password='trialtest', dsn=dsn_tns)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE employees (
        emp_id NUMBER PRIMARY KEY,
        emp_name VARCHAR2(50),
        hire_date DATE
    )
""")

# Closing the connection
cursor.close()
conn.close()