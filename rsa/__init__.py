# RSA algorithm module
# Author : Ayush Gupta
# Date created : 15-01-2021
import sys

try:
    import generate_key
except ModuleNotFoundError:
    import rsa.generate_key
    
SYMBOLS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ,!?.\n"

def return_block(text, blocksize):
    for charac in text:
        if charac not in SYMBOLS:
            sys.exit("ERROR: The symbol set does not have the character %s"%(charac))
    block_int=[]
    for i in range(0, len(text), blocksize):
        block=0
        for j in range(i, min(i+blocksize, len(text))):
            block += SYMBOLS.index(text[j])*(len(SYMBOLS)**(j%blocksize))
        block_int.append(block)
    return block_int

def return_text(block, text_len ,blocksize):
    text=[]
    for block_int in block:
        block_text=[]
        for i in range(text_len-1,-1,-1):
            if len(text)+1<text_len:
                char_index=block_int//(len(SYMBOLS)**i)
                block_int=block_int%(len(SYMBOLS)**i)
                block_text.insert(0, SYMBOLS[char_index])
        text.extend(block_text)
    return "".join(text)

def encrypt_message(message, key, blocksize):
    cipher_block=[]
    n, e = key
    for block in return_block(message, blocksize):
        cipher_block.append(pow(block, e, n)) 
    return cipher_block

def decrypt_message(cipher_block, text_len, key, blocksize):
    text_block=[]
    n, d = key
    for block in cipher_block:
        text_block.append(pow(block, d, n)) 
    return return_text(text_block, text_len, blocksize)

def read_key_file(filename):
    fo = open(filename, "r")
    content = fo.read()
    fo.close()
    keysize, n, EorD = content.split(",")
    return (int(keysize), int(n), int(EorD))

if __name__ == "__main__":
    pubkey,privkey=generate_key.get_key(1024)
    text="ayush"
    cipher=encrypt_message(text, pubkey, 169)
    print(cipher)
    print(decrypt_message(cipher, len(text), privkey, 169))
  