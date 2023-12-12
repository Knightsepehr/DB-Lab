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

def create_database(connection):
    cursor = connection.cursor()
    query = """
    CREATE DATABASE IF NOT EXISTS database1
    """
    cursor.execute(query)
    connection.commit()

def create_table(connection):
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS products (
        product_id INT AUTO_INCREMENT,
        product_name VARCHAR(255) NOT NULL,
        category_id INT,
        price DECIMAL(10, 2),
        quantity INT,
        PRIMARY KEY (product_id)
    )
    """
    cursor.execute(query)
    connection.commit()
    query = """
    CREATE TABLE IF NOT EXISTS categories (
        category_id INT AUTO_INCREMENT,
        category_name VARCHAR(255) NOT NULL,
        PRIMARY KEY (category_id)
    )
    """
    cursor.execute(query)
    connection.commit()

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
    
    
def test_add_category():
    add_category(1, 'Category 1')
    add_category(2, 'Category 2')
    add_category(3, 'Category 3')
    
def test_add_product():
    add_product(1, 'Product 1', 1, 10.50, 10)
    add_product(2, 'Product 2', 2, 15.00, 20)
    add_product(3, 'Product 3', 3, 20.50, 30)

if __name__ == "__main__":
    connection = create_connection()
    create_database(connection)
    create_table(connection)
    test_add_product()
    test_add_category()
    close_connection(connection)