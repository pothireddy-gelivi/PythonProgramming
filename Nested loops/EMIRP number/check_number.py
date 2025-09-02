#WAP to check the number is EMIRP number or not?

# n=int(input("Enter the number: "))
# if n>1:
#     for i in range(2,n//2+1):
#         if n%i==0:
#             print("Not a EMIRP number.why Because it is not a prime number.")
#             break
#     else:
#         s=int(str(n)[::-1])
#         if s>1:
#             for j in range(2,s//2+1):
#                 if s%j==0:
#                     print("Not a EMIRP number.why Because it is not a Reverse prime number.")
#                     break
#             else:
#                 if n!=s:
#                     print("EMIRP number")
#                 else:
#                     print("Not EMIRP number.Why Because it is a palindrome number.")


n=int(input("Enter the number: "))
r=int(str(n)[::-1])
if n!=r:
    for i in range(2,n//2+1):
        if n%i==0:
            print("Not emirp")
            break
    else:
        for j in range(2,r//2+1):
            if r%j==0:
                print("Not a emirp")
                break
        else:
            print("Emirp")
else:
    print("Emirp")