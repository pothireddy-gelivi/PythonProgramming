#WAP to printhow many integers present in given list?

list=eval(input("Enter the list: "))
count=0
for element in list:
    if isinstance(element,int):#isinstance is used to check the data type is present.
        count+=1
print(count)