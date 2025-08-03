#WAP to print even numbers in a given range by while loop ?

lower_limit=int(input("Enter the lower limit: "))
upper_limit=int(input("Enter the upper limit: "))
if lower_limit%2==1:
    lower_limit+1
ip=lower_limit
while ip<upper_limit+1:
    print(ip)
    ip+=2