from menu import Menu, MenuItem
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_machine = CoffeeMaker()
menu = Menu()

coffe_machine.report()
money_machine.report()

is_on = True

while is_on:
	options = menu.get_items()
	choice = input(f"What would you like? ({options}): ")
	if choice == "off":
		is_on = False
	elif choice == "report":
		coffe_machine.report()
		money_machine.report()
	else:
		drink = menu.find_drink(choice)
		if coffe_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
			coffe_machine.make_coffee(drink)
