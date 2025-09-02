'''
A B C D E 
A C E G I 
A D G J M 
A E I M Q 
A F K P U
'''

n=int(input("Enter the number of rows: "))
for row in range(1,n+1):
    dummy=1
    for col in range(1,n+1):
        print(chr(64+dummy),end=" ")
        dummy+=row
    print()
