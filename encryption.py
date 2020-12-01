from cryptography.fernet import Fernet 
from os import path
import settings, json

'''Run this python script only once to create the files, 
remove this script from the folder after executing'''


credential={
    'key' : Fernet.generate_key().decode("utf-8"),
    'mvp' : <-- YOUR PASSWORD -->
}

#key is generated 
key = Fernet.generate_key()

# value of key is assigned to a variable
cipher = Fernet(key)

#key is stored in a file for further use
if (path.exists(settings.key_file)):
    print("exists")
else:
    with open(settings.key_file,'wb') as f:
        f.write(key)

#encoding the credential file
cred_byte = json.dumps(credential).encode('utf-8')

#encrypting the file with the cipher key
encode = cipher.encrypt(cred_byte)

#writing the encoded text into json file
if (path.exists(settings.creds_file)):
    pass
else:
    with open(settings.creds_file,'wb') as file_enc:
        file_enc.write(encode)
