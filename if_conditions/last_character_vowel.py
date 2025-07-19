#WAP to print given string if it has vowel as their last character?

string=input("Enter the string: ")
if string[-1] in "aeiouAEIOU":
    print(string)