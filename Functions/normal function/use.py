ll=int(input("Enter the lower limit: "))
ul=int(input("Enter the upper limit: "))


# checking prime number

def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True

# reverse a number

def reverse(n):
    rev=0
    while n>0:
        ld=n%10
        n//=10
        rev=rev*10+ld
    return rev

# Checking even number

def isEven(n):
    if n%2==0:
        return True
    else:
        return False
    
# Checking odd number

def isOdd(n):
    if n%2==1:
        return True
    else:
        return False

# Checking Perfect number

def isPerfect(n):
    s=0
    for i in range(1,n//2+1):
        if n%i==0:
            s+=i
    if n==s:
        return True
    else:
        return False
    
# Checking Armstrong number

def isArmstrong(n):
    s=0
    dn=n
    l=len(str(n))
    while dn>0:
        ld=dn%10
        s=s+ld**l
        dn//=10
    if n==s:
        return True
    else:
        return False
    
# Checking Disarium Number
def isDisarium(n):
    s=0
    l=len(str(n))
    dn=n
    while dn>0:
        ld=dn%10
        s=s+ld**l
        dn//=10
        l-=1
    if n==s:
        return True
    else:
        return False

# Checking Duck Number
def isDuck(n):
    while n>0:
        ld=n%10
        n//=10
        if ld==0:
            return True
        
    else:
        return False
    
#  Checking Harshad Number 

def isHarshad(n):
    s=0
    dn=n
    while dn>0:
        ld=dn%10
        s+=ld
        dn//=10
    if n%s==0:
        return True
    else:
        return False