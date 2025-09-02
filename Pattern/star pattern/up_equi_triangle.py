'''
* * * * * 
  * * * 
    * 
'''

n=int(input("Enter the number of rows: "))
spaces=0
stars=n
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    spaces+=1
    stars-=2