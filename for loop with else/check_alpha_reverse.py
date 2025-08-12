#WAP input='a4b4c4d5'
#output="aaaabbbbccccddddd"

string=input("Enter the string: ")
ns=''
for i in range(0,len(string),2):
    ns=ns+(string[i]*int(string[i+1]))

print(ns)