password=input("Enter the password:")
lower,upper,digit,symbol=0,0,0,0
valid = len(password)>=8
position = 0
if(len(password)>=8):
    for i in password:
        if(i.islower()):
            lower=lower+1
        if(i.isupper()):
            upper=upper+1
        if(i.isdigit()):
            digit=digit+1
            
        if(i=="@"or i=="$"or i=="#"or i=="-"or i=="_"):
            symbol=symbol+1

if(lower>=1 and upper>=1 and digit>=1 and symbol>=1 and lower+upper+digit+symbol==len(password)):

    print("The password is  valid .")
else:
    print("The password is  not valid .")
    