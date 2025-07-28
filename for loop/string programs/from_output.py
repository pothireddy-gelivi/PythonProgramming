#the input of the program is [11,20,'hai12','25',['bye',40],[10]]
# the output of the program is 56.

list=eval(input("Enter the list consist of different data types: "))
summ=0
for element in list:
    if isinstance(element,int):
        summ+=element
    elif isinstance(element,str) and element.isdigit():
        summ+=int(element)
print(summ)