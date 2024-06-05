from .Customer import Customer
from db_app_logic.Order_DB import Order_DB

class Admin(Customer):

    def __init__(self, name, email, pwd):
        super().__init__(name, email, pwd)
        self.dbmgt = Order_DB()

    def add_product(self, name, price):
        self.dbmgt.add_product_to_db(name, price)

    def remove_product(self, name):
        self.dbmgt.remove_product_from_db(name)
        
    def print_all_orders(self):
        order_list = self.dbmgt.view_all_orders()
        print("order_id,order_date,customer_id,order_items,item_price,item_qty,est_delivery,order_status")
        for order in order_list:
            print(order)
    
    def add_admin(self, name, email, pwd):
        self.dbmgt.add_admin_to_db(name, email, pwd)
        
