#WAP to print summ of odd index positions all the even numbers present in the given list?

list=eval(input("Enter the list: "))
summ=0
for ip in range(1,len(list),2):
    if list[ip] %2==0:
        summ+=int(ip)
print(summ)

