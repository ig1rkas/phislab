import mysql.connector
import time

db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                              host='k953588c.beget.tech',
                              database='k953588c_physlab')

cursor = db.cursor()

# select = "SELECT student_name FROM spvAOCofQ3_solutions WHERE id = 1"
# cursor.execute(select)
# for i in cursor: print(i)

filename = "test_solution.txt"
id = 1
ck = ["spvAOCofQ3"]
sql = f"SELECT filedata FROM {ck[0]}_solutions WHERE id = {id}"
cursor.execute(sql)
result = cursor.fetchone()

# Запись файла на диск
if result:
    filedata = result[0]
    with open(filename, 'wb') as file:
        file.write(filedata)
    print(f"Файл '{filename}' успешно получен.")
else:
    print(f"Файл с именем '{filename}' не найден.")




db.commit()

cursor.close()
db.close()