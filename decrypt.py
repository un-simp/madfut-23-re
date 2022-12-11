# import json
# import sys
# from base64 import b64decode, b64encode

# from Crypto.Cipher import AES

# from Crypto.Random import get_random_bytes

# key = b64decode("shBeeokeqh1k3Mz/2PbbuFC7NG3UZEN9dGOT9VzwG9k=")


# cipher = AES.new(key, AES.MODE_SIV)    # Without nonce, the encryption

#                                                     # becomes deterministic

# # ciphertext, tag = cipher.encrypt_and_digest(b"fuck")
# # print(ciphertext)
# # print(tag)



# ciphertext = b'a2c48563a71dff7780d5a13e48ea607950209f72f6d3cec64f3feb561814bfdd3f39a554f465db81be9c21b3c980c6ae2cde125b9e3dc46d511b45fea8755e7f5c10f40d620fa82f953d373f36f8668a35c6c994b7d56cab1efe4dd51f4720fea5e650ead1f16f287f9aa1249a96d193c312837050d3ae8d3def91454c97792ac316cc2fcced73777a6a79486a63bf859593ceb754d109bf8f40feb3cbe3370c7100b5e251a4408b4c3a38905123c0a30747970652e676f6f676c65617069732e636f6d2f676f6f676c652e63727970746f2e74696e6b2e4165735369764b6579100118b4c3a389052001'
# tag = b'12a901108a27e11'
# untag = cipher.decrypt_and_verify(ciphertext, tag)
# print("cipher ", ciphertext)
# print("tag", tag)
# print("decrpted ", untag)
# print("hex of tag is ", tag.hex())

import base64
from Crypto.Cipher import AES
def decrypt_keyset(key, encrypted_data, tag):
    decoded_data = base64.b64decode(encrypted_data)

    decoded_key = base64.b64decode(key)
    decode_tag = base64.b64decode(tag)


    cipher = AES.new(decoded_key, AES.MODE_SIV,)


    decrypted_data = cipher.decrypt_and_verify(decoded_data,tag)

    return decrypted_data


def decrypt_data(key, iv, encrypted_data):
    # Decode the encrypted data from base64
    decoded_data = base64.b64decode(encrypted_data)

    # Create a new AES cipher using the key and iv
    cipher = AES.new(key, AES.MODE_GCM, iv)

    # Decrypt the data
    decrypted_data = cipher.decrypt(decoded_data)

    # Return the decrypted data
    return decrypted_data


keyset_file_path = "/home/un/dev/madfut-23-re/an"

prefs_file_path = "/data/data/com.example.app/shared_prefs/com.example.app_preferences.xml"

keyset_key = b"shBeeokeqh1k3Mz/2PbbuFC7NG3UZEN9dGOT9VzwG9k="

with open(keyset_file_path, "rb") as f:
 

    tag = f.read()[-16:]
    f.seek(0)
    encrypted_keyset = f.read()[:-16]
    

decrypted_keyset = decrypt_keyset(keyset_key, encrypted_keyset,tag)

key = decrypted_keyset[:16]
iv = decrypted_keyset[16:32]

print(key)
print(iv)
print(decrypt_keyset)
# encrypted_data = ""


# decrypted_data = decrypt_data(key, iv, encrypted_data)

# # Print the decrypted data
# print(decrypted_data)
