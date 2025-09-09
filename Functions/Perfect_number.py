import use
def perfectNumber(ll,ul):
    for n in range(ll,ul+1):
        if use.isPerfect(n):
            print(n)
perfectNumber(use.ll,use.ul)
