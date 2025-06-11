import math 

def add(num1, num2):
    return num1 + num2 

def subtract(num1, num2):
    return num1 - num2 

def multiply(num1, num2):
    return num1 * num2 

def divide(num1, num2):
    if num2 == 0:
        return "You cannot divide by zero, silly!"
    return num1 / num2

print("--------------------------------------")
print("Welcome to the best calculator ever!")
print("--------------------------------------")
print("Please choose an operation you would like to use: \n+ Add\n- Subtract\n* Multiply\n/ Divide")


operation = input("Enter the operation you would like to use: ").lower()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == "+" or operation == "add":
    result = add(num1, num2)
elif operation == "-" or operation == "subtract":
    result = subtract(num1, num2)
elif operation == "*" or operation == "multiply":
    result = multiply(num1, num2)
elif operation == "/" or operation == "divide":
    result = divide(num1, num2)
else:
    result = "Invalid operation, you may use the list of operations shown above."
    
print(result)    
   