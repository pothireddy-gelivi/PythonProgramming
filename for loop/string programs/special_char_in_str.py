# WAP to check how many special characters are present in the given string?

string=input("Enter the string: ")
count=0
for element in string:
    if element.isalnum()==False:
        count+=1
print(count)