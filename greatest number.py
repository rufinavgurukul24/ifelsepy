num_1=(input("enter the number"))
num_2=(input("enter the number"))
num_3=(input("enter the number"))
if num_1>num_2 and num_2<num_1:
    print(num_1,"is greatest number")
elif num_2>num_3 and num_3<num_2:
    print(num_2,"is greatest number")
elif num_3>num_1 and num_1<num_3:
    print(num_3,"is greatest number")
else:
    print("all are same")
