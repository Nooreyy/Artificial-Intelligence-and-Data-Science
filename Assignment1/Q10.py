'''Mini Calculator Using Loop

Create a calculator that:
Takes two numbers
Takes operator (+, -, *, /)
Prints result
Repeats until user enters "exit"'''


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
opr = input("Enter an operator (+, -, *, /) or press '1' to quit: ")
while opr != '1':
    if opr == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif opr == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif opr == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif opr == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operator. Please enter a valid operator (+, -, *, /).")
    
    opr = input("Enter an operator (+, -, *, /) or 'press 1' to quit: ")
