'''

'''

n=int(input("Enter the number of rows: "))
spaces=n-1
stars=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print(chr(64+dummy),end=" ")
        dummy+=1
    print()
    spaces-=1
    stars+=1