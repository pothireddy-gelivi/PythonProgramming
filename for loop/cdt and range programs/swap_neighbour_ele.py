#input=[11,22,33,44,55,66]
#output=[22,11,44,33,66,55]

list=eval(input("Enter the list: "))
for ip in range(0,len(list),2):
    list[ip],list[ip+1]=list[ip+1],list[ip]
print(list)

