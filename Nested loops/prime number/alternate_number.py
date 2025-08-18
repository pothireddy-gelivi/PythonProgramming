#WAP to print every 2nd prime number in a given range?

ll=int(input("Enter the number: "))
ul=int(input("Enter the number: "))
c=0
for i in range(ll,ul+1):
    if i>1:
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            c+=1
            if c%2==0:
                print(i)
