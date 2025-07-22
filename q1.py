
n=int(input("enter the rows:"))
for i in range(n):
    for j in range(i+1):
        print( ' ',end=" ")
    for k in range(i,n):
        print( '*',end=" ")
    for l in range(n,i,-1):
        print( '*',end=" ")   
    print()  

    