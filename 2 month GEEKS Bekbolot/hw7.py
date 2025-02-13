import sqlite3

connection = sqlite3.connect('''db.db''')


def create_table(connection,sql): #создание таблицы
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def select_student_last_name(connection):
    try:
        sql = '''SELECT * FROM students WHERE LENGTH(last_name) > 10'''
        cursor = connection.cursor()
        cursor.execute(sql,)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def update_students_name(connection):
    try:
        sql = '''UPDATE students SET name = 'genius' WHERE marks > 10'''
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def select_student_genius(connection):
    try:
        sql = '''SELECT * FROM products WHERE name LIKE 'genius' '''
        cursor = connection.cursor()
        cursor.execute(sql,)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


sql_to_create_students_table = '''
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    hobby VARCHAR(255) NOT NULL DEFAULT NULL,
    birthday INTEGER NOT NULL,
    marks INTEGER NOT NULL DEFAULT 0
)
'''

def delete_students(connection):
    try:
        sql = '''DELETE FROM products WHERE id % 2 = 0'''
        cursor = connection.cursor()
        cursor.execute(sql,)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


connect_to_db = connection
if connect_to_db is not None:
    print('Connection succesfully!')
    select_student_last_name(connect_to_db)
    select_student_genius(connect_to_db)
    update_students_name(connect_to_db)
    delete_students(connect_to_db)
    # create_table(connect_to_db, sql_to_create_students_table)