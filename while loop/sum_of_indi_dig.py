#WAP to print the sum of individual digits of a given number?

#without changing input value
number=int(input("Enter the number: "))
dummy_number=number
s=0
while dummy_number>0:
    remainder=dummy_number%10
    s+=remainder
    dummy_number=dummy_number//10
print(s)

#changing input value
number=int(input("Enter the number: "))
s=0
while number>0:
    remainder=number%10
    s+=remainder
    number=number//10
print(s)