num1=input("enter the new id")
if num1=="0 to 9"or "a to z" or "@" or "other":
   password=input("enter the password")
   if password=="a to z" or "0 to 9" or "@" or "other":
     print("login succesfully")
   else:
      print("something went wrong")
else:
  print("try forgot password")