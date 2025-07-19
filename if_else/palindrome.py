#WAP to print given string us palindrome or not?

string=input("Enter the string: ")
if string==string[::-1]:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
