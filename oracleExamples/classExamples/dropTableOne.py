import cx_Oracle

# Connection parameters
dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='free')
conn = cx_Oracle.connect(user='c##trial', password='trialtest', dsn=dsn_tns)

cursor = conn.cursor()
query ='''
DROP TABLE departments PURGE
'''

cursor.execute(query)

# Closing the connection
cursor.close()
conn.close()