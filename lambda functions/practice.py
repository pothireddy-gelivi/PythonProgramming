import functools


# Write a lambda function to add two numbers.
'''a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
add=lambda a,b:a+b
print(add(a,b))'''


# Write a lambda function to find the square of a number.
'''a=int(input("Enter the number: "))
square=lambda a:a**2
print(square(a))'''

# Create a lambda function to return the maximum of two numbers.
'''a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
maximum=lambda a,b:a if a>b else b
print(maximum(a,b))'''

# Write a lambda function to check if a number is even or odd.

'''a=int(input("Enter the number: "))
check=lambda a:"even" if a%2==0 else "odd"
print(check(a))'''

# Write a lambda function to reverse a string.
'''reverse=lambda s:s[::-1]
print(reverse('asdfghjk'))'''

# Use a lambda with map() to square all numbers in a list.

'''print(list(map(lambda n:n**2,[2,3,4,5,6,7,8,9] )))'''

# Use a lambda with filter() to get only even numbers from a list.

'''print(list(filter(lambda n:n%2==0,[12,23,423,4,34,23,4,334,36,345,223])))'''

# Use a lambda with reduce() to find the product of a list of numbers.


'''print(functools.reduce(lambda a,b:a*b,[2,3,4,5,6,7]))'''


# Write a lambda function to sort a list of tuples by the second element.

list=[(3,1),(2,5),(34)]
# Write a lambda function to find the length of each word in a list of words.

'''words = ["Reddy", "Python", "Lambda"]
lengths = list(map(lambda w: len(w), words))
print(lengths) '''

# Use a lambda to sort a list of dictionaries by the value of a key.

'''data=[
    {"name":"reddy","age":23},
    {"name":"kiran","age":22},
    {"name":"gowda","age":26} 
]
sorted_data=sorted(data,key=lambda d:d["age"])
print(sorted_data)'''

# Write a lambda function to check if a string is a palindrome.


'''check=lambda s: s==s[::-1]
print(check("madam"))'''