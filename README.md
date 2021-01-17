# RSA-Cipher
Encrypt/Decrypt files using RSA algorithm.

## Description
RSA (Rivest–Shamir–Adleman) is an algorithm used by modern computers to encrypt and decrypt messages. It is an asymmetric cryptographic algorithm. Asymmetric means that there are two different keys. This is also called public key cryptography, because one of the keys can be given to anyone.\
Imagine that someone on the other side of the world wants to communicate
with you. You both know that spy agencies are monitoring all emails, letters,
texts, and phone calls. To send encrypted messages to that person, you both
must agree on a secret key to use. But if one of you emails the secret key to
the other, the spy agency will intercept this key and then decrypt any future
messages encrypted using that key. Secretly meeting in person to exchange
the key is impossible. You can try encrypting the key, but this requires sending that secret key for that message to the other person, which will also be
intercepted.\
Public key cryptography solves this encryption problem by using two keys,
one for encryption and one for decryption, and is an example of an asymmetric cipher. Ciphers that use the same key for encryption and decryption
are symmetric ciphers.
It’s important to know that a message encrypted using the encryption key
(public key) can only be decrypted using the decryption key (private key). So even if
someone obtains the encryption key, they won’t be able to read the original
message because the encryption key can’t decrypt the message.\
The encryption key is called the public key because it can be shared with
the entire world. In contrast, the private key, or the decryption key, must be
kept secret.

## Installation
Download *python3* from [here](https://www.python.org/downloads/). Don't forget to add Python to your PATH variable.\
Then download the *RSA-Cipher-main.zip* from github and extract it to a directory of your convenience.

## Ways to execute the program
There are two ways through which one can run the program,
  1. Open Command Prompt and type the following arguement to run the program.
  2. Just click *main.py* present in the parent directory and python console window will open.

To run the program in Command Prompt type,
```cmd
$ python main.py
```
Upon pressing enter, the following will be displayed -
```
RSA ENCRYPTION ALGORITHM [Version 1.1.2]
source code -> https://github.com/GuptaAyush19/RSA-Cipher
Copyright (c) 2021 Ayush Gupta

Encrypt/Decrypt files using the corresponding public/private key.
NOTE: public key is used for encryption and private key for decryption.
Generate a key pair by entering 'True'. If key exists then enter 'False' ...
>>> _
```
NOTE: The above display will be same if one uses python console.\
The rest of the instructions is fairly easy. Just follow the inputs as they are displayed.

## Public and Private Key generation
Let's see an example to see how we can generate public and private key for our encryption program.
```
Generate a key pair by entering 'True'. If key exists then enter 'False' ...
>>> True
Enter the file name (with no extensions)> x
Enter the key size (bit size, eg: 1024)> 1024
The public key is a 617 and 309 digit number
The private key is a 617 and 616 digit number
Key files made!
Now as the keys are generated, rerun the program to encrypt/decrypt
```
It is recommended to use 1024 bit-size key for RSA encryption.\
In the above example public key is saved as *x_publickey.txt* and private key as *x_privatekey.txt*. If you entered the name as 'Elon', the keys will be saved as *Elon_publicley.txt* and *Elon_privatekey.txt*. Now we can share the public key text file to anyone, they in turn can encrypt their messages using the public key and the message to you. You can then decrypt the message using the private key.

## Encrypting or Decrypting text files
Encryption -
```
Generate a key pair by entering 'True'. If key exists then enter 'False' ...
>>> False

Files in current directory for reference ->

        0 : LICENSE.txt
        1 : main.py
        2 : plain-text.txt
        3 : README.md
        4 : x_publickey.txt

Corresponding numbers can be used to refer to the existing file.

Do you want to (e)ncrypt or (d)ecrypt?> encrypt
Mode selected: ENCRYPT
Input the path/number of the public key ...
>>> 4
Input the path/number of the plain-text file ...
>>> 2
Input the desired path of the cipher file ...
>>> cipher.txt

Encrypting the file (generating a default blocksize)....
The plain-text has been encrypted to <cipher.txt>
Time taken to encrypt the file : 0.102 seconds
Press any key to continue ...
```

Decryption -
```
Generate a key pair by entering 'True'. If key exists then enter 'False' ...
>>> False

Files in current directory for reference ->

        0 : cipher.txt
        1 : LICENSE.txt
        2 : main.py
        3 : README.md
        4 : x_privatekey.txt
        5 : x_publickey.txt

Corresponding numbers can be used to refer to the existing file.

Do you want to (e)ncrypt or (d)ecrypt?> decrypt
Mode selected: DECRYPT
Input the path/number to the private key ...
>>> 4
Input the path/number of the cipher file ...
>>> 0
Input the desired path for the plain-text file ...
>>> plain-text.txt

Decrypting the file ...
The cipher-text has been decrypted to <plain-text.txt>
Time taken to encrypt the file : 0.08 seconds
Press any key to continue ...
```

Rather than using numbers for file, one can either use the path to the file or the file itself if it is in the current directory.
One such example -
```
Input the path/number of the cipher file ...
>>> cipher.txt
```

In this input, `Input the desired path for the plain-text file ...` the program generates a new file with the name given by the user. It is similiar for both encrypt and decrypt mode.

## Modules
You do not have to download any modules prior to running this program as they used are already included in the source code.
```tree
├── RSA-Cipher-main                  
│   ├── prime 
|   |   └── __init__.py
│   └── rsa 
|       ├── __init__.py
|       └── generate_key.py
└──
```

## Credits
The [Description](https://github.com/GuptaAyush19/RSA-Cipher#description) has been derived from *CRACKING CODES WITH PYTHON* by Al Sweigart and this book has been my inspiration to write this program.\
Al Sweigart is a software developer and tech book author living in San
Francisco. Python is his favorite programming language, and he is the
developer of several open source modules for it. His other books are
freely available under a Creative Commons license on his website https://
inventwithpython.com. His cat weighs 12 pounds.

## License
MIT License : see the [`License.txt`](https://github.com/GuptaAyush19/RSA-Cipher/blob/main/LICENSE.txt) file
