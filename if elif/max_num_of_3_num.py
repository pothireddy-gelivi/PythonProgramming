#WAP to print maximum number among three numbers?

num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))
num3=int(input("Enter the number: "))
if num1>num2 and num1>num3:
    print(f"{num1} is maximum.")
elif num2>num3:
    print("{num2} is maximum.")
else:
    print(f"{num3} is maximum.")
