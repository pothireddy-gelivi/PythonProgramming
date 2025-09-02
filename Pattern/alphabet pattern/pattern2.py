'''
A B C D E 
F G H I J
K L M N O
P Q R S T
U V W X Y
'''

n=int(input("Enter the number of rows: "))
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(chr(64+dummy),end=" ")
        dummy+=1
    print()