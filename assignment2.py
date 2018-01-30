#!/usr/bin/env python3

"""
Username    : tmtiuca
Student #   : 20521385
"""
"""
Assignment 2 Python file
Copy-and-paste your extended_euclid and modexp functions
from assignment 1
"""
import random
import math
import sys

# part (i) for modular exponentiation -- fill in the code below
def modexp(x, y, N):
    """
    Input: Three positive integers x and y, and N.
    Output: The number x^y mod N
    """
    if (y == 0):
        return 1

    z = modexp(x, math.floor(y/2), N)

    if (y % 2 == 0):
        return (z*z) % N
    else:
        return (x * z*z) % N


# part (ii) for extended Euclid  -- fill in the code below
def extended_euclid(a, b):
    """
    Input: Two positive integers a >= b >= 0
    Output: Three integers x, y, and d returned as a tuple (x, y, d)
            such that d = gcd(a, b) and ax + by = d
    """
    if (b == 0):
        return 1, 0, a

    x, y, d = extended_euclid(b, a%b)

    return y, x - math.floor(a/b) * y, d

##################################

def primality(N):
    """
    Test if a number N is prime using Fermat's little Theorem with
    ten random values of a.  If a^(N-1) mod N = 1 for all values,
    then return true.  Otherwise return false.
    Hint:  you can generate a random integer between a and b using
    random.randint(a,b).
    """

    for i in range(10):
        a = random.randint(2, N-1)
        remainder = modexp(a, N-1, N)
        if (remainder != 1):
            return False
    return True


def prime_generator(N):
    """
    This function generates a prime number <= N
    """
    p = random.randint(N/10, N)

    for i in range(int(math.pow(math.log(N), 4))):
        p = random.randint(N/10, N)
        if primality(p):
            return p

    return -1

def main():
    """
    Test file for the two parts of the question
    """
    ## Excercise 1:  generating primes and RSA
    ##################

    e = 5
    p = q = 0
    are_relatively_prime = False

    while not are_relatively_prime:
        p = prime_generator(10000000)
        q = prime_generator(10000000)

        if p == -1 or q == -1:
            sys.exit()

        _, _, gcd = extended_euclid(e, (p-1) * (q-1))
        are_relatively_prime = gcd == 1


    private_key, _, _ = extended_euclid(e, (p-1) * (q-1))

    if private_key < 0:
        private_key = private_key + (p-1) * (q-1)

    x = 329415
    N = p * q

    encoded = modexp(x, e, N)
    decoded = modexp(encoded, private_key, N)

    print('p:           ', p)
    print('q:           ', q)
    print('private_key: ', private_key)
    print('message :    ', x)
    print('encoded :    ', encoded)
    print('decoded :    ', decoded)


if __name__ == '__main__':
    main()
