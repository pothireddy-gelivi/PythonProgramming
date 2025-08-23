''' 
Infinte loop:
------------
1.Infinte loop is created by using while True.
2.if we are creating infinite loop externally.
'''
#Taking value inputs from the user until the given value is negative and add into list


l=[]
while True:
    n=int(input("Enter the number: "))
    if n<=0:
       break
    l.append(n)
print(l)