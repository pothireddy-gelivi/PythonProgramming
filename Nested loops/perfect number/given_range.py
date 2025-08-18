#WAP to print perfect number in a given range ?

ll=int(input("Enter the number: "))
ul=int(input("Enter the number: "))
for i in range(ll,ul+1):
    s=0
    for j in range(1,i//2+1):
        if i%j==0:
            s+=j
    if s==i:
        print(i)