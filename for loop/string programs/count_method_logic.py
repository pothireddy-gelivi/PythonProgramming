# WAP to print how manytimes given substring is present i given string?
#or
#implement count method logic?

string=input("Enter the string: ")
substring=input("Enter the substring: ")
count=0
for ele in string:
    if ele == substring:
        count+=1
print(count)