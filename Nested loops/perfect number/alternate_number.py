#WAP to print every 2nd perfect number in a range?

ll=int(input("Enter the number: "))
ul=int(input("Enter the number: "))
c=0
for i in range(ll,ul+1):
    s=0
    for j in range(1,i//2+1):
        if i%j==0:
            s+=j
    if s==i:
        c+=1
        if c%2==0:
            print(i)