# Nested function returning integer as output:

def outer(arg):
    print("first line of outer")
    print(arg)
    def inner():
        print("First line of inner")
        print(arg)
        print("last line of inner")
    inner()
    print("last line of outer")
    return 100
result=outer(23)
print(result)