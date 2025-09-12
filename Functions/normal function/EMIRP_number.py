import use

def emirpNumber(ll,ul):
    for i in range(ll,ul+1):
        rev=use.reverse(i)
        if use.isPrime(i) and use.isPrime(rev) and i != rev:
            print(i)

ll=int(input("Enter the lower limit: "))
ul=int(input("Enter the upper limit: "))
emirpNumber(ll,ul)