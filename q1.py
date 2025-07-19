''''n=int(input())

if n%2 ==0:
    if n>=2 and n<=5:
        print("Not Weird")
    elif n>=5 and n<=20:
        print("Wierd")
    elif n>20:
        print("Not Wierd")
else:
    print("Wierd") '''

n=int(input("enter the rows:"))
for i in range(n):
    for j in range(i+1):
        print( ' ',end=" ")
    for k in range(i,n):
        print( '*',end=" ")
    for l in range(n,i,-1):
        print( '*',end=" ")   
    print()  

    