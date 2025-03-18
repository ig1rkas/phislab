import mysql.connector
import time

db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                              host='k953588c.beget.tech',
                              database='k953588c_physlab')

cursor = db.cursor()

# select = "SELECT student_name FROM spvAOCofQ3_solutions WHERE id = 1"
# cursor.execute(select)
# for i in cursor: print(i)

cursor.execute("select * FROM ufdv25QAJV_solutions")
for i in cursor: print(i)



db.commit()

cursor.close()
db.close()