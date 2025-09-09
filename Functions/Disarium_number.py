import use 
def disariumNumber(ll,ul):
    for n in range(ll,ul+1):
        if use.isDisarium(n):
            print(n)
disariumNumber(use.ll,use.ul)