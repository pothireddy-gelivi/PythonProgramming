#WAP to print how many digits are present in given string?

string=input("Enter the string: ")
count=0 #because if the input is 0, then we define count equal to 0
for ele in string:
    if ele.isdigit():
        count+=1
print(count)

#without using built in methods?

string1=input("Enter the string: ")
count1=0
for element in string1:
    if element > '0' and element < '9':
        count1+=1
print(count1)