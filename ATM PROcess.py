num=input("enter the ATM card")
if num=="card"  :
    print("welcome")
    num2=input("enter the language")
    if num2=="english,hindi,marathi,etc":
        print("ok, fast")
        num3=int(input("enter 4 digit number"))
        if num3==4638:
            print("correct pin")
            num4=input("enter the transaction")
            if num4=="cash withdrawal":
                print("go to next")
                num5=input("enter the account")
                if num5=="saving account":
                    print("good")
                    num6=int(input("enter the withdrawal money"))
                    if num6==1000:
                        print("okk")
                        num7=input("enter to take the cash")
                        if num7=="yes":
                            print("go forth")
                            num8=input("enter to take a printed receipt")
                            if num8=="got the receipt":
                                print(" visit again..")
                            else:
                                print("error")    
                        else:
                            print("no option") 
                    else:
                        print("no money") 
                else:
                    print("no account")
            else:
                print("trasver") 
        else:
            print("lost") 
    else:
        print("hindi") 
else:
    print("try again")                                                   