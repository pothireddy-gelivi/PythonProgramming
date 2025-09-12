# n=int(input("Enter the number: "))
# s=0
# while n>0:
#     ld=n%10
#     s+=ld
#     n//=10

# WAP to print sum of individual digits of given number by using recursion?

def sumd(n):
    if n==0:
        return 0
    return n%10 + sumd(n//10 )
num=int(input("Enter the number: "))
print(sumd(num))