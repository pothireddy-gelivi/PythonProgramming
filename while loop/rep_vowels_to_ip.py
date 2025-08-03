#WAP to replace all vowels with their index positions ina given string by using while loop ?

string=input("Enter the string: ")
new_string=' '
ip=0
while ip<len(string):
    if string[ip] in 'aeiouAEIOU':
        new_string+=str(ip)
    else:
        new_string+=string[ip]
    ip+=1
print(new_string)

