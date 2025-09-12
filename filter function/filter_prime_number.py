# WAP to filter the prime numbers in a given list

def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False

print(list(filter(isPrime,[3,59,26,345,3631,47,437,566])))
