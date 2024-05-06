from ui.Order_mgt_UI import Order_mgt_UI
if __name__ == "__main__":
    choice = 1
    while choice != "1" and choice != "2":
        choice = input("Would you like to create:\n(1): A store order \n(2): A postal order?\n")
    o_ui=Order_mgt_UI(choice)

    for order in o_ui.orders:
        print(str(order))

         
#Remove an item
#order.remove_item(item1)
#order.display_order()
