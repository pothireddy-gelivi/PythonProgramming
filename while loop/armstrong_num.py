#WAP to check given number is armstrong ?
'''
armstrong number are those numbers which are equal to the sum of the digits 
of the each number raised to the power of the number of digits in the number 
itself.There are 14 Armstrong numbers in the range of 1 - 5000.
1,2,3,4,5,6,7,8,9,153,370,371,407,1634
'''
# 153=1**3+5**3+3**3 take length of number in power

number=int(input("Enter the number: "))
dummy_number=number
s=0
length=len(str(number))
while dummy_number>0:
    remainder=dummy_number%10
    dummy_number//=10
    s+=remainder**length
   
if s==number:
    print("Armstrong Number")
else:
    print("Not A Armstrong Number")