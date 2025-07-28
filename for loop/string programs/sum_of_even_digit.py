#WAP to find the sum of even digits present in the given string?

string=input("Enter the string: ")
summ=0
for element in string:
    if element.isdigit():
        if int(element)%2==0:
            summ+=int(element)
print(summ)