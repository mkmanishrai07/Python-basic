import re
while  True:
    number =input("Please enter your number: ")
    if len(number) == 10 and number.isdigit():
        print("Valid input : ",number)
        if  re.fullmatch("^[0-9 \-]+$", number) : 
            print("Your numnber is Valid : ",number)
            break
        else:
            print("Your numnber is invalid : ",number)
    else:
        print("Invalid Input : ",number)