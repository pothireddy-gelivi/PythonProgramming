# WAP to print nth perfect number?

target=int(input("Enter the number:"))
c=0
n=1
while c<target:
    s=0
    for i in range(1,n//2+1):
        if n%i==0:
            s+=i
    if s==n:
        c+=1
        if c==target:
            print(n)
    n+=1