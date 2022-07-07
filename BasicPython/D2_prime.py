# from sys import flags
p = int(input("Enter number : "))
flag =False
if p >1:
    for i in range(2,p):
        if(p%i) == 0:
            flag =True
            break
if flag:
    print(p,": is not prime number")
else:
    print(p,": is prime number")    
