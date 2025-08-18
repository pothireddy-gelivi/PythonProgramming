#WAP to print first n prime number?

target=int(input("Enter the number: "))
n=2
c=0
while c<target:
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
        c+=1
        print(n)
    n+=1