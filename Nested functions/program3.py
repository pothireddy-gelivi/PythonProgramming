#Passing another function address as a value to the argument:

def outer(arg):
    print("First line of outer")
    print(arg)
    def inner():
        print("First line of inner")
        print(arg)
        arg()
        print("Last line of inner")
    print("Last line of outer")
    return inner
def hai():
    print("First line of hai function")
    print("Last line of hai function")

result=outer(hai)
print(result)
result()
