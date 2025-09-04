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