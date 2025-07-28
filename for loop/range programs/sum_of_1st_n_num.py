#WAP to print the sum of first n numbers?
upper_limit=int(input("Enter the upper limit: "))
summ=0
for number in range(1,upper_limit+1):
    summ+=number
print(summ)