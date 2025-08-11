#WAP to check the given number is prime number or not?

number=int(input("Enter the number: "))
if number>1:
    for  i in range(2,number//2+1):
        if number%i==0:
            print("Not a prime number.")
            break
    else:
        print("Prime number.")
else:
    print("Not a prime number.")