#WAP to print nth numbers?

target=int(input("Enter the number: "))
c=0
n=1
while c<target:
    dn=n
    s=0
    while dn>0:
        ld=dn%10
        dn//=10
        fact=1
        for i in range(1,ld+1):
            fact*=i
        s+=fact
    if s==n:
        c+=1
        if c==target:
            print(s)
    n+=1