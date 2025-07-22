#WAP to find maximum number among 3 numbers?

num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))
num3=int(input("Enter the number: "))
if num1>num2:
    if num1>num3:
        print(f"{num1} is maximum number.")
    else:
        print(f"{num3} is maximum number.")
else:
    if num2>num3:
        print(f"{num2} is maximum number.")
    else:
        print(f"{num3} is maximum number.")