#WAP to print numbers from-number to to-numbers of armstrong numbers?

from_num=int(input("Enter the number: "))
to_num=int(input("Enter the number: "))
c=0
n=1
while c<to_num:
    dn=n
    s=0
    l=len(str(n))
    while dn>0:
        dl=dn%10
        s+=dl**l
        dn//=10
    if n==s:
        c+=1
        if c>=from_num:
            print(n)
    n+=1