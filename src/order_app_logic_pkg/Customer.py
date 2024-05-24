from datetime import date, datetime


class Customer:
    this_year = datetime.now().year
    cust_id_base = "Cust_" + str(this_year)
    cust_num = 0  # ideally this should be initialized from a file

    def __init__(
        self,
        customer_name: type[str],
        customer_email: type[str],
        customer_pwd: type[str],
    ):
        Customer.cust_num += 1
        self.cust_id = str(Customer.cust_num)
        self.customer_email = customer_email
        self.customer_name = customer_name
        self.customer_pwd = customer_pwd

    @property
    def cust_id(self) -> type[str]:
        return self._cust_id

    @cust_id.setter
    def cust_id(self, customer_num: type[str]):
        self._cust_id = Customer.cust_id_base + "_" + customer_num

    @property
    def customer_name(self) -> type[str]:
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name: type[str]):
        if customer_name is not None and customer_name != "":
            self._customer_name = customer_name

    @property
    def customer_email(self) -> type[str]:
        return self._customer_email

    @customer_email.setter
    def customer_email(self, customer_email: type[str]):
        if (
            customer_email != None
            and len(customer_email) >= 6
            and "@" in customer_email
        ):
            self._customer_email = customer_email

    def view_my_orders(self):
        pass
        # search in databases for orders belongingto this customer
        # for each order found, call print_order(order_type)

    def print_orders(order_type):
        pass
        # if order: print using order.py method
        # if postal_order: print using postal_order.py method

    def __str__(self) -> type[str]:
        return (
            "Customer details are:\n"
            + f"Customer ID ={self.cust_id:20}"
            + f"Customer name ={self.customer_name:20}"
            + f"Customer email ={self.customer_email:30}\n"
        )
