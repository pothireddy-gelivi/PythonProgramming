#WAP to check the given number is duck number or not ?


# Duck Number
# 	• A number that contains zero(s), but not at the beginning.
# 	• Example: 102, 304

n=int(input("Enter the nubmer: "))
while n>0:
    ld=n%10
    if ld==0:
        print("duck number")
        break
    n//=10
else:
    print("not a duck number")