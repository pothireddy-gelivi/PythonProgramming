#WAP to print how many consonents are present in given string?

string=input("Enter the string: ")
count=0
for element in string:
    if element.isalpha() and element.lower() not in 'aeiou':
        count+=1
print(count)