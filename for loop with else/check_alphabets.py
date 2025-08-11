#WAP input="aaaabbbbccccddddd"
#output='a4b4c4d5'

s=input("Enter the string:")
ns=''
c=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c+=1
    else: 
        ns+=(str(s[i-1]+str(c)))
        c=1
ns+=(str(s[-1]+str(c)))
print(ns)