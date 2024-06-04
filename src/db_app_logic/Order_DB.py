import sqlite3
from pathlib import Path

from order_app_logic_pkg.Order import Order
from order_app_logic_pkg.Postal_Order import Postal_Order


class Order_DB:

    def __init__(self) -> None:
        self.dbpath = [i for i in Path(__file__).resolve().parents][2].joinpath(
            str(Path("assets/data_files/order_system.db"))
        )
        try:
            with sqlite3.connect(self.dbpath) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM orders")
        except sqlite3.OperationalError:
            self.initialise_db()
        # check if order_management system exists, if not run init file to create tables

    def add_order_to_db(self, order):
        self.i_names = ""
        for item in order.items:
            self.i_names += f"{item.name},"
        self.i_prices = ""
        for item in order.items:
            self.i_prices += f"{item.price},"
        self.i_qtys = ""
        for item in order.items:
            self.i_qtys += f"{item.qty},"
        if isinstance(order, Postal_Order):
            statement = """INSERT INTO orders (order_date, customer_id, order_items, item_price, item_qty, est_delivery, order_status) VALUES (?,?,?,?,?,?,?)"""
        elif isinstance(order, Order):
            statement = """INSERT INTO orders (order_date, customer_id, order_items, item_price, item_qty) VALUES (?,?,?,?,?)"""
        cust_id_searched = self.customer_id(order.customer.customer_name, order.customer.customer_email, order.customer.customer_pwd)
        if cust_id_searched:
            order.customer.cust_id = cust_id_searched
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            if isinstance(order, Postal_Order):
                cursor.execute(
                    statement,
                    (
                        str(order.order_date),
                        order.customer.cust_id,
                        self.i_names,
                        self.i_prices,
                        self.i_qtys,
                        order.o_delivery_date,
                        order.current_state,
                    ),
                )
                print("DONE" * 3)
            elif isinstance(order, Order):
                cursor.execute(
                    statement,
                    (
                        str(order.order_date),
                        order.customer.cust_id,
                        self.i_names,
                        self.i_prices,
                        self.i_qtys,
                    ),
                )
                print("DONE" * 5)

            conn.commit()
            id_data = cursor.execute(
                "SELECT order_id FROM orders WHERE order_date =?",
                (str(order.order_date),),
            )
            return id_data.fetchone()[0]

    def add_customer_to_db(self, customer) -> int:
        sql_cust = """INSERT INTO customers (customer_name, customer_email, customer_pwd) VALUES(?,?,?)"""
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            cursor.execute(
                sql_cust,
                (
                    customer.customer_name,
                    customer.customer_email,
                    customer.customer_pwd,
                ),
            )
            conn.commit()
            id_data = cursor.execute(
                "SELECT customer_id FROM customers WHERE customer_name =?",
                (customer.customer_name,),
            )
            return id_data.fetchone()[0]

    def add_product_to_db(self, product_name, product_price):
        sql_product = (
            """INSERT INTO products (product_name, product_price) VALUES(?,?)"""
        )

        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_product, (product_name, product_price))
            conn.commit()
        print(f"'{product_name}' added successfully")

    def remove_product_from_db(self, product_name):
        sql_product = """DELETE FROM products WHERE product_name=?"""
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_product, (product_name,))
            conn.commit()
        print(f"'{product_name}' removed successfully")

    def view_all_orders(self):
        sql_all = "SELECT * FROM orders"
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            all_orders = cursor.execute(sql_all)
            return all_orders.fetchall()
    
    def customer_id(self, customer_name, customer_email, customer_pwd):
        sql_cus = """SELECT customer_id FROM customers WHERE customer_name=? AND customer_email=? AND customer_pwd=?"""
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            customer_id = cursor.execute(sql_cus, (customer_name, customer_email, customer_pwd))
            order_done = customer_id.fetchone()[0]
            if order_done is not None:
                return order_done
            else:
                return None
    
    def search_customer_orders(self, customer_id):
        sql_all = """SELECT * FROM orders WHERE customer_id=?"""
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            all_orders = cursor.execute(sql_all, (customer_id,))
            return all_orders
    
    def get_customer_from_id(self, customer_id):
        sql_all = """SELECT * FROM customers WHERE customer_id=?"""
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            cust_info = cursor.execute(sql_all, (customer_id,)).fetchone()
            return cust_info


    def initialise_db(self):
        sql_statements = [
            """CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY,
            order_date TEXT,
            customer_id INTEGER,
            order_items TEXT,
            item_price TEXT,
            item_qty TEXT,
            est_delivery TEXT,
            order_status TEXT 
        );""",
            """CREATE TABLE products (
            product_name TEXT,
            product_price INT
        );""",
            """CREATE TABLE customers (
            customer_id INTEGER PRIMARY KEY,
            customer_name TEXT,
            customer_email TEXT,
            customer_pwd TEXT
        );""",
        ]
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            for statement in sql_statements:
                cursor.execute(statement)
            conn.commit()
