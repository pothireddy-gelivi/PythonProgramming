#WAP to check given number is disarium?

# 135=1**1+3**2+5**3 take index position of number in power

number=int(input("Enter the number: "))
dummy_number=number
s=0
length=len(str(number))
while dummy_number>0:
    remainder=dummy_number%10
    dummy_number//=10
    s+=remainder**length
    length-=1
if s==number:
    print("Disarium Number")
else:
    print("Not A Disarium Number")

