# Dictionary of Menu
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Resource we have for coffee
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Ask user what do they want

profit = 0 # To record the money we have or will make

# To grab the information from resource
water_resource = resources["water"]
milk_resource = resources["milk"]
coffee_resource = resources["coffee"]

is_on = True # check the coffe machine is on or off

while is_on:

    # ask user for their choice
    user_choice = input("What would you like? (expresso/latte/cappuccino): ").lower()
    
    # Turn off the coffee when management says it to off.
    if user_choice == "off":
        is_on = False 

    if user_choice == "report":
        print(f"Water: {water_resource}")
        print(f"Milk: {milk_resource}")
        print(f"Coffee: {coffee_resource}")
        print(f"Money: {profit}")