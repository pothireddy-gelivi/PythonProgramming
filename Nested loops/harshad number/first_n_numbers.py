#WAP to print first n harshad numbers?

target=int(input("Enter the number: "))
c=0
n=1
while c<target:
    s=0
    dn=n
    while dn>0:
        dl=dn%10
        s+=dl
        dn//=10
    if n%s==0:
        c+=1
        print(n)
    n+=1