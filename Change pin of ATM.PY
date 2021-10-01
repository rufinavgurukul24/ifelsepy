atm=input("enter option on ATM screen")
if atm=="pin generation":
    print("go next")
    atm2=int(input("enter the bank account number"))
    if atm2==123456789011:
        print("ok,then go to next")
        atm3=int(input("enter the OTP received"))
        if atm3==1234:
            print("right!!")
            atm4=int(input("enter the NEW PASSWORD"))
            if atm4==1906:
                print("password changed!!")
            else:
                print("successfully down")

else:
    print("try again")