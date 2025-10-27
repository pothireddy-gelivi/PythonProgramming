#Print how many characters of data present in a file?

FO=open("appending.txt","r")
lines=FO.readlines()
count=1
res=lines[0]
for i in res:
   count+=1

print(count)