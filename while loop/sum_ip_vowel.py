#WAP to print the sum of index positions of the vowels in a given string ?

string=input("Enter the string: ")
s=0
ip=0
while ip<len(string):
    if string[ip] in 'aeiouAEUIO':
        s+=ip
    ip+=1
print(s)