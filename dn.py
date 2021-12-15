#Final code
from cryptography.fernet import Fernet

# key generation
key = Fernet.generate_key()

# string the key in a file - "C:\Users\meena\PycharmProjects\Practice\venv\Scripts\filekey.key"
with open(r'filekey.key', 'wb') as filekey:
    filekey.write(key)

# opening the key
with open(r'C:\Users\meena\PycharmProjects\Practice\venv\Scripts\filekey.key', 'rb') as filekey:
    key = filekey.read()
print(key)

# using the generated key
f = Fernet(key)

with open(r'C:\Users\meena\Downloads\adi4LightHalfFullTitles.csv', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open (r'D:\Project Exhibhition\Encrypted File\enc_file.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

#decryption
f = Fernet(key)

with open(r'D:\Project Exhibhition\Encrypted File\enc_file.csv', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open(r'D:\Project Exhibhition\Decrypted File\dec_file.csv', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)


