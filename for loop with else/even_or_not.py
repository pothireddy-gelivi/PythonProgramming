# WAP to check given list has a even number or not ?
#if it has print YES.
#otherwise print NO.

list=eval(input("Enter the list :"))
ip=0
for i in list:
    if i%2==0:
        print("YES")
        break
    
else:
    print("NO")