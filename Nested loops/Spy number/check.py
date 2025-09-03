#WAP to check the given number is spy number or not?

# Spy Number
# 	• A number where the sum of its digits equals the product of its digits.
# 	• Example:
# 		○ 1124 → 1+1+2+4 = 8; 1×1×2×4 = 8


n=int(input("Enter the number: "))
s=0
p=1
while n>0:
    ld=n%10
    s+=ld
    p*=ld
    n//=10
if s==p:
    print("spy number")
else:
    print("not a spy number")