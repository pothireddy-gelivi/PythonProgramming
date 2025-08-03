#input=[11,22,33,10,222]
#output=['odd','even',"odd","even","even"]
# without modifying existing list

list=eval(input("Enter the list: "))
new_list=[]
for ip in range(len(list)):
    if int(list[ip])%2==0:
        new_list.append('even')
    else:
        new_list.append('odd')
print(list)
print(new_list)

#modifying existing list

list=eval(input("Enter the list: "))
for ip in range(len(list)):
    if int(list[ip])%2==0:
        list[ip] ='even'
    else:
         list[ip] ='odd'
print(list)

