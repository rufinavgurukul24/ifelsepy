a=input("enter the characters")
b=input("enter the Digit")
c=input("enter the  Special character")
if a=="A-Z":
    print("it is alphabet")
    if b=="0-9":
        print("it is numerical")
    elif c=="@#":
        print ("it is specil charecter")
    else : 
        print("invailed")
else:
    print (a+b+c)
    print("strong password")