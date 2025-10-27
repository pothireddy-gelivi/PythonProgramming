#Print How many lines have 101 characters in it?


FO=open("appending.txt","r")
lines=FO.readlines()
for i in range(len(lines)+1):
    res=lines[i-1]
    ch_count=0
    l=[]
    for ch in res:
        ch_count+=1

   
    c=0
    if ch_count==101:
        c+=1
        print(f"{i+1}th line has {ch_count} characters,and line is {lines[i]}| count is {c}")
        
    ch_count=0

    
