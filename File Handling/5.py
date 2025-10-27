#Print words which have 7 characters init?


FO=open("appending.txt","r")
lines=FO.readlines()
res=lines[0]
count=0
s=" "
for i in res:
    if i!=" ":
        count+=1
        s+=i
    else:
        if count==7:
            print(s)
        count=0
        s=" "
       



