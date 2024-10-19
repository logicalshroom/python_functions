# 2. The Shopping List Maker

# Objective: The aim of this assignment is to create a program that helps users make a shopping list.
# 
# Task 1: Write a function that lets the user add items to a list.
# 
# Task 2: Include a function to remove items from the list.
# 
# Task 3: Add a function that prints out the entire list in a formatted way.
# 
# Note: The goal of this is to be a program. The recommendation is to use a while loop that will allow the user to continue to add, remove, and print off their shopping list until they decide to "quit", also known as breaking the loop.

# First lets define our functions.

def add_list(item):
    shop_list.append(item)
    print(f"The item {item} has been added to your shopping list.")

def remove_list(item):
    shop_list.remove(item)
    print(f"The item {item} has been removed from your shopping list.")

def print_list():
    print(f"Your shopping list includes the following:")
    for items in range(len(shop_list)):
        print(shop_list[items])

shop_list = [] #Initiatize list

print("Welcome, User!\nThis program will help you make a shopping list.")
action = 1 

while action != 0: # Setting the action to 0 is how we will escape the While loop.
    if shop_list == []:
        print("There's nothing in the list yet!")
    else: #This should format it nicely.
        pass
    action = input("What action would you like to take?\nItem Options: Add, Remove, Print, or Close :")
    action = action.lower()
#    Create a nested if loop inside the while loop to execute actions, calling the functions from before.
    if action == "add":
        newitem = input("Please type in the item you'd like to add.")
        add_list(newitem)
    elif action == "remove":
        newitem = input("Please type in the item you'd like to remove.")
        remove_list(newitem)
    elif action == "print":
        print_list()
    elif action == "close":
        print("Okay, good bye!)")
        break #This kills the program
    else:
        print('Wonky input. Please be sure to type "Add, Remove, Print, or Close ."')