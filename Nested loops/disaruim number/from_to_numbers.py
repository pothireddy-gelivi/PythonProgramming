#WAP to print numbers from-number to to-number of disaruim numbers?

from_num=int(input("Enter the number: "))
to_num=int(input("Enter the number: "))
c=0
n=1
while c<to_num:
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
        if c>=from_num:
            print(n)
    n+=1