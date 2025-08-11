#WAP to check given number is perfect number or not?

number=int(input("Enter the number: "))
s=0
for i in range(1,number//2+1):
    if number%i==0:
        s+=i
if s==number:
    print("Perfect Number")
else:
    print("not a perfect number")
