'''
A B C D E 
A B C D E
A B C D E
A B C D E
A B C D E
'''

n=int(input("Enter the number of rows: "))
for row in range(1,n+1):
    dummy=1
    for col in range(1,n+1):
        print(chr(64+int(dummy)),end=" ")
        dummy+=1
    print()
    