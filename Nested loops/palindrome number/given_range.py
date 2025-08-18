#WAP to print palindrome number in a given range?

ll=int(input("ENter the number: "))
ul=int(input("Enter the  number: "))

for i in range(ll,ul+1):
    rev=0
    dn=i
    while dn>0:
        ld=dn%10
        rev=rev*10+ld
        dn//=10
    if rev==i:
        print(i)