'''

A B C D E 
B D F H J
C D E F G
D F H J L 
E F G H I 

'''

n=int(input("Enter the number of rows: "))
dummy=1
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(chr(64+dummy),end=" ")
        if row%2==0:
            dummy+=2
        else:
            dummy+=1
    print()
    dummy+=1