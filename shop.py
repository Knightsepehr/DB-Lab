import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="database1"
        )
        print("Connection to database successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def close_connection(connection):
    connection.close()

def add_product(product_id, product_name, category_id, price, quantity):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    INSERT INTO products (product_id, product_name, category_id, price, quantity) 
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (product_id, product_name, category_id, price, quantity))
    connection.commit()
    print("Product added successfully")
    close_connection(connection)

def add_category(category_id, category_name):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    INSERT INTO categories (category_id, category_name) 
    VALUES (%s, %s)
    """
    cursor.execute(query, (category_id, category_name))
    connection.commit()
    print("Category added successfully")
    close_connection(connection)

def remove_product(product_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    DELETE FROM products WHERE product_id = %s
    """
    cursor.execute(query, (product_id,))
    connection.commit()
    print("Product removed successfully")
    close_connection(connection)

def remove_category(category_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    DELETE FROM categories WHERE category_id = %s
    """
    cursor.execute(query, (category_id,))
    connection.commit()
    print("Category removed successfully")
    close_connection(connection)

def edit_product(product_id, product_name, category_id, price, quantity):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    UPDATE products 
    SET product_name = %s, category_id = %s, price = %s, quantity = %s
    WHERE product_id = %s
    """
    cursor.execute(query, (product_name, category_id, price, quantity, product_id))
    connection.commit()
    print("Product updated successfully")
    close_connection(connection)

def edit_category(category_id, category_name):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    UPDATE categories 
    SET category_name = %s
    WHERE category_id = %s
    """
    cursor.execute(query, (category_name, category_id))
    connection.commit()
    print("Category updated successfully")
    close_connection(connection)

def search_products(name_or_category):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    SELECT * FROM products WHERE product_name LIKE %s 
    OR category_id IN (SELECT category_id FROM categories WHERE category_name LIKE %s)
    """
    cursor.execute(query, ('%' + name_or_category + '%', '%' + name_or_category + '%'))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    close_connection(connection)

def search_categories(category_name):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    SELECT * FROM categories WHERE category_name LIKE %s
    """
    cursor.execute(query, ('%' + category_name + '%',))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    close_connection(connection)

def display_products():
    connection = create_connection()