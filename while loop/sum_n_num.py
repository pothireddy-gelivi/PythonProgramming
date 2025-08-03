#WAP to print the sum of first n numbers using while loop?

number=int(input("Enter the number: "))
s=0
ip=1
while ip<number+1:
    s+=ip
    ip+=1
print(s)