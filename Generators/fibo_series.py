# def fiboGen(fn,sn,n):
#     a=1
#     while a<=n:
#         a+=1
#         yield fn
#         fn,sn=sn,fn+sn

# fgo=fiboGen(0,1,10)
# for i in fgo:
#     print(i,end=" ")


# t=11,22,44,57,108,88
# l=[]
# for i in t:
#     if i%2==0:
#         if i >50:
#             l.append(i)
#     else:
#         l.append(i)
# print(l)

# l=[i for i in t if i%2==1 or i>50]
# print(l)

l=[[i]*3 for i in range(1,11)]

print(l)