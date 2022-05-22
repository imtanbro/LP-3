
from Crypto.Cipher import AES

key = b'Sixteen byte key'
data = b'hello from other side'

e_cipher = AES.new(key, AES.MODE_EAX)
e_data = e_cipher.encrypt(data)

d_cipher = AES.new(key, AES.MODE_EAX, e_cipher.nonce)
d_data = d_cipher.decrypt(e_data)

print("Encryption was: ", e_data)
print("Original Message was: ", d_data)