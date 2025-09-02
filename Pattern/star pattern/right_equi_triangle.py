'''
        * 
    * * * 
* * * * * 
    * * * 
        * 
'''

n=int(input("Enter the number of rows: "))
spaces=n-1
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    if row<=n//2:
        spaces-=2
        stars+=2
    else:
        spaces+=2
        stars-=2