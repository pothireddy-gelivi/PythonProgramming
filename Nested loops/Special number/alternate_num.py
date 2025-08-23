#WAP to print every 2nd number in a given range?

ll=int(input("Enter the number: "))
ul=int(input("Enter the number: "))
c=0
for i in range(ll,ul+1):
    s=0
    dn=i
    while dn>0:
        ld=dn%10
        dn//=10
        fact=1
        for j in range(1,ld+1):
            fact*=j
        s+=fact
    if s==i:
        c+=1
        if c%2==0:
            print(i)