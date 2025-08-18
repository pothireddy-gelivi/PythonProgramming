#WAP to print prime numbers in a given range ?

ll=int(input("Enter the number: "))
ul=int(input("Enter the number: "))
for i in range(ll,ul+1):
    if i>1:
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            print(i)


