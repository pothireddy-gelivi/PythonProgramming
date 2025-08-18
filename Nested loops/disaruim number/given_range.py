#WAP to print disaruim numbers in a given range?

ll=int(input("Enter the number: "))
ul=int(input("Enter the number: "))
for i in range(ll,ul+1):
    s=0
    l=len(str(i))
    dn=i
    while dn>0:
        dl=dn%10
        s=s+dl**l
        dn//=10
        l-=1
    if s==i:
        print(i)