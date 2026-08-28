#Write a Python script that asks the user for their name and favorite food using input(), then prints a welcome message like 'Hello Priya, your favorite food is Pizza!' using print().
"""name = input("Enter your name: ")
food = input("Enter your favorite food: ")
print("Hello", name, ", your favorite food is", food + "!")"""

#Create a small program that takes two numbers as input (use input()), converts them to integers using int(), and prints their sum, difference, product, and quotient using print().<br><br><em><strong>Hint:</strong> Remember to convert the input strings to integers before performing arithmetic operations.</em>
"""num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum =", num1 + num2)
print("Difference =", num1 - num2)
print("Product =", num1 * num2)
print("Quotient =", num1 / num2)"""

#Build a Zomato-style bill calculator: take the price of a food item and quantity as input, convert them to float and int, calculate the total bill, and display it with a message like 'Your total bill is ₹350.50'.
"""price = float(input("Enter food price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
print("Your total bill is ₹", total)
"""
#Write a script that asks the user for their Instagram follower count, converts it to an integer, and prints the count in a formatted string like 'You have 1,500 followers'. Use escape characters to add a new line and tab before the output.<br><br><em><strong>Hint:</strong> Use '\n' for new line and '\t' for tab in your print statement.</em>
"""followers = int(input("Enter your follower count: "))
print("\n\tYou have", format(followers, ","), "followers")"""

#Create a basic calculator program that takes two numbers and an operator (+, -, *, /) as input, performs the correct operation using typecasting, and prints the result. If the user enters an invalid operator, print an error message.\human
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result =", num1 + num2)

elif operator == "-":
    print("Result =", num1 - num2)

elif operator == "*":
    print("Result =", num1 * num2)

elif operator == "/":
    print("Result =", num1 / num2)

else:
    print("Invalid operator")