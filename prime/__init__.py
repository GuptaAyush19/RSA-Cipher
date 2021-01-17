# prime number module
# Author : Ayush Gupta
# Date created : 15-01-2021

from random import randrange
from math import sqrt

def prime_seive(n):
    """Function that returns first n prime numbers.

    Args:
        n (int): Upperlimit of the search.

    Returns:
        list: First n prime numbers.
    """
    seive = [True]*n
    seive[0] = False
    seive[1] = False
    
    for i in range(2, int(sqrt(n)+1)):
        pointer = i*2
        while pointer<n:
            seive[pointer] = False
            pointer += i
            
    prime = []
    for i in range(len(seive)):
        if seive[i]:
            prime.append(i)
            
    return prime

def rabin_miller(n):
    """Rabin Miller algorithm, a probabilistic primality test. 

    Args:
        n (int)

    Returns:
        bool: True or False.
    """
    if n%2==0 or n<2:
        # this algorithm does not work on even integers
        return False
    
    if n==3:
        return True
    
    s = n-1
    t = 0
    while s%2 == 0:
        s = s//2
        t += 1
        
    for trial in range(5):
        a = randrange(2, n-1)
        v = pow(a, s, n)
        if v != 1: # This test does not apply if v is 1.
            i = 0
            while v != (n - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % n
    
    return True

_LOW_PRIME = prime_seive(100)

def is_prime(n):
    if n<2:
        return False
    
    for prime in _LOW_PRIME:
        if n%prime==0:
            return False
        
    return rabin_miller(n)

def generate_prime(keysize=1024):
    """Function to generate a random prime number.

    Args:
        keysize (int, optional): Defaults to 1024 bit.

    Returns:
        int: Prime number of keysize bit size.
    """
    while True:
        n = randrange(2**(keysize-1), 2**keysize)
        if is_prime(n):
            return n

    
if __name__ == "__main__":
    prime = generate_prime()
    print(prime, is_prime(prime), sep="\n")         
