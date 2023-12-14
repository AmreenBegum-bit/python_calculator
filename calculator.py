import os 
# Clearing the Screen
os.system('clear')


print("Welcome to the Calculator")
print("_" * 20)
answer = input("Is it Operation or Expression?? \n Enter: ").upper()
if answer == "OPERATION":
# operation = input("Enter an operation: ").upper()
    operations = ["ADD", "SUBTRACT", "MULTIPLICATION", "DIVISION"]
    operation = input("operation: ").upper()
    if operation in operations:
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))
        if operation == "ADD":
            print(num1 + num2)
        elif operation == "SUBTRACT":
            print(num1 - num2)
        elif operation == "MULTIPLICATION":
            print(num1 * num2)
        elif operation == "DIVISION":
            print(num1 / num2)
elif answer == "EXPRESSION":
    x = input("whats the expression?: ").split(" ")
    print(x)
else:
     print('No, sorry. Wrong operation') 


# ask operation or expression
# then if operation go down normal code flow
# if expression, then build out that path
# they type in 1 + 1
# you convert and solve
# https://stackoverflow.com/questions/1740726/turn-string-into-operator
