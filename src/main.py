from datetime import datetime

from ui.Order_mgt_UI import Order_mgt_UI

if __name__ == "__main__":
    now = datetime.now()
    choice = 0
    while choice != "1" and choice != "2" and choice != "3":
        choice = input(
            "Would you like to:\n(1): Create a store order \n(2): Create a postal order?\n(3): Sign in as an admin?\n(4): Sign in as a customer?\n"
        )
    o_ui = Order_mgt_UI(choice)

    for order in o_ui.orders:
        print(str(order))

    if choice == "1":
        print("Thank you for your purchase. Have a nice day.")
    else:
        print("Thank you for your purchase. Your product will be arriving shortly.")


# Remove an item
# order.remove_item(item1)
# order.display_order()
