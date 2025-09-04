import use
def primeNumbers(ll,ul):
    for i in range(ll,ul+1):
        if use.isPrime(i):
            print(i)

ll=int(input("Enter the lower limit: "))
ul=int(input("Enter the upper limit: "))
primeNumbers(ll,ul)