def greet(name):
    print(f"Welcome, {name}!")

greet("Malay")

def check_stock(item, stock_count):
    if stock_count>0:
        print(f"{item} is Available")
    else:
        print(f"{item} not Available")

check_stock("soda", 10)


def calculate_change(cost, money_given):
    change = money_given - cost
    return change

print("change amount is: ", calculate_change(450,500))