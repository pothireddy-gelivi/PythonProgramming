#WAP to print how many times given substring present in specified main string ?
 
string=input("Enter the string: ")
sub_string=input("Enter the sub string: ")
count=0
for ip in range(len(string)):
    if string[ip:ip+len(sub_string):]==sub_string:
        count+=1
print(count)


#another

string=input("Enter the string: ")
sub_string=input("Enter the sub string: ")
count=0
for ip in range(len(string)-len(sub_string)+1):
    if string[ip:ip+len(sub_string):]==sub_string:
        count+=1
print(count)