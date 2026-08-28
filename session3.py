#Write a Python program that takes your age as input and prints whether you are eligible to create an account on Instagram (must be 13 or older). Use if and else statements.
'''age = int(input("Enter your age: "))
if age >= 13:
    print("Eligible to create an Instagram account")
else:
    print("Not eligible to create an Instagram account")
'''

#Build a Python script that asks the user for their marks (0-100) and prints their grade based on this rule: 90+ = 'A', 75-89 = 'B', 60-74 = 'C', 40-59 = 'D', below 40 = 'F'. Use if, elif, and else.
'''marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 40:
    print("Grade D")

else:
    print("Grade F")
'''
#Create a Python program that checks if a person can order food from Zomato late at night: input age and current time (24-hour format). If age is 18 or above and time is between 22 (10pm) and 2 (2am), print 'Order allowed', else print 'Order not allowed'. Use nested if statements.\<br>\<br>\<em>\<strong>Hint:\</strong> Handle the time range that crosses midnight by checking if time >= 22 or time <= 2.\</em>

'''age = int(input("Enter your age: "))
time = int(input("Enter current time: "))
if age >= 18:

    if time >= 22 or time <= 2:
        print("Order allowed")
    else:
        print("Order not allowed")
else:
    print("Order not allowed")'''
#Write a Python program that takes your favorite cricket team's score as input and prints a message: if score is 200 or more, print 'High Score!', if between 150 and 199, print 'Good Score', if between 100 and 149, print 'Average', else print 'Needs Improvement'. Use if, elif, else.
score = int(input("Enter your team's score: "))

if score >= 200:
    print("High Score!")
elif score >= 150:
    print("Good Score")
elif score >= 100:
    print("Average")
else:
    print("Needs Improvement")