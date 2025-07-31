#WAP to print sum of even digits present in even index positions in the given string?

string=input("Enter the string: ")
summ=0
for ip in range(0,len(string),2):
    if string[ip] in '02468':
        summ+=int(string[ip])
print(summ)

