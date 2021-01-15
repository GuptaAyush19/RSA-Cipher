# Encrypting/Decrypting files using RSA algorithm
# Author : Ayush Gupta
# Date created : 15-01-2021

import rsa
import math
import sys
import os
import time

__version__ = "1.0.1"

def read_key_file(filename):
    """function that reads the public/private key file and returns the keysize, modulus and key
    """
    fo = open(filename, "r")
    content = fo.read()
    fo.close()
    keysize, n, EorD = content.split(",")
    return (int(keysize), int(n), int(EorD))

def encrypt_to_file(text_file, cipher_file, key_file, blocksize=None):
    """functions that encrypts text-file to cipher-file
    """
    keysize, n, e = read_key_file(key_file)
    if blocksize==None:
        blocksize = math.floor(math.log(2**keysize, len(rsa.SYMBOLS)))
    if not math.floor(math.log(2**keysize, len(rsa.SYMBOLS))) >= blocksize:
        sys.exit("ERROR: input the correct the key file for the specified block size") 
        
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
    """functions that decrypts cipher-file to text-file
    """
    keysize, n, d = read_key_file(key_file)
    
    fo = open(cipher_file, "r")
    content = fo.read()
    fo.close()
    
    text_len, blocksize, cipher = content.split("_")
    text_len = int(text_len)
    blocksize = int(blocksize)
    
    if not math.floor(math.log(2**keysize, len(rsa.SYMBOLS))) >= blocksize:
        sys.exit("ERROR: input the correct the key file for the specified block size")
        
    cipher_blocks =[]
    for block in cipher.split(","):
        cipher_blocks.append(int(block))
        
    text = rsa.decrypt_message(cipher_blocks, text_len, (n, d), blocksize)
    
    fo = open(text_file, "w")
    fo.write(text)
    fo.close()    
    
    return text

def main():
    # description
    print("RSA ENCRYPTION ALGORITHM [Version %s]"%(__version__))
    print("source code -> github.com/GuptaAyush19/ \n")
    print("Encrypt/Decrypt files using the corresponding public/private key.")
    print("NOTE: public key is used for encryption and private key for decryption.")
    # check whether the user wants to generate a key pair
    print("Generate a key pair by entering 'True'. If key exists then enter 'False' ...")
    keypair_bool = input(">>> ").lower()
    if keypair_bool.startswith("t"):
        rsa.generate_key.main()
        sys.exit("Now as the keys are generated, rerun the program to encrypt/decrypt")
        
    # create table for files in current directory
    print("\nFiles in current directory for reference ->\n")
    onlyfiles = [f for f in os.listdir() if os.path.isfile(os.path.join(f))]
    for i in range(len(onlyfiles)):
        print("\t%s : %s"%(i, onlyfiles[i]))
    print("\nCorresponding numbers can be used to refer to the existing file.\n")
        
    # input the mode either encrypt or decrypt
    mode = input("Do you want to (e)ncrypt or (d)ecrypt?> ").lower()
    if mode.startswith("e"): # encrypt
        mode="encrypt"
        print("Mode selected: ENCRYPT")
        print("Input the path/number of the public key ...")
        publickey_file=input(">>> ")
        if not os.path.exists(publickey_file):
            if publickey_file.isalnum():
                publickey_file = onlyfiles[int(publickey_file)]
            else:
                sys.exit("ERROR: File does not exists.")
    elif mode.startswith("d"): # decrypt
        mode="decrypt"
        print("Mode selected: DECRYPT")
        print("Input the path/number to the private key ...")
        privatekey_file=input(">>> ")
        if not os.path.exists(privatekey_file):
            if privatekey_file.isalnum():
                privatekey_file = onlyfiles[int(privatekey_file)]
            else:
                sys.exit("ERROR: File does not exists.")
    else:
        sys.exit("ERROR: Not a valid input.")
        
    if mode=="encrypt":
        print("Input the path/number of the plain-text file ...")
        text_file = input(">>> ")
        if not os.path.exists(text_file):
            if text_file.isalnum():
                text_file = onlyfiles[int(text_file)]
            else:
                sys.exit("ERROR: File does not exists.")
        print("Input the desired path of the cipher file ...")
        cipher_file = input(">>> ")
        if os.path.exists(cipher_file):
            sys.exit("WARNING: The cipher-file already exists.")
        print("\nEncrypting the file (generating a default blocksize)....")
        startime = time.time()
        encrypt_to_file(text_file, cipher_file, publickey_file, blocksize=None)
        print("The plain-text has been encrypted to <%s>"%(cipher_file))
        print("Time taken to encrypt the file : %s seconds"%(round(time.time()-startime, 4))
    else:
        print("Input the path/number of the cipher file ...")
        cipher_file = input(">>> ")
        if not os.path.exists(cipher_file):
            if cipher_file.isalnum():
                cipher_file = onlyfiles[int(cipher_file)]
            else:
                sys.exit("ERROR: File does not exists.")
        print("Input the desired path for the plain-text file ...")
        text_file = input(">>> ")
        if os.path.exists(text_file):
            sys.exit("WARNING: The text-file already exists.")
        print("\nDecrypting the file ...")
        startime = time.time()
        decrypt_to_file(cipher_file, text_file, privatekey_file)
        print("The cipher-text has been decrypted to <%s>"%(text_file))
        print("Time taken to encrypt the file : %s seconds"%(round(time.time()-startime, 4)))
        
if __name__ == "__main__":
    main()
    input("Press any key to continue ...")
