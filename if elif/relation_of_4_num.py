#WAP to print relation between four numbers?

num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))
num3=int(input("Enter the number: "))
num4=int(input("Enter the number: "))
if num1==num2 and num1==num3 and num1==num4:
    print("all numbers are equal.")
elif num1>num2 and num1> num3 and num1>num4:
    print("num1  is greater than other number.")
elif num2>num3 and num2>num4:
    print("num2 is greater than other number.")
elif num3>num4:
    print("num3 is greater than other numbers.")
else:
    print("num4 is greater than other numbers.")
    