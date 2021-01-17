# Encrypting/Decrypting files using RSA algorithm
# Author : Ayush Gupta
# Date created : 15-01-2021

from math import floor, log
from os import path, listdir
from sys import exit
from textwrap import dedent
from time import time

import rsa

__version__ = "1.2.0"

def read_key_file(filename):
    """function that reads the public/private key file and returns the keysize, modulus and key"""
    fo = open(filename, "r")
    content = fo.read()
    fo.close()
    keysize, n, EorD = content.split(",")
    return (int(keysize), int(n), int(EorD))

def encrypt_to_file(text_file, cipher_file, key_file, blocksize=None):
    """function that encrypts text-file to cipher-file"""
    keysize, n, e = read_key_file(key_file)
    if blocksize==None:
        blocksize = floor(log(2**keysize, len(rsa.SYMBOLS)))
    if not floor(log(2**keysize, len(rsa.SYMBOLS))) >= blocksize:
        exit("ERROR: input the correct the key file for the specified block size") 
        
    fo = open(text_file, "r")
    text = fo.read()
    fo.close()
    
    cipher_block = rsa.encrypt_message(text, (n, e), blocksize)  
    
    for i in range(len(cipher_block)):
        cipher_block[i] = str(cipher_block[i])
    cipher = ",".join(cipher_block)
    
    cipher = "%s_%s_%s"%(len(text), blocksize, cipher)
    fo = open(cipher_file, "w")
    fo.write(cipher)
    fo.close()
    
    return cipher

def decrypt_to_file(cipher_file, text_file, key_file):
    """function that decrypts cipher-file to text-file"""
    keysize, n, d = read_key_file(key_file)
    
    fo = open(cipher_file, "r")
    content = fo.read()
    fo.close()
    
    text_len, blocksize, cipher = content.split("_")
    text_len = int(text_len)
    blocksize = int(blocksize)
    
    if not floor(log(2**keysize, len(rsa.SYMBOLS))) >= blocksize:
        exit("ERROR: input the correct the key file for the specified block size")
        
    cipher_blocks =[]
    for block in cipher.split(","):
        cipher_blocks.append(int(block))
        
    text = rsa.decrypt_message(cipher_blocks, text_len, (n, d), blocksize)
    
    fo = open(text_file, "w")
    fo.write(text)
    fo.close()    
    
    return text

onlyfiles = [f for f in listdir() if path.isfile(path.join(f))]

def check_file_exists(filename):
    """function that checks whether the file exists or in the table. If the condition is true, it returns
    the corresponding file."""
    if not path.exists(filename):
        if filename.isdigit():
            return onlyfiles[int(filename)]
        else:
            exit("ERROR: File does not exist.")
    return filename

def main():
    
    description = """
    RSA ENCRYPTION ALGORITHM [Version %s]
    source code -> https://github.com/GuptaAyush19/RSA-Cipher
    Copyright (c) 2021 Ayush Gupta\n
    Encrypt/Decrypt files using the corresponding public/private key.
    NOTE: public key is used for encryption and private key for decryption.
    """%(__version__)
    
    print(dedent(description))
    
    # check whether the user wants to generate a key pair
    print("Generate a key pair by entering 'True'. If key exists then enter 'False' ...")
    keypair_bool = input(">>> ").lower()
    if keypair_bool.startswith("t"):
        rsa.generate_key.main()
        input("Now as the keys are generated, rerun the program to encrypt/decrypt.")
        exit()
    elif keypair_bool.startswith("f"):
        pass
    else:
        exit("ERROR: Not a valid input.")
        
    # create table for files in current directory
    print("\nFiles in current directory for reference ->\n")
    for i in range(len(onlyfiles)):
        print("\t%s : %s"%(i, onlyfiles[i]))
    print("\nCorresponding numbers can be used to refer to the existing file.\n")
        
    mode = input("Do you want to (e)ncrypt or (d)ecrypt?> ").lower()
    # public key and private key input
    if mode.startswith("e"): # encrypt
        mode="encrypt"
        print("Mode selected: ENCRYPT")
        print("Input the path/number of the public key ...")
        publickey_file=input(">>> ")
        publickey_file = check_file_exists(publickey_file)
    elif mode.startswith("d"): # decrypt
        mode="decrypt"
        print("Mode selected: DECRYPT")
        print("Input the path/number to the private key ...")
        privatekey_file=input(">>> ")
        privatekey_file = check_file_exists(privatekey_file)
    else:
        exit("ERROR: Not a valid input.")
        
    # encrypt or decrypt text file
    if mode=="encrypt":
        print("Input the path/number of the plain-text file ...")
        text_file = input(">>> ")
        text_file = check_file_exists(text_file)
        print("Input the desired path of the cipher file ...")
        cipher_file = input(">>> ")
        if path.exists(cipher_file):
            exit("WARNING: The cipher-file already exist.")
        print("\nEncrypting the file (generating a default blocksize)....")
        startime = time()
        encrypt_to_file(text_file, cipher_file, publickey_file, blocksize=None)
        print("The plain-text has been encrypted to <%s>"%(cipher_file))
        print("Time taken to encrypt the file : %s seconds"%(round(time()-startime, 4)))
    else:
        print("Input the path/number of the cipher file ...")
        cipher_file = input(">>> ")
        cipher_file = check_file_exists(cipher_file)
        print("Input the desired path for the plain-text file ...")
        text_file = input(">>> ")
        if path.exists(text_file):
            exit("WARNING: The text-file already exists.")
        print("\nDecrypting the file ...")
        startime = time()
        decrypt_to_file(cipher_file, text_file, privatekey_file)
        print("The cipher-text has been decrypted to <%s>"%(text_file))
        print("Time taken to encrypt the file : %s seconds"%(round(time()-startime, 4)))
        
if __name__ == "__main__":
    main()
    input("Press any key to continue ...")
