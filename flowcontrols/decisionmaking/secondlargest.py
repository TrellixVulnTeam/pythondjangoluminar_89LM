num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
if(num1>num2)&(num1>num3)&(num2>num3):
    print("num2",num2,"is second higest")
elif(num1>num2)&(num1>num3)&(num3>num2):
    print("num3", num3, "is second higest")
elif(num2>num1)&(num2>num3)&(num1>num3):
    print("num1",num1,"is second highest")
elif(num2>num1)&(num2>num3)&(num3>num1):
    print("num3", num3, "is second highest")
elif(num3>num2)&(num3>num1) & (num2> num1):
    print("num2", num2, "is second highest")
elif (num3 > num2) & (num3 > num1) & (num1> num2):
    print("num1", num1, "is second highest")