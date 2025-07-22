#WAP to print relation between four numbers?

num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))
num3=int(input("Enter the number: "))
num4=int(input("Enter the number: "))
num5=int(input("Enter the number: "))
if num1==num2 and num1==num3 and num1==num4 and num1==num5:
    print("all numbers are equal.")
elif num1>num2 and num1> num3 and num1>num4 and num1>num5:
    print("num1  is greater than other number.")
elif num2>num3 and num2>num4 and num2>num5:
    print("num2 is greater than other number.")
elif num3>num4 and num3>num5:
    print("num3 is greater than other numbers.")
elif num4>num5:
    print("num4 is greater than other numbers.")
else:
    print("num5 is greater than other numbers.")
    