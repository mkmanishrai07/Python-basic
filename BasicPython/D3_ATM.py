while True :
    print("Welcome to your favorate Bank : ")
    p = input("Please enter your 4 digit valid pin : ")
    u = input("Enter your name :")
    if len(p) == 4 and p.isdigit():
        print("Hii",u," How may i help you ?")
        
        choice = input("Enter 1 for Check Balance.\nEnter 2 for Case Withdraw.\nEnter 3 for Deposit.\nEnter your Choice :")
        choice = int(choice)
        balance = 25000
        
        if choice == 1:
            print(u,",Your available balance is :",balance)
        elif choice == 2:
            print("Enter amount which you want to withdraw : ")
            w = float(input())
            total = balance - w
            print("Withdraw successfully : ",w)
            print(u,",Available balance is : ",total)
            break
        elif choice == 3:
            print("Enter amount which you want to deposit : ")
            d = float(input())
            total = balance + d
            print("Deposit successfully :",d)
            print(u,",Available balance is : ",total)
            break
    else:
        print("Invalid pin:")
    exit()
    

