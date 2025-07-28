# WAP to print how many special characters and alphabets and digits?

string=input("Enter the number: ")
alpha_count=0
digit_count=0
spl_count=0
for element in string:
    if element.isalpha():
        alpha_count+=1
    elif element.isdigit():
        digit_count+=1
    else:
        spl_count+=1
print(f"{alpha_count} is the alphabets count.")
print(f"{digit_count} is the digits count.")
print(f"{spl_count} is the special character count.")
