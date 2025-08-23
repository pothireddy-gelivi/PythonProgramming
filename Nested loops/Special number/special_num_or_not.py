#WAP to check the number is special number or not?
'''if the given number is equal to sum of individual digits factorial then we call number as special numbers'''


n=int(input("Enter the number: "))
s=0
dn=n

while dn>0:
    ld=dn%10
    dn//=10
    fact=1
    for i in range(1,ld+1):
        fact*=i
    s+=fact
if s==n:
    print("special number")
else:
    print("not a special number")