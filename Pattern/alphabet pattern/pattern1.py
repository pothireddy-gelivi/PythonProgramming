'''
A A A A A 
B B B B B
C C C C C
D D D D D
E E E E E
'''

n=int(input("Enter the number of rows: "))
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(chr(64+dummy),end=" ")
    print()
    dummy+=1