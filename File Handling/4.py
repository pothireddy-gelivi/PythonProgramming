#Print how many words have 5 characters?

FO=open("appending.txt","r")
lines=FO.readlines()
res=lines[0]
count_of_five_ch=0
count=0
for i in res:
    if i!=" ":
        count+=1
        
    else:
        if count==5:
            count_of_five_ch +=1
        count=0
       
print(count_of_five_ch)

