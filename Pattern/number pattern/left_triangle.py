'''
            1  
         2  3
      4  5  6
   7  8  9  10
11 12 13 14 15
'''

n=int(input("Enter the number of rows: "))
spaces=n-1
stars=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print("  ",end=" ")
    for st in range(1,stars+1):
        if dummy<10:
            print(dummy,end="  ")
        else:
            print(dummy,end=" ")
        dummy+=1
    print()
    spaces-=1
    stars+=1