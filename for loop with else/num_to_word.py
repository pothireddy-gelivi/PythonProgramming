#WAP input=[12,11,17,21,5]
#output=["even"."prime","prime","odd","prime"]

list=eval(input("Enter the list: "))
nl=[]
for ele in list:
    if ele>1:
        for i in range(2,ele//2+1):
            if ele%i==0:
                if ele%2==0:
                    nl.append("even")
                else:
                    nl.append('odd')
                break
        else:
            nl.append("prime")
    else:
        nl.append('odd')
print(nl)