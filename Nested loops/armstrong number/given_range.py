#WAP to print armstrong numbers in a given range?

ll=int(input("Enter the number: "))
ul=int(input("Enter the number: "))
for i in range(ll,ul+1):
    dn=i
    s=0
    l=len(str(i))
    while dn>0:
        ld=dn%10
        s=s+ld**l
        dn//=10
    if i==s:
        print(i)

    
