# Calculator with (+,-,*,/) these operators

num1 = int(input("Enter first number:> "))
num2 = int(input("Enter second number:> "))

operator = input("Enter operator (+, -, *, /):> ")

if operator == "+":
    print("Addition:", num1 + num2)

elif operator == "-":
    print("Subtraction:", num1 - num2)

elif operator == "*":
    print("Multiplication:", num1 * num2)

elif operator == "/":
    print("Division:", num1 / num2)

else:
    print("Invalid operator")









