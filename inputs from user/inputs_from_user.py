#4
#60,70,80,90
#[60,70,80,90]
#90
#Taking n input values from user and add into list

n=int(input("Enter the value: "))
l=[]
for i in range(n):
    value=int(input("ENter the number: "))
    l.append(value)
print(l)