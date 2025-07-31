#WAP to print index positions of all the vowels present in the string? 

string=input("Enter the string: ")
for ip in range(len(string)):
    if string[ip] in 'aeiouAEIOU':
        print(ip)