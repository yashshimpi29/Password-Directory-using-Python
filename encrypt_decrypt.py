from cryptography.fernet import Fernet 
from os import path
import settings, json

'''
We make a credential file and store the original key and master password in a dictionary format.
1. original key will be used to encrypt and decrypt the raw password before they are stored.
2. master password is used to while beginning the program.

This credential file is then encrypted with the help of second key generated.
Before encrypting any password, with the help of second key we decrypt the credential file
and get the original key.
'''

def master_password(mvp_check):
    """ The function checks the input password with the
    already set password. If both are same, we proceed further. 
    :param mvp_check: input master password. 
    :return: 1 if password matches, else 0
    """
    if (path.exists(settings.key_file)):
        # get the key from the text file
        with open(settings.key_file, "rb")as file_dec:
            key = file_dec.read()
            # value of key is assigned to a variable
            cipher = Fernet(key)
    
    with open(settings.creds_file, "rb")as file_dec:
        cred_decrypt = file_dec.read()
        
    data = cipher.decrypt(cred_decrypt).decode('utf-8')
    #converting the string format to json
    cred_json = json.loads(data)
    mvp = cred_json['mvp']

    if(mvp_check == mvp):
        return 1
    return 0

def get_key():
    """ With the help of key from key.txt file, we decrypt the credential file.
    From that file we get the original key through which we will encrypt and decrypt the 
    password. 
    :return: ciphered key for encryption and decryption
    """
    if (path.exists(settings.key_file)):
        # get the key from the text file
        with open(settings.key_file, "rb")as file_dec:
            key = file_dec.read()
            # value of key is assigned to a variable
            cipher = Fernet(key)

    #reads the creds.txt file containing the original key
    with open(settings.creds_file, "rb")as file_dec:
        cred_decrypt = file_dec.read()

    #data from the dictionary is decrypted    
    data = cipher.decrypt(cred_decrypt).decode('utf-8')
    
    #converting the string format to json
    cred_json = json.loads(data)
    
    #getting the key
    mvp = cred_json['key']

    #value of key is assigned to a variable
    cipher_og = Fernet(mvp.encode("utf-8"))
    
    return cipher_og

def encrypt(pword):
    """ The function encrypts the input raw password and returns the 
    encrypted form 
    :param pword: raw password. 
    :return: encrypted form of password
    """
    # Gets the key used to decrypt the original key
    cipher = get_key()
    #encoding the password file
    pword_byte = json.dumps(pword).encode('utf-8')
    #encrypting the file with the original cipher key
    pword_encrypt = cipher.encrypt(pword_byte)
    return pword_encrypt

def decrypt(pword):
    """ The function decrypts the encrypted password and returns the 
    password in raw format 
    :param pword: encrypted form of password. 
    :return: raw password
    """
    cipher = get_key()
    #decoding the credential file
    pword_decrypt = cipher.decrypt(pword).decode('utf-8') 
    return pword_decrypt    