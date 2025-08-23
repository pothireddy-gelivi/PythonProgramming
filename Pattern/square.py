'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
#By using generic method

n=int(input("Enter the number of rows: "))
for rows in range(1,n+1):
    for col in range(1,n+1):
        print("*",end=" ")
    print()   

#By using single loop
n=int(input("Enter the number of rows: "))
for row in range(1,n+1):
    print("* "*5)