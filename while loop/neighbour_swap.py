#WAP input=[11,22,33,44,55,66]
#    output=[22,11,44,33,66,55]


list=eval(input("Enter the list: "))
ip=0
while ip<len(list):
    list[ip],list[ip+1]= list[ip+1],list[ip]
    ip+=2
print(list)