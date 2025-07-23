#WAP to print how many vowels are present in given string?

string=input("Enter the string: ")
count=0
for element in string:
    if element in 'aeiouAEIOU':
        count+=1
print(count)