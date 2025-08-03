#WAP input=[11,22,33,10,222]
#    output=["odd","even","odd","even","even"]

#modifying list
list=eval(input("Enter the list: "))
ip=0
while ip<len(list):
    if list[ip]%2==0:
        list[ip]='even'
    else:
        list[ip]='odd'
    ip+=1
print(list)

#without modifying list
list=eval(input("Enter the list: "))
new_list=[]
ip=0
while ip<len(list):
    if list[ip]%2==0:
        new_list.append('even')
    else:
        new_list.append('odd')
    ip+=1
print(new_list)