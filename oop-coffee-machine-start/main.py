from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def take_order():
    item = menu.get_items()
    order_name = input(f"What would you like? {item}:\n")
    if order_name == "off":
        print("Time for fixxing, powering off.")
        exit()
    elif order_name.lower() == "report":
        print(coffee_maker.report())
    elif menu.find_drink(order_name) == None:
        print("Item is not on the menu. Please choose again :)")
        take_order()
    else:
        return menu.find_drink(order_name)


def coffee_machine():
    order = take_order()
    if coffee_maker.is_resource_sufficient(order) == True:
        if money_machine.make_payment(order.cost) == True:
            coffee_maker.make_coffee(order)
            coffee_machine()
        else:
            print("Please order again.")
            coffee_machine()
    else:
        print("Sorry for the inconvenience, would you like to order again?")
        coffee_machine()
    

coffee_machine()
