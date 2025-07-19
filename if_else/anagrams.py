#WAP to print given strings are anagrams or not?

str1=input("Enter the string: ")
str2=input("Enter the string: ")
if sorted(str1)==sorted(str2):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")