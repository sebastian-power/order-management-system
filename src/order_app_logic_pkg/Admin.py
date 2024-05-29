from .Customer import Customer
from db_app_logic.Order_DB import Order_DB

class Admin(Customer):

    def __init__(self):
        super.__init__()
        self.dbmgt = Order_DB()

    def add_product(self, name, price):
        self.dbmgt.add_product_to_db(name, price)

    def view_all_orders():
        pass
        #for each order: call print_order(order_type)
