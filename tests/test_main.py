from sys import path
__file__ = __file__.split("\\")
del __file__[-1];del __file__[-1]
PATH="\\".join(__file__)
path.append(PATH)

import os
import unittest

import rsa
import prime
import main

class TestPrime(unittest.TestCase):
    def test_generate_prime(self):
        print("checking prime number module ...")
        prime_num = prime.generate_prime()
        self.assertTrue(prime.is_prime(prime_num))

class TestGenerateKey(unittest.TestCase):
    
    def setUp(self):
        self.text="Hello World"
    
    def test_get_key(self):
        print("checking get_key, encrypt_message and decrypt_message functions ...")
        pubkey,privkey=rsa.generate_key.get_key(1024)
        block_size = 169
        cipher=rsa.encrypt_message(self.text, pubkey, block_size)
        self.assertAlmostEqual(self.text, rsa.decrypt_message(cipher, len(self.text), privkey, block_size))
        
class TestMain(unittest.TestCase):
    def setUp(self):
        self.text = "Hello World"
        self.name = "x"
        self.plain_text_file = "plain-text.txt"
        self.cipher_file = "cipher.txt"
        self.blocksize = 168
        # we create an example text file for the test
        fo = open(self.plain_text_file, "w")
        fo.write(self.text)
        fo.close()
        
    def tearDown(self):
        os.remove(self.plain_text_file)
        os.remove(self.cipher_file)
        os.remove("%s_publickey.txt"%(self.name))
        os.remove("%s_privatekey.txt"%(self.name))
        
    def test_decrypt_to_file(self):
        print("checking the encrypt_to_file and decrypt_to_file functions ...")
        rsa.generate_key.make_key_file(self.name, 1024 ,display=False)
        main.encrypt_to_file(self.plain_text_file, self.cipher_file, "%s_publickey.txt"%(self.name), self.blocksize)
        os.remove(self.plain_text_file)
        main.decrypt_to_file(self.cipher_file, self.plain_text_file, "%s_privatekey.txt"%(self.name))
        fo = open(self.plain_text_file, "r")
        content = fo.read()
        fo.close()
        self.assertAlmostEqual(content, self.text)
        

if __name__ == "__main__":
    unittest.main()   