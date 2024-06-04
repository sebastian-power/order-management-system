from order_app_logic_pkg.Customer import Customer
from order_app_logic_pkg.Order import Order
from order_app_logic_pkg.OrderItem import OrderItem
from order_app_logic_pkg.Postal_Order import Postal_Order
from order_app_logic_pkg.Products import Products
from db_app_logic.Order_DB import Order_DB
from order_app_logic_pkg.Admin import Admin


class Order_mgt_UI:

    def __init__(self, choice):
        # Get a mode(admin or customerc)
        self.cust_name = self.get_cust_name()
        self.cust_email = self.get_cust_email()
        self.db_manager = Order_DB()
        self.cust_pwd = self.get_cust_pwd()
        # testing below: Creation of a regular Order or a Postal Order
        if int(choice) == 1:
            self.orders = [self.create_order()]
        elif int(choice) == 2:
            self.orders = [self.create_postal_order()]
        elif int(choice) == 3:
            self.orders = [self.access_existing_orders()]
        elif int(choice) == 4:
            print("Signed in as admin.")
            self.adminUI()
            
            # self.adminUI()

        # self.orders=[self.create_order(), self.create_postal_order()]

    def get_cust_name(self) -> type[str]:
        done = False
        while not done:
            done = True
            # forbidden = [" ", "\n", "\r", "\t", "\b"]
            name = input("Enter your name. \nLength should be between 3-10 chars. ")
            if len(name) < 3 or len(name) > 10:
                print("Name should be between 3-10 characters (inclusive). Try again")
                done = False
            # Check if any forbidden characters are in the name
            #'any' returns true if any of the forbidden char is in name
            # elif any(a_char in name for a_char in forbidden):
            #         print("You have used white space characters. Try again")
            #         done=False
        return name
    
    def access_existing_orders(self):
        a_customer = Customer(self.cust_name, self.cust_email, self.cust_pwd)
        
        exists = self.db_manager.customer_id(self.cust_name, self.cust_email, self.cust_pwd)
        print(exists)
        if exists:
            a_customer.cust_id = int(exists)
            orders = a_customer.search_my_orders()
            for order in orders:
                print(order)
        else:
            print("Sorry, we could not find the user associated with these details.")
        return orders

        

    def get_cust_email(self) -> type[str]:
        done = False
        while not done:
            done = True
            forbidden = [" ", "\n", "\r", "\t", "\b"]
            email = input(
                "Enter your email. \n6-20 characters with an @. No white space chars allowed: "
            )
            if len(email) < 6 or len(email) > 20:
                print("Email should be between 6-20 characters. Try again")
                done = False
            elif any(a_char in email for a_char in forbidden):
                print("You have used white space characters. Try again")
                done = False
            elif email[0] == "@" or email.count("@") != 1 or email[-1] == "@":
                print("An in-between @ character expected in email. Try again")
                done = False
        return email

    def get_cust_pwd(self) -> type[str]:
        done = False
        while not done:
            done = True
            # forbidden = [" ", "\n", "\r", "\t", "\b"]
            name = input("Enter your password. \nLength should be between 5-20 chars. ")
            if len(name) < 5 or len(name) > 20:
                print("Password should be between 5-20 characters (inclusive). Try again")
                done = False
            # Check if any forbidden characters are in the name
            #'any' returns true if any of the forbidden char is in name
            # elif any(a_char in name for a_char in forbidden):
            #         print("You have used white space characters. Try again")
            #         done=False
        return name

    def create_postal_order(self) -> Postal_Order:
        a_customer = Customer(self.cust_name, self.cust_email, self.cust_pwd)
        a_postal_order = Postal_Order(a_customer)
        done = False
        while not done:
            done = True
            a_postal_order.add_item(self.create_order_item())
            correct_more = False
            while not correct_more:
                correct_more = True
                more = input("Do you want to order another item Y/N: ")
                more = more.strip()
                if more not in ["Y", "y", "N", "n"]:
                    print("You did not enter Y or N. Please try again")
                    correct_more = False
            if more in ["Y", "y"]:
                done = False
        a_postal_order.set_delivery_date()
        a_postal_order.customer.cust_id = self.db_manager.add_customer_to_db(a_postal_order.customer)
        a_postal_order.order_id = self.db_manager.add_order_to_db(a_postal_order)
        return a_postal_order

    def create_order(self) -> Order:

        a_customer = Customer(self.cust_name, self.cust_email, self.cust_pwd)
        an_order = Order(a_customer)
        done = False
        while not done:
            done = True
            an_order.add_item(self.create_order_item())
            correct_more = False
            while not correct_more:
                correct_more = True
                more = input("Do you want to order another item Y/N: ")
                more = more.strip()
                if more not in ["Y", "y", "N", "n"]:
                    print("You did not enter Y or N. Please try again")
                    correct_more = False
            if more in ["Y", "y"]:
                done = False
        self.db_manager.add_order_to_db(an_order)
        return an_order

    def create_order_item(self) -> OrderItem:
        item_id = None
        item_name = None
        item_unit_price = None
        item_qty = None
        p = Products()
        print(str(p))  # Available products
        correct_choice = False
        while not correct_choice:
            correct_choice = True
            choice = input("Enter your choice 1-4: ")
            if choice not in ["1", "2", "3", "4"]:
                print("Your entry was incorrect. Try again")
                correct_choice = False
        item_id = int(choice)
        item_name = p.get_attr("name", item_id)
        item_unit_price = int(p.get_attr("unit_price", item_id))

        correct_qty = False
        while not correct_qty:
            correct_qty = True
            item_qty = input("Input the quanity. Positive integers only: ")

            try:
                item_qty = int(item_qty)
                if item_qty < 0:
                    print("You did not enter a positive integer. Try again")
                    correct_qty = False
            except ValueError:
                print("You did not enter an integer. Try again")
                correct_qty = False

        anItem = OrderItem(item_name, item_unit_price, item_qty)

        return anItem
    
    def adminUI(self):
        self.admin = Admin(self.cust_name, self.cust_email, self.cust_pwd)
        action = int(input("Would you like to:\n(1): Add a product to the database?\n(2): Remove a product from the database?\n(3): View all orders?\n"))
        if action == 1:
            name = input("Enter the new product name: ")
            price = int(input("Enter the new product price:"))
            self.admin.add_product(name, price)
        elif action == 2:
            name = input("Enter the product name: ")
            self.admin.remove_product(name)
        elif action == 3:
            self.admin.print_all_orders()

