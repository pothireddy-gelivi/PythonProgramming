'''
1 6  11 16 21 
2 7  12 17 22
3 8  13 18 23
4 9  14 19 24
5 10 15 20 25
'''
n=int(input("Enter the number of rows: "))
dummy=1
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end=" ")
        dummy+=5
    print()
    dummy+=1