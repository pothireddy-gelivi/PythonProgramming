#WAP to replace all vowels with their index positions in a given string?

string=input("Enter the string: ")
new_string=''
for ip in range(len(string)):
    if string[ip] in 'aeiouAEIOU':
        new_string+=str(ip)
    else:
        new_string+=string[ip]
print(new_string)

