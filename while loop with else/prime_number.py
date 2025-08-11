# WAP to check the given number is prime number or not by using while loop with else?

number=int(input("Enter the number: "))
if number>1:
    i=2
    while i<number//2+1:
        if number%i==0:
            print("Not a prime number.")
            break
        i+=1
    else:
        print("Prime number.")
else:
    print("Not a prime number.")