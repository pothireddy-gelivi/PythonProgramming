#WAP to print sum of index positions of the consonents present in a given string by using while loop?

string=input("Enter the string: ")
s=0
ip=0
while ip<len(string):
    if string[ip].isalpha():
        if string[ip] not in 'aeiouAEUIO':
            s+=ip
    ip+=1
print(s)