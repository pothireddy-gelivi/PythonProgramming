#WAP to print sum of even index positions of all the even numbers present in a given string ?

string=input("Enter the numbers in a string: ")
s=0
ip=0
while ip<len(string):
    if int(string[ip])%2==0:
        s+=ip
    ip+=2
print(s)