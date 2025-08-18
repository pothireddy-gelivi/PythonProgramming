#WAP to print first n armstrong numbers?

target=int(input("Enter the number: "))
c=0
n=1
while c<target:
    dn=n
    s=0
    l=len(str(n))
    while dn>0:
        dl=dn%10
        s+=dl**l
        dn//=10
    if n==s:
        c+=1
        print(n)
    n+=1