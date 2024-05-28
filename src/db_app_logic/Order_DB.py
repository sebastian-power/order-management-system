import sqlite3
from pathlib import Path

from order_app_logic_pkg.Customer import Customer
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
            statement = """INSERT INTO orders (order_date, customer_name, customer_email, order_items, item_price, item_qty, est_delivery, order_status) VALUES (?,?,?,?,?,?,?,?)"""
        elif isinstance(order, Order):
            statement = """INSERT INTO orders (order_date, customer_name, customer_email, order_items, item_price, item_qty) VALUES (?,?,?,?,?,?)"""

        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            if isinstance(order, Postal_Order):
                cursor.execute(
                    statement,
                    (
                        str(order.order_date),
                        order.customer.customer_name,
                        order.customer.customer_email,
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
                        order.customer.customer_name,
                        order.customer.customer_email,
                        self.i_names,
                        self.i_prices,
                        self.i_qtys,
                    ),
                )
                print("DONE" * 5)

            conn.commit()

    def add_customer_to_db(self, customer: Customer):
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

    def add_product_to_db(self, product_name, product_price):
        sql_product = (
            """INSERT INTO products (product_name, product_price) VALUES(?,?)"""
        )
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_product, (product_name, product_price))
            conn.commit()

    def initialise_db(self):
        sql_statements = [
            """CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            order_date TEXT,
            customer_id INTEGER,
            customer_name TEXT,
            customer_email TEXT,
            order_items TEXT,
            item_price TEXT,
            item_qty TEXT,
            est_delivery TEXT,
            order_status TEXT 
        );""",
            """CREATE TABLE IF NOT EXISTS products (
            product_name TEXT,
            product_price INT
        );""",
            """CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            customer_name TEXT,
            customer_email TEXT,
            customer_pwd TEXT,
        );""",
        ]
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            for statement in sql_statements:
                cursor.execute(statement)
            conn.commit()
