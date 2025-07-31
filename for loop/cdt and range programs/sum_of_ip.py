#WAP to print sum of index positions of all the consonents present in the string? 

string=input("Enter the string: ")
summ=0
for ip in range(len(string)):
    if string[ip].isalpha():
        if string[ip] not in 'aeiouAEIOU':
            summ+=ip
print(summ)
    