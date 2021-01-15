# RSA algorithm module
# Author : Ayush Gupta
# Date created : 15-01-2021

import os
import sys
prime = __file__.split("\\")
prime.remove("generate_key.py")
prime.remove("rsa")
sys.path.append("\\".join(prime))

from prime import generate_prime
from random import randrange

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def isint(n):
    if type(n)==int:
        return True
    return int(n)==n

def inverse_mod(a, m):
    if gcd(a,m)!=1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3!=0:
        q=u3//v3
        v1, v2, v3, u1, u2, u3 = (u1-q*v1), (u2-q*v2), (u3-q*v3), v1, v2, v3
    return u1%m

def get_key(keysize):
    p,q = 0,0 # prime numbers
    while p == q:
        p = generate_prime(keysize)
        q = generate_prime(keysize)
    n = p*q
    phi = (p-1)*(q-1)
    while True: # public key
        e = randrange(2**(keysize-1), 2**(keysize))
        if gcd(e,phi) == 1:
            break
    
    """
    k=1
    while True: # private key
        d = (1+k*phi)/e
        if isint(d):
            break
        k+=1
    """
    
    d = inverse_mod(e, phi)
    
    publickey = (n, e)
    privatekey = (n, d)
    
    return publickey, privatekey

def make_key_file(name, keysize):
    if os.path.exists("%s_publickey.txt"%(name)) or \
        os.path.exists("%s_private.txt"%(name)):
        sys.exit("WARNING: The file %s_publickey.txt or %s_privatekey.txt already exists! "%(name, name)+\
            "Use a different name or delete these file and rerun the program.")
    pubkey, privkey = get_key(keysize)
    # public key
    print("The public key is a %s and %s digit number"%(len(str(pubkey[0])), len(str(pubkey[1]))))
    fo=open("%s_publickey.txt"%(name), "w")
    fo.write("%s,%s,%s"%(keysize, pubkey[0], pubkey[1]))
    fo.close()
    # private key
    print("The private key is a %s and %s digit number"%(len(str(privkey[0])), len(str(privkey[1]))))
    fo=open("%s_privatekey.txt"%(name), "w")
    fo.write("%s,%s,%s"%(keysize, privkey[0], privkey[1]))
    fo.close()
    print("Key files made!")

def main():
    name = input("Enter the file name (with no extensions)> ")
    for i in name:
        if i == ".": sys.exit("ERROR: not a valid name for the file.")
    keysize = int(input("Enter the key size (bit size, eg: 1024)> "))
    make_key_file(name, keysize)
        
if __name__ == "__main__":
    main()
    