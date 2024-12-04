from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of the necessary classes
menu = Menu()  # Represents the menu containing all available drinks
coffee_maker = CoffeeMaker()  # Handles resource management and coffee-making logic
money_machine = MoneyMachine()  # Manages monetary transactions and tracking profits

# Main loop to run the coffee maker
is_on = True  # Flag to keep the machine running

while is_on:
    # Display available options to the user
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()

    # Handle user input
    if choice == "off":
        # Turn off the coffee machine
        is_on = False
    elif choice == "report":
        # Print reports for resources and money
        coffee_maker.report()
        money_machine.report()
    else:
        # Find the chosen drink from the menu
        drink = menu.find_drink(choice)
        if drink:
            # Check if resources are sufficient and process payment
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
