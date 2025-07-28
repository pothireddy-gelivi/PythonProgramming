#WAP to find the sum of the digits are present int he given string?

string=input("Enter the string: ")
summ=0
for element in string:
    if element.isdigit():
        summ+=int(element)
print(f"The total sum is {summ}")