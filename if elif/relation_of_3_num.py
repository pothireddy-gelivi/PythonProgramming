#WAP to print relation between three numbers?

num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))
num3=int(input("Enter the number: "))
if num1==num2 and num1==num3:
    print("all numbers are equal.")
elif num1>num2 and num1> num3:
    print("num1  is greater than other number.")
elif num2>num3:
    print("num2 is greater than other number.")
else:
    print("num3 is greater than other number.")
    