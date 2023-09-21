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



def resource (order):
    """Check whether or not the resource is enough or not."""
    for item in order:
        if order[item]> resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True

def coins():
    '''Count the change and return in dollars'''
    quarter = int(input("How many quarter you want to insert?: "))
    dime = int(input("How many dime you want to insert?: "))
    nickel = int(input("How many nickel you want to insert?: "))
    penny = int(input("How many penny you want to insert?: "))

    total = quarter*0.25 + dime*0.1 + nickel*0.05 +penny*0.01
    return total

def enoughcoins(total, choice):
    '''Check if the coins are enough to get drink or not'''
    cost = MENU[choice]["cost"]
    if cost > total:
        print("Sorry not enough money. Money is refunded.")
        return False
    else:
        change = round(total - cost, 2)
        print(f"Here your change is ${change}.")
        return True

def make_coffe(drink, ingredients):
    '''Make coffee and deduct the resources we have'''
    for item in ingredients:
        resources[item] = resources[item] - ingredients[item]
    print(f"Here is your {drink}. Enjoy!!")


while is_on:
    # ask user for their choice
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    # Turn off the coffee when management says it to off.
    if user_choice == "off":
        is_on = False 

    # Give the report if the user ask for report
    elif user_choice == "report":
        print(f"Water: {water_resource}")
        print(f"Milk: {milk_resource}")
        print(f"Coffee: {coffee_resource}")
        print(f"Money: {profit}")
    
    
    else:
        drink = MENU[user_choice] # get the ingedrients from the data
        if resource (drink["ingredients"]): # check if we have enough resource
            print("We have enough resource.")
            print("Please insert coins.")
            total = coins() # get the total 
            if enoughcoins(total, user_choice): # check if we have enough coins
                make_coffe(user_choice, drink["ingredients"]) # serve the customer

        