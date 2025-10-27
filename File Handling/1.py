#Print How many lines of data present in a given file?

FO=open("appending.txt","r")
lines=FO.readlines()
print(len(lines))