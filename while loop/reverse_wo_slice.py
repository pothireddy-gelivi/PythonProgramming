#WAP to print a reverse a given string without using slicing by using while loop ?

string=input("Enter the string: ")
new_string=' '
ip=-1
while ip>-(len(string)+1):
    new_string+=string[ip]
    ip+=-1
print(new_string)
