'''
* * * * * 
  * * * *
    * * *
      * *
        *
'''
#By using generic method
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
    stars-=1

#by using normal method 

n=int(input("Enter the number of rows: "))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row<=col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#by using single loop

n=int(input("Enter the number of rows: "))
for row in range(1,n+1):
    print("  "*(row-1)+"* "*(n-row+1))