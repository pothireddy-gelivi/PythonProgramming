import use
def armstrongNumber(ll,ul):
    for n in range(ll,ul+1):
        if use.isArmstrong(n):
            print(n)
armstrongNumber(use.ll,use.ul)