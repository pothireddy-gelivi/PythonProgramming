import use
def duckNumber(ll,ul):
    for n in range(ll,ul+1):
        if use.isDuck(n):
            print(n)
duckNumber(use.ll,use.ul)