import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(connection,sql): #создание таблицы
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)
def insert_inf(connection,inf):  # добавление студентов
    try:
        sql = '''INSERT INTO store
        (title) 
        VALUES (?)'''
        cursor = connection.cursor()
        cursor.execute(sql, inf)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def all_print(connection,s_id):  # общий вывод
    try:
        sql = (f'SELECT products.title,categories.title,until_price, stock_quantity'
               f' FROM (products JOIN store ON products.store_id = store.store_id) JOIN categories '
               f'ON categories.code = products.category_code WHERE store.store_id = {s_id}')
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            return(row)
    except sqlite3.Error as e:
        print(e)

def store_print(connection): #вывод маркетов
    try:
        sql = '''SELECT store.store_id,store.title FROM store '''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

sql_to_create_store_table = '''
    CREATE TABLE store (
    store_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(10) NOT NULL
)
'''

sql_to_create_categories_table = '''
    CREATE TABLE categories (
    code VARCHAR (2) PRIMARY KEY,
    title VARCHAR(100) NOT NULL
)
'''
sql_to_create_products_table = '''
    CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    category_code VARCHAR(2) NOT NULL REFERENCES categories (code),
    until_price FLOAT(5,2) NOT NULL,
    stock_quantity INTEGER DEFAULT NULL,
    store_id INTEGER REFERENCES store (store_id)
)
'''

connect_to_db = create_connection('''examen.db''')
if connect_to_db is not None:
    # create_table(connect_to_db,sql_to_create_store_table)
    # create_table(connect_to_db, sql_to_create_products_table)
    # create_table(connect_to_db, sql_to_create_categories_table)
    # all_print(connect_to_db,3)
    # store_print(connect_to_db)
    connect_to_db.close()