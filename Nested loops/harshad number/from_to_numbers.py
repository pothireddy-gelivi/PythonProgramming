#WAP to print numbers from_number to to_number of harshad numbers?

from_num=int(input("Enter the number: "))
to_num=int(input("Enter the number: "))
c=0
n=1
while c<to_num:
    s=0
    dn=n
    while dn>0:
        dl=dn%10
        s+=dl
        dn//=10
    if n%s==0:
        c+=1
        if c>=from_num:
            print(n)
    n+=1