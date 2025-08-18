#WAP to print numbers from number to to number ?

from_number=int(input("Enter the number: "))
to_number=int(input("Enter the number: "))
c=0
n=2
while n<to_number:
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
        c+=1
        if c>=from_number:
            print(n)
    n+=1