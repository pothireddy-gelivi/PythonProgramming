'''

'''

n=int(input("Enter the number of rows: "))
dummy=1
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(chr(64+dummy),end=" ")
        dummy+=5
    print()