#Print How many words of data present in a given file?

FO=open("appending.txt","r")
lines=FO.readlines()
print(lines)
count=1
res=lines[0]
for i in res:
    if i==" ":
        count+=1

print(count)