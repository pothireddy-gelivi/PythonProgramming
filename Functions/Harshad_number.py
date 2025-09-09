import use
def harshadNumber(ll,ul):
    for n in range(ll,ul+1):
        if use.isHarshad(n):
            print(n)
harshadNumber(use.ll,use.ul)