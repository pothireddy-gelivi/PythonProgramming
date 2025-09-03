#WAP to check the given number is fabinocci series or not ?

#Fabinocci series:	A series where each number is the sum of the two preceding ones.

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
n=int(input("Enter the number: "))
if n==1:
    print(a)
elif n==2:
    print(a,b)
else:
    print(a,b)
    for i in range(n-2):
        print(a+b)
        a,b=b,a+b

