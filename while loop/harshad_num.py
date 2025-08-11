#WAP to check the given number is harshad number or not?
'''harshad number:an integer which is divisible by its sum of digits is called harshad number'''
#12=1+2 --->12%3==0


number=int(input("Enter the number: "))
dummy_number=number
s=0
while dummy_number>0:
    remainder=dummy_number%10
    dummy_number=dummy_number//10
    s+=remainder
if number%s==0:
    print("it is a harshad number.")
else:
    print("it is not a harshad number")
