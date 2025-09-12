# input = [10,[12,13],[15,16,[17,8]],40]
# output= [10, 12, 13, 15, 16, 17, 8, 40]

def flatten(list):
    fl=[]
    for ele in list:
        if isinstance(ele,int):
            fl.append(ele)
        else:
            fl.extend(flatten(ele))
    return fl

list=eval(input("Enter the number: "))
print(flatten(list))

# print(list(map(lambda n:n%2==0,[11,22,30,13])))

# print(list(map(int,["12","45","90","88"])))

print(list(map(int,input() .split())))