#WAP input=[12,11,17,21,5]
#output=["even"."prime","prime","odd","prime"]

list=eval(input("Enter the list: "))
nl=[]
ip=1
while ip<len(list)+1:
    if int(list[ip])%ip==0:
        if list[ip]%2==0:                      #wrong
            nl.append('even')
        else:
            nl.append('odd')
    ip+=1
else:
    nl.append('prime')  
print(nl)       
          
