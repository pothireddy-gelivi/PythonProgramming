#WAP to print factorial of a given number by using while loop?

number=int(input("Enter the number: "))
fact=1
i=1
while i<number+1:
    fact*=i
    i+=1
print(fact)