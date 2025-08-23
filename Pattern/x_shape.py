'''
*       * 
  *   *
    *
  *   *
*       *
'''
#By using generic method

n=int(input("Enter the number of rows: "))
for row in range(1,n+1):
    for col in range(1,n+1):
        if col==row or row+col==n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()