import math
from sympy import *

def findprime(n):
    """check the given number is prime"""
    """(num) ====> Boolean"""

    x = 3 # the small two primes 2, 3
    if n==1:
        raise ValueError("Input Check Number Should be Greater than 1!")
    elif (n <= x):
        return True
    
    # A composite number n has at least one pair of factors,
    # one is less than sqrt(n), the other one is larger.
    key = int(math.sqrt(n))
    for i in range(2, key+1):
        if(n % i == 0):
            return False
    return True

def ExpMath(n, digits):
    """Generate the target number as degit format"""
    """(num. num) ----> str"""
    #it is convenient to use str to change indices
    if n % pi == 0: # remove the decimal, should add another number for n.eval()
        return str(n.evalf(digits+1))[0:digits+1].replace(".", "")
    elif n % E == 0:
        return str(n.evalf(digits+1))[0:digits+1].replace(".", "")
    elif isinstance(n, float):
        k = str(n)[0:digits+1].replace(".", "")
        return k
    else:
        return str(n)[0:digits]


def SlidWind(num, l):
    """find out the first prime number"""

    #len is the length of searching range:
    len = l
    #left cut bound
    left = 0

    """"
    if the initial length of target number is prime, it won't go in the following while loop,
    so I define the initial result(potential prime number) here:
    """
    if isinstance(num, float):
        result = str(num)[0:l+1].replace(".", "")
    else:
        result = str(num)[0:l]
    
    #Searching the prime, untill the target prime is found, change the str of number to integer format
    while not findprime(int(ExpMath(num, len)[left:left+l])):
        len += 1
        left += 1

    #define the prime
    result = int(ExpMath(num, len)[left:left+l])
    print(f"the first 10-digit prime in the decimal expansion of 17π is: {result}")
    return result

if __name__ == '__main__':
    num = 17 * pi #target number
    digit = 10 #required digits
    SlidWind(num, digit)

    




