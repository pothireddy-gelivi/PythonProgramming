#WAP to check given number is palindrome number or not if it is palindrome print yes or else no?

number=int(input("Enter the number: "))
dummy_number=number
reverse=0
while dummy_number>0:
    remainder=dummy_number%10
    dummy_number=dummy_number//10
    reverse=reverse*10+remainder
if number==reverse:
    print("yes")
else:
    print("no")



