import mysql.connector
import random
from pprint import pprint
from os import system
from config import labs

db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                             host='k953588c.beget.tech',
                             database='k953588c_physlab')

# cursor = db.cursor()
# query = ("SELECT * FROM USERS")

# cursor.execute(query)

# for i in cursor:
#   print(i)

def add_student_in_class(Student_name: str, Student_email: str, class_key: str) -> None:
    db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                             host='k953588c.beget.tech',
                             database='k953588c_physlab')
    cursor = db.cursor()
    query = f"INSERT INTO {class_key} (Student_name, Student_email) VALUES ('{Student_name}', '{Student_email}')" 

    cursor.execute(query)

    db.commit()

    cursor.close()
    db.close()


def autorisation_user(username: str, email: str, class_key: str, type: int) -> bool:
    db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                             host='k953588c.beget.tech',
                             database='k953588c_physlab')
    cursor = db.cursor()
    query = ("SELECT * FROM USERS")

    cursor.execute(query)

    users = [i for i in cursor]

    if type:
        try:
            cursor.execute(F"SELECT * FROM {class_key}")
            students = [i for i in cursor]
            for id, name, email in students:
                if (name, email) == (username, email):
                    break
            else:
                add_student_in_class(username, email, class_key)
            return True
        except Exception:
            return False
        
    db.commit()

    cursor.close()
    db.close()
    
    for id, un, em, ck, t in users:
        # print((un, em, ck, t), (username, email, class_key, type))
        if (un, em, t) == (username, email, type):
            return True
        
    return False


def regestration_new_user(username: str, email: str, class_key: str, type: int) -> None:
    db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                             host='k953588c.beget.tech',
                             database='k953588c_physlab')
    cursor = db.cursor()
    insertion = f"""
    INSERT INTO USERS (username, email, class, type) VALUES
    ('{username}', '{email}', '{class_key}', {type})
    """
    # print(f"('{str(username)}', '{str(email)}', '{str(class_key)}', {int(type)})")
    cursor.execute(insertion)

    db.commit()

    cursor.close()
    db.close()
    if not type: create_classes_list(class_key)

def create_classes_list(teacher_key: str) -> None:
    db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                             host='k953588c.beget.tech',
                             database='k953588c_physlab')
    cursor = db.cursor()
    insertion = f"""
    CREATE TABLE {teacher_key} (id int PRIMARY KEY NOT NULL AUTO_INCREMENT, Classname varchar(255), Classkey varchar(255))
    """
    cursor.execute(insertion)

    db.commit()

    cursor.close()
    db.close()


def check_email(email: str) -> bool:
    if "@" in email and "." in email:
        if email.index("@") != 0 and email.index("@") <= len(email) - 3 and email.index(".") > email.index("@"):
            return True
    return False


def check_username(username: str) -> bool:
    if len(username.split()) == 2:
        return True
    return False


def generate_key() -> str:
    db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                             host='k953588c.beget.tech',
                             database='k953588c_physlab')

    cursor = db.cursor()
    keys_from_db = f"""
    SELECT * FROM CLASSKEYS
    """
    symbols = "qwertyuiopasdfghjklzxcvbnm"
    symbols += symbols.upper() + "1234567890"
    symbols = list(symbols)
    cursor.execute(keys_from_db)

    keys = [i[1] for i in cursor]

    while 1:
        key = ""
        for i in range(8):
            key += random.choice(symbols)
        if key not in keys:
            break
        
    insertion = f"""
    INSERT INTO CLASSKEYS (classkey) VALUES ('{key}')
    
    """
    cursor.execute(insertion)

    db.commit()

    cursor.close()
    db.close()

    return key 

def generate_classkey() -> str:
    db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                             host='k953588c.beget.tech',
                             database='k953588c_physlab')

    cursor = db.cursor()
    keys_from_db = f"""
    SELECT * FROM CLASSKEYS
    """
    symbols = "qwertyuiopasdfghjklzxcvbnm"
    symbols += symbols.upper() + "1234567890"
    symbols = list(symbols)
    cursor.execute(keys_from_db)

    keys = [i[1] for i in cursor]

    while 1:
        key = ""
        for i in range(10):
            key += random.choice(symbols)
        if key not in keys:
            break
        
    insertion = f"""
    INSERT INTO CLASSKEYS (classkey) VALUES ('{key}')
    
    """
    cursor.execute(insertion)

    db.commit()

    cursor.close()
    db.close()

    return key 

def give_tasks(tasks: list, class_key: str) -> None:
    db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                             host='k953588c.beget.tech',
                             database='k953588c_physlab')
    cursor = db.cursor()
    select = f"SELECT * FROM {class_key}_tasks"
    cursor.execute(select)
    tasks_gived = [i[1] for i in cursor]
    for task in tasks:
        if task not in tasks_gived:
            insert = f"""
            INSERT INTO {class_key}_tasks (task_key) VALUES ('{task}')
            """
            cursor.execute(insert)
    db.commit()

    cursor.close()
    db.close()

def add_class(classname: str, teacher_key: str) -> str:
    db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                             host='k953588c.beget.tech',
                             database='k953588c_physlab')
    cursor = db.cursor()
    key = generate_classkey()
    insert = f"""
    INSERT INTO {teacher_key} (Classname, Classkey) VALUES
    ('{classname}', '{key}')
    """
    cursor.execute(insert)
    
    insertion = f"""
    CREATE TABLE {key} (id int PRIMARY KEY NOT NULL AUTO_INCREMENT, Student_name varchar(255), Student_email varchar(255))
    """
    cursor.execute(insertion)
    insertion = f"""
    CREATE TABLE {key}_tasks (id int PRIMARY KEY NOT NULL AUTO_INCREMENT, task_key varchar(255))
    """
    cursor.execute(insertion)
    insertion = f"""
    CREATE TABLE {key}_solutions (id int PRIMARY KEY NOT NULL AUTO_INCREMENT, student_name varchar(255), theme varchar(255), desription varchar(255), filename VARCHAR(255) NOT NULL, filedata LONGBLOB NOT NULL)
    """
    cursor.execute(insertion)
    
    

    db.commit()

    cursor.close()
    db.close()
    
    return key

def take_teacher_key(username: str, email: str) -> str:
    db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                             host='k953588c.beget.tech',
                             database='k953588c_physlab')
    cursor = db.cursor()
    query = ("SELECT * FROM USERS")

    cursor.execute(query)

    users = [i for i in cursor]

    db.commit()

    cursor.close()
    db.close()
    for id, un, em, ck, t in users:
        if (un, em) == (username, email):
            return ck

def download_classes(key: str) -> list:
    db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                             host='k953588c.beget.tech',
                             database='k953588c_physlab')

    cursor = db.cursor()
    classes_list = f"""
    SELECT * FROM {key}
    """
    cursor.execute(classes_list)
    classes = [[i[1], i[2]] for i in cursor]
    db.commit()

    cursor.close()
    db.close()
    
    return classes

def open_lab(lab_key: str) -> exec:
    system(f"python {labs[lab_key][1]}")

def download_tasks(key: str) -> list:
    db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                             host='k953588c.beget.tech',
                             database='k953588c_physlab')
    cursor = db.cursor()
    download = f"""
    SELECT * FROM {key}_tasks
    """
    cursor.execute(download)
    tasks = [i[1] for i in cursor]
    db.commit()

    cursor.close()
    db.close()
    
    return tasks
    
def take_name(key: str) -> str:
    return labs[key][0]

def add_solution(key: str, student_name: str, theme: str, description: str, filename: str, filepath: str) -> None:
    db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                             host='k953588c.beget.tech',
                             database='k953588c_physlab')
    cursor = db.cursor()
    
    description = description[:70]
    
    
    if (filename, filepath) != ("name", "path"):
    
        with open(filepath, 'rb') as file:
            filedata = file.read()

        # Вставка файла в таблицу
        sql = "INSERT INTO " + key + "_solutions (student_name, theme, desription, filename, filedata) VALUES (%s, %s, %s, %s, %s)"
        values = (student_name, theme, description, filename, filedata)
    else:
        sql = "INSERT INTO " + key + "_solutions (student_name, theme, desription) VALUES (%s, %s, %s)"
        values = (student_name, theme, description)
    cursor.execute(sql, values)
    
    db.commit()

    cursor.close()
    db.close()

def get_solutions(key: str) -> list:
    db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                             host='k953588c.beget.tech',
                             database='k953588c_physlab')
    cursor = db.cursor()
    
    solutions = []
    select = f"SELECT * FROM " + key
    cursor.execute(select)
    classkeys = [i[2] for i in cursor]
    # print(classkeys)
    for ck in classkeys:
        select = f"SELECT id, student_name, theme, desription, filename FROM {ck}_solutions"
        # print(f"SELECT id, student_name, theme, desription, filename FROM {ck}_solutions")
        cursor.execute(select)
        for id, sn, th, ds, fn in cursor:
            solution_dict = {"id": id, "student_name": sn, "theme": th, "filename": fn, "class_key": ck, "description": ds}
            solutions.append(solution_dict)
                
                
                
        
    db.commit()

    cursor.close()
    db.close()

    return solutions

def get_file_solution(filename: str, id: int, class_key: str) -> open:
    db = mysql.connector.connect(user='k953588c_physlab', password='Russianumber1',
                            host='k953588c.beget.tech',
                            database='k953588c_physlab')
    cursor = db.cursor()
    sql = f"SELECT filedata FROM {class_key}_solutions WHERE id = {id}"
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
    
    if filename.split(".")[-1] == "txt": system(f'notepad.exe {filename}')
    elif filename.split(".")[-1] == "docx": system(f'start winword.exe {filename}')
    
# get_solutions("IjQ3jCeO")
# get_file_solution("test_solution.txt", 1, "spvAOCofQ3")
# pprint(get_solutions("6i5i8q1g"))
# pprint(download_classes("6i5i8q1g"))