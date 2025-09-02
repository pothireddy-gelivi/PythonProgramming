'''
1  2  3  4  5  
2  4  6  8  10  
3  4  5  6  7
4  6  8  10 12
5  6  7  8  9
'''

n=int(input("Enter the number of rows: "))
dummy=1
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end="  ")
        if row%2==0:
            dummy+=2
        else:
            dummy+=1
    print()    