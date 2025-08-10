import cx_Oracle

# Connection parameters
dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='free')
conn = cx_Oracle.connect(user='c##trial', password='trialtest', dsn=dsn_tns)

cursor = conn.cursor()
query ='''
CREATE TABLE departments (
  department_id   NUMBER(2) CONSTRAINT departments_pk PRIMARY KEY,
  department_name VARCHAR2(14),
  location        VARCHAR2(13)
)
'''

cursor.execute(query)

# Closing the connection
cursor.close()
conn.close()