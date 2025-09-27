# Returning inner function address from outer function space to main space:

def outer(arg):
    print("First line of outer")
    print(arg)
    def inner():
        print("First line of inner")
        print(arg)
        print("Last line of inner")
    print("Last line of outer")
    return inner

result =outer(23)
print(result)
result()