import use

def oddNumbers(ll,ul):
    for i in range(ll,ul+1):
        if use.isOdd(i):
            print(i)


# ll=int(input("Enter the lower limit: "))
# ul=int(input("Enter the upper limit: "))
oddNumbers(use.ll,use.ul)