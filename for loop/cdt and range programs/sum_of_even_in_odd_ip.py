#WAP to print summ even digits present in odd index positions in a given string?

string=input("Enter the string: ")
summ=0
for ip in range(1,len(string),2):
    if int(string[ip])%2==0:
        summ+=int(string[ip])
print(summ)
       