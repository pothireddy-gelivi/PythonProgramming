#WAP to print harshad number in a given range?

ll=int(input("Enter the number: "))
ul=int(input("Enter the number: "))
for i in range(ll,ul+1):
    s=0
    dn=i
    while dn>0:
        dl=dn%10
        s+=dl
        dn//=10
    if i%s==0:
        print(i)
    