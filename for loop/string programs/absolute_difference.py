#WAP to print absolute difference of all even integers and odd integers present in given list?
#absolute difference =sum(even)-sum(odd) it gives only value between the numbers.
list=eval(input("Enter the list: "))
even_summ=0
odd_summ=0
for element in list:
    if element%2==0:
        even_summ+=element
    else:
        odd_summ+=element
print(abs(even_summ-odd_summ))