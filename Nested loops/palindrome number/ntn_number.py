#WAP to print nth palindrome number?

target=int(input("Enter the number: "))
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
        if c==target:
            print(n)
    n+=1
