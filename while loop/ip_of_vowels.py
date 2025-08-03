#WAP to print index positions of all the vowels present in a string by using while loop?

string=input("Enter the string: ")
new_string=' '
ip=0
while ip<len(string):
    if string[ip] in 'aeiouAEIOU':
        new_string+=str(ip)
    ip+=1
print(new_string)