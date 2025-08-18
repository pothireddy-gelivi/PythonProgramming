#WAP to print first n disaruim numbers?

target=int(input("Enter the number: "))
c=0
n=1
while c<target:
    s=0
    l=len(str(n))
    dn=n
    while dn>0:
        dl=dn%10
        s=s+dl**l
        dn//=10
        l-=1
    if s==n:
        c+=1
        print(n)
    n+=1