'''
        * 
      * *
    * * *
  * * * *
* * * * *
'''
#By using generic method

n=int(input("ENter the number of rows: "))
spaces=n-1
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    spaces-=1
    stars+=1

#By using single loop

n=int(input("ENter the number of rows: "))
for rows in range(1,n+1):
    print("  "*(n-rows)+"* "*(rows))

#By using normal method

n=int(input("Enter the number of rows: "))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col>=n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
