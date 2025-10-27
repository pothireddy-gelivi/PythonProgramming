#Print Words which are Starting with h?

with open("content.txt","w") as f:
    f.write("Hello how are you doing today? Hope you have a happy holiday ahead!")

with open("content.txt","r") as r:
    content=r.readline()

words=content.split()
for word in words:
    if word.lower().startswith("h"):
        # cleaned=word.strip(",./?!")
        print(word)

    