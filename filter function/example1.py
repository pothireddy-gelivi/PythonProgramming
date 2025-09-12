# Filter with normal function

def isEven(n):
    return n%2==0

print(list(filter(isEven,[12,23,34,45,567,67])))