#WAP to print nth harsahd number?

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
        if c==target:
            print(n)
    n+=1