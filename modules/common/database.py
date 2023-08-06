import sqlite3

class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'/Users/Yuliia/Desktop/QAAuto/QA_Auto_2023' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) VALUES ({product_id}, '{name}', '{description}', '{qnt}')"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = f"SELECT orders.id, customers.name, products.name, products.description, orders.order_date FROM orders JOIN customers ON orders.customer_id = customers.id JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    

    # Below there are methods created within the individual homework

    def insert_customers(self, id, name, address, city, postalCode, country):
        # to insert a data row into customers table
        try:
            query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) VALUES ({id}, '{name}', '{address}', '{city}', '{postalCode}', '{country}')"
            self.cursor.execute(query)
            self.connection.commit()
        except:
            return False
        else:
            return True
    
    def delete_customer_by_id(self, customer_id):
        # delete an entry in customers table
        query = f"DELETE FROM customers WHERE id = {customer_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_null_entries_customers(self):
        # find NULL values in customers table
        query = f"SELECT * from customers WHERE name IS NULL OR address IS NULL OR city IS NULL OR postalCode IS NULL OR country IS NULL"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_null_entries_products(self):
        # find NULL values in products table
        query = f"SELECT * from products WHERE name IS NULL OR description IS NULL OR quantity IS NULL"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_null_entries_orders(self):
        # find NULL values in orders table
        query = f"SELECT * from orders WHERE customer_id IS NULL OR product_id IS NULL OR order_date IS NULL"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_orders(self, customer_name):
        # get order entries for a customer
        query = f"SELECT c.id, c.name, o.id, o.order_date from orders o JOIN customers c ON o.customer_id = c.id WHERE c.name = '{customer_name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_info_no_orders(self):
        # get customers which have no orders at all (no entries in orders table)
        query = f"SELECT c.id, c.name from customers c LEFT JOIN orders o ON c.id = o.customer_id WHERE o.customer_id IS NULL"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_orders(self, id, customer_id, product_id, order_date):
        # insert an entry into orders table
        query = f"INSERT INTO orders (id, customer_id, product_id, order_date) VALUES ('{id}', '{customer_id}', '{product_id}', '{order_date}')"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_order(self, id):
        # delete an entry in orders table
        query = f"DELETE FROM orders WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_customer_by_parameter(self, parameter, value):
        # get a customer by specified parameter (or column)
        query = f"SELECT * FROM customers WHERE {parameter} = '{value}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def count_customers_by_country(self, country):
        # count number of customers living in a specific country
        query = f"SELECT COUNT(*) FROM customers WHERE country = '{country}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_maximal_stock(self):
        # get the product entry which has maximal stock (quantity)
        query = f"SELECT name, MAX(quantity) FROM products"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record