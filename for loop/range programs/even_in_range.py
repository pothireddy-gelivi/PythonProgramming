#WAP to print even number in a given number?
lower_limit=int(input("Enter the number: "))
upper_limit=int(input("Enter the number: "))
if lower_limit%2==1:
    lower_limit+=1
for number in range(lower_limit,upper_limit+1,2):
    print(number,end=" ")