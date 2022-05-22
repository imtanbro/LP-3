from Crypto.Cipher import DES

def pad(text):
    n = len(text) % 8
    print(len(text))
    print(n)
    print(text + (b' ' * (8 - n)))
    print()
    return text + (b' ' * (8-n))


key = b'hello123'
text1 = b'Python is the Best Language!'

des = DES.new(key, DES.MODE_ECB)

padded_text = pad(text1)
encrypted_text = des.encrypt(padded_text)

print()
print(encrypted_text)
print(des.decrypt(encrypted_text))

