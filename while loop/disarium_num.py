#WAP to check given number is disarium?
'''A Disarium number is a number in which the sum of its digits powered with their respective positions is equal to the number itself.'''
# 135=1**1+3**2+5**3 take index position of number in power
# 89=8**1+9**2
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

