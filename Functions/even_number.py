import use

def evenNumbers(ll,ul):
    for n in range(ll,ul+1):
        if use.isEven(n):
            print(n)

ll=int(input("Enter the lower limit: "))
ul=int(input("Enter the upper limit: "))
evenNumbers(ll,ul)