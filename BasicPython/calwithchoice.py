from secrets import choice


x = float(input("Enter First Value : "))
y = float(input("Enter Second Value : "))


choice = input("Enter 1 for addition.\nEnter 2 for subtraction.\nEnter 3 for muliplication.\nEnter 4 for division.\nEnter your Choice :")
choice = int(choice)

if choice == 1:
    print(f"You have entered x and y and Addition of their is : {x + y}")
elif choice == 2:
    print(f"You have entered x and y and subtraction of their is : {x - y}")
elif choice == 3:
    print(f"You have entered x and y and muliplication of their is : {x * y}")
elif choice == 4:
    print(f"You have entered x and y and division of their is : {x / y}")
else :
    print("You have choosed wrong :")