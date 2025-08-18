#WAP to print nth prime number?

Target=int(input("Enter the number: "))
n=2
c=0
while c<Target:
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
        c+=1
        if c==Target:
            print(n)
    n+=1