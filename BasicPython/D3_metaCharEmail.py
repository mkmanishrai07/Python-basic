# import email
# import re   
# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
# def check(email):   
#     if(re.fullmatch(regex,email)): 
#         print("Valid Email")   
#     else:   
#         print("Invalid Email")   
# if __name__ == '__main__':
      
#     email = input("Enter your Email : ")
#     check(email)   
import email
import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
while  True:
    email =input("Please enter your email: ")
    if  re.fullmatch(regex, email) : 
            print("Your email is Valid : ",email)
            break
    else:
        print("Your email is invalid : ",email)