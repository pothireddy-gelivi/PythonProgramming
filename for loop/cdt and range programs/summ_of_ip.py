#WAP to print sum of even index positions of all the even numbers present in the given string?

string=input("Enter the string: ")
summ=0
for ip in range(len(string)):
    if string[ip].isdigit():
        if int(string[ip])%2==0 and ip%2==0:
            summ+=ip
print(summ) 
            


