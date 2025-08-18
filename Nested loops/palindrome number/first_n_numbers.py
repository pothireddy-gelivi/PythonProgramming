#WAP to print first n palindrome nubmers?

target=int(input("ENter the number: "))
n=1
c=0
while c<target:
    dn=n
    rev=0
    while dn>0:
        ld=dn%10
        rev=rev*10+ld
        dn//=10
    if rev==n:
        c+=1
        print(n)
    n+=1
