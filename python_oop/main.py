from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

on = True

while on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        on = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(choice)

        if coffee.enough_source(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)