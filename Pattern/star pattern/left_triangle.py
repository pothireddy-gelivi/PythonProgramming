'''
* 
* *
* * *
* * * *
* * * * *
'''
#By using generic method

n=int(input("Enter the number of rows: "))
stars=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    stars+=1

#By using single loop

n=int(input("Enter the number of rows: "))
for row in range(1,n+1):
    print("* "*row)

#By using normal method

n=int(input("Enter the number: "))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row>=col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()