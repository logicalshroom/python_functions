# Objective 1

'''
1. The Calculator App
Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

Task 1: Create functions for each arithmetic operation.

Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.
'''

# Okay so honestly, finishing the objectives is way faster if I just complte the tasks all at once. Following, is my functional code. I've commented out some tests I've shown and my thought process on everything.

# 1. Build each math function

# I want to be able to pass a lot of numbers at once so I think I will use *args to build this.

def add(*args):
    result = 0 # We can start the counter at 0...
    for num in args:
        result += num #and then add another arg each iteration
    return result #and then return the counter variable

def sub(*args): #Basically the same thing here
    result = args[0] #Hmm, my last method wont really work here so lets change it up a little
    for num in args[1:]: #This will set results to the first argument, and num to the second argument
        result -= num #then we can iterate as normal :)
    return result

def mult(*args):
    result = 1 #Multiplying by one is okay since it wont change the result
    for num in args:
        result *= num
    return result

def div(*args):
    result = args[0] #We dont wanna make fractions so, lets set the result to be the first argument...
    for num in args[1:]: #we will need to specify that we start iterating on the second argument, since we have set the first arge to = results
        try:
            result /= num #and, we will start with the second arg.
        except: #If Python outputs an error, return the following. This will handle either a single arg being passed, or, a 0.
            return("I'm sorry Dave, I'm afraid I can't do that.")
    return result

# I commented out some tests I ran here.

# print(division(6,90,3)) #Ensuring this can handle multiple args: Output should be .02 repeating

# print(multiply(4,5,2)) #Testing: Output should be 40

# print(add(10,9,10,0)) #Testing: Output should be 29

# print(division(4,0)) #Testing: Output should be my error message :)

# print(sub(10,5,30)) #Testing: Output should be -25

# print(sub(10)) #10 minus nothing is indeed 10 so I think accepting a single arg here is fine. If I'm wrong for that let me know and I'll go ahead and tidy it up LOL

# Now we can ask the user for an input.

math_choice = input("Please select the mathematical function you'd like to use.\nAdd, Substract, Multiply, or Divide? \n")

if math_choice == "Add" or math_choice == "add": #I asked my partner to test my code and they wanted a lowercase inout to be accepted, so I added the line RQ
    arguments = list(map(float, input("Please input the numbers you'd like to add, separated with a space.").split()))
    print(add(*arguments)) #We can use map and input.split to force the user input into a neat little integer list.
elif math_choice == "Subtract" or math_choice == "subtract":
    arguments = list(map(float,input("Please input the numbers you'd like to subtract, separated with a space.").split()))
    print(sub(*arguments))
elif math_choice == "Multiply" or math_choice == "multiply":
    arguments = list(map(float,input("Please input the numbers you'd like to multiply, separated with a space.").split()))
    print(mult(*arguments))
elif math_choice == "Divide" or math_choice == "divide":
    arguments = list(map(float,input("Please input the numbers you'd like to divide, separated with a space.").split()))
    print(div(*arguments))
else:
    print("Whoops, weird input. I'm going on break. Run the program from the top to try again.")



