#WAP to print the relation between two numbers?

num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))
if num1==num2:
    print(f"{num1} and {num2} are Equal numbers.")
elif num1>num2:
    print(f"{num1} is grater than {num2}")
else:
    print(f"{num2} is greater than {num1}")
    