#WAP to print fatorial of a given nubmer?

number=int(input("Enter the number: "))
fact=1
for number in range(1,number+1):
    fact*=number
print(fact)