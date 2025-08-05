def say_Hello():
    print("Hello there")
    print("Welcome to our program")

say_Hello()

#Function arguments and parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Malay")

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}")
    print(f"It's name is {pet_name}")

describe_pet("dog", "tommy")

#Returning values from a function
def add_numbers(num1, num2):
    sum_result = num1+num2
    return sum_result

total = add_numbers(44,54)
print(f"The sum is {total}")
print(add_numbers(78,12))