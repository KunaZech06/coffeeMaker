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

machine_resource = {"ingredients": {
    "water": 2000,
    "milk": 2000,
    "coffee": 2000,
    "money_bag": 0
}
}

# TODO: 1. Prompt the user “What would you like? (espresso/latte/cappuccino):”. If report is typed, it should return
#  all the available resources.
# TODO: 2. Entering "off" should stop the program and turn off the machine.
# TODO: 3. Check resources sufficient?

money = dict(quarters=0.25, dimes=0.10, nickles=0.05, pennies=0.01)
off = False

while not off:
    # Get input choice from user
    userChoice = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()

    if userChoice == 'report':
        print(f"Water: {machine_resource['ingredients']['water']}ml")
        print(f"Milk: {machine_resource['ingredients']['milk']}ml")
        print(f"Coffee: {machine_resource['ingredients']['coffee']}g")
        print(f"Money: ${machine_resource['ingredients']['money_bag']}")

    elif userChoice == 'off':
        off = True

    else:
        # Declare required variables extracted from 'MENU' to make coffee.
        water = int(MENU[userChoice]['ingredients']['water'])
        coffee = int(MENU[userChoice]['ingredients']['coffee'])
        try:
            milk = int(MENU[userChoice]['ingredients']['milk'])
        except:
            milk = 0
        cost = int(MENU[userChoice]['cost'])

        if machine_resource['ingredients']['water'] < water:
            print("Sorry, there is not enough water.")
        elif machine_resource['ingredients']['coffee'] < coffee:
            print("Sorry, there is not enough coffee.")
        else:
            print(f"Please insert coins.\n")

            # Ask user to insert coins and calculate the amount inserted.
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            total = quarters * money["quarters"] + dimes * money["dimes"] + nickles * money["nickles"] + pennies * money['pennies']

            if total == cost:
                print("Here you go! Here is your coffee!")

                water_balance = machine_resource['ingredients']['water'] - water
                coffee_balance = machine_resource['ingredients']['coffee'] - coffee
                milk_balance = machine_resource['ingredients']['milk'] - milk
                machine_resource['ingredients']['water'] = water_balance
                machine_resource['ingredients']['coffee'] = coffee_balance
                machine_resource['ingredients']['coffee'] = milk_balance
                moneyAdd = machine_resource['ingredients']['money_bag'] + cost
                machine_resource['ingredients']['money_bag'] = moneyAdd

            elif total < cost:
                print("Sorry! That's not enough money. Money refunded.")
            elif total > cost:
                change = round(total - cost, 2)
                print(f"Here is your change of ${change}. Enjoy your coffee!")
                water_balance = machine_resource['ingredients']['water'] - water
                coffee_balance = machine_resource['ingredients']['coffee'] - coffee
                milk_balance = machine_resource['ingredients']['milk'] - milk
                machine_resource['ingredients']['water'] = water_balance
                machine_resource['ingredients']['coffee'] = coffee_balance
                machine_resource['ingredients']['coffee'] = milk_balance
                moneyAdd = machine_resource['ingredients']['money_bag'] + cost
                machine_resource['ingredients']['money_bag'] = moneyAdd
