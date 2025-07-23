#for loop with string

string='pothireddy'
for element in string:
    print(element,end=" ")

#for loop with list
list=[11,22,33,44,'hai']
for element in list:
    print(element)

#for loop with tuple
tuple=11,22,33,44,55,66,[12,23]
for element in tuple:
    print(element)

#for loop with set
set={11,22,33,44,55,66,'hai'}
for element in set:
    print(element)

#for loop with dictionary
dictionary={'name':'pothireddy','age':23,'sex':'male'}
for keys in dictionary:
    print(keys)

#for loop with dictionary
dictionary={'name':'pothireddy','age':23,'sex':'male'}
for element in dictionary.items():
    print(element)

#for loop with dictionary
dictionary={'name':'pothireddy','age':23,'sex':'male'}
for key,value in dictionary.items():
    print(key,value)



