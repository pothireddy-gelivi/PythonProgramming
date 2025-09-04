import use
def palindromeNumbers(ll,ul):
    for i in range(ll,ul+1):
        if i==use.reverse(i):
            print(i)

ll=int(input("Enter the lower limit: "))
ul=int(input("Enter the upper limit: "))
palindromeNumbers(ll,ul)