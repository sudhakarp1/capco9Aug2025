'''
INSERT INTO departments VALUES (10,'ACCOUNTING','NEW YORK');
INSERT INTO departments VALUES (20,'RESEARCH','DALLAS');
INSERT INTO departments VALUES (30,'SALES','CHICAGO');
INSERT INTO departments VALUES (40,'OPERATIONS','BOSTON');

'''

import cx_Oracle

# Connection parameters
dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='free')
conn = cx_Oracle.connect(user='c##trial', password='trialtest', dsn=dsn_tns)
allQueries = [
"INSERT INTO departments VALUES (10,'ACCOUNTING','NEW YORK')",
"INSERT INTO departments VALUES (20,'RESEARCH','DALLAS')",
"INSERT INTO departments VALUES (30,'SALES','CHICAGO')",
"INSERT INTO departments VALUES (40,'OPERATIONS','BOSTON')",
]
cursor = conn.cursor()

for query in allQueries:
    cursor.execute(query)

conn.commit()
# Closing the connection
cursor.close()
conn.close()