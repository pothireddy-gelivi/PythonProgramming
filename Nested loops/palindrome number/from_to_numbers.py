#WAP to print number from-number to to-number of palindrome numbers?

from_num=int(input("Enter the number: "))
to_num=int(input("Enter the number: "))
n=1
c=0
while c<to_num:
    dn=n
    rev=0
    while dn>0:
        ld=dn%10
        rev=rev*10+ld
        dn//=10
    if rev==n:
        c+=1
        if c>=from_num:
            print(n)
    n+=1
