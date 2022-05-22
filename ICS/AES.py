# 16-bit plaintext and 16-bit key
plain_text = '1101011100101000'
key = '0100101011110101'

assert len(plain_text) == 16
assert len(key) == 16
def split_half(key: str) -> tuple:
    n = len(key)
    mid = n//2
    return key[:mid], key[mid:]

w0, w1 = split_half(key)
print(f'w0: {w0}')
print(f'w1: {w1}')

def xor(first, second):
    result = []
    for f, s in zip(first, second):
        result.append(int(f) ^ int(s))
    result = [str(x) for x in result]
    result = "".join(result)
    return result


S_BOX = {
    '0000': '1001',
    '0001': '0100',
    '0010': '1010',
    '0011': '1011',
    '0100': '1101',
    '0101': '0001',
    '0110': '1000',
    '0111': '0101',
    '1000': '0110',
    '1001': '0010',
    '1010': '0000',
    '1011': '0011',
    '1100': '1100',
    '1101': '1110',
    '1110': '1111',
    '1111': '0111',
}

S_BOX_INV = dict(zip(S_BOX.values(), S_BOX.keys()))
from pprint import pprint
pprint(S_BOX_INV)

# w2 = w0 XOR 10000000 XOR SubNib(RotNib(w1))
def rot_nib(key: str) -> str:
    first, second = split_half(key)
    return second + first

def sub_nib(key: str) -> str:
    if len(key) != 4:
        first, second = split_half(key)
        return sub_nib(first) + sub_nib(second)
    return S_BOX[key]

def inverse_sub_nib(key: str) -> str:
    if len(key) != 4:
        first, second = split_half(key)
        return inverse_sub_nib(first) + inverse_sub_nib(second)
    return S_BOX_INV[key]

def g_func(first, second, round_constant) -> str:
    return xor(xor(first, round_constant), sub_nib(rot_nib(second)))

round_one_constant = '10000000'
w2 = g_func(w0, w1, round_one_constant)
print(f'w2: {w2}')

w3 = xor(w2, w1)
print(f'w3: {w3}')

round_two_constant = '00110000'
w4 = g_func(w2, w3, round_two_constant)
print(f'w4: {w4}')

w5 = xor(w4, w3)
print(f'w4: {w5}')

key0 = w0 + w1
key1 = w2 + w3
key2 = w4 + w5
print(f'key0: {key0}')
print(f'key1: {key1}')
print(f'key2: {key2}')

# Add Round 0 Key
def add_round_key(text: str, key: str) -> str:
    return xor(text, key)
result = add_round_key(plain_text, key0)
print(result)

result = sub_nib(result)
print(result)

# shift row, swap 2nd and 4th nibble
def shift_row(text: str) -> str:
    first_half, second_half = split_half(text)
    (f0, f1), (f2, f3) = split_half(first_half), split_half(second_half)
    result = f0 + f3 + f2 + f1  # swapping second and fourth nibble [zero based indexing]
    return result

result = shift_row(result)
print(result)

# mix columns
Me = [
    [1, 4],
    [4, 1]
]

Mf = [
    [9, 2],
    [2, 9]
]
M4 = {
    '0x1': '4',
    '0x2': '8',
    '0x3': '0xc',
    '0x4': '3',
    '0x5': '7',
    '0x6': '0xb',
    '0x7': '0xf',
    '0x8': '6',
    '0x9': '0',
    '0xa': '0xe',
    '0xb': '0xa',
    '0xc': '5',
    '0xd': '1',
    '0xe': '0xd',
    '0xf': '9'
}
M2 = {
    '0x1': '2',
    '0x2': '4',
    '0x3': '6',
    '0x4': '8',
    '0x5': '0xa',
    '0x6': '0xc',
    '0x7': '0xe',
    '0x8': '3',
    '0x9': '1',
    '0xa': '7',
    '0xb': '5',
    '0xc': '0xb',
    '0xd': '9',
    '0xe': '0xf',
    '0xf': '0xd'
}
M9 = {
    '0x1': '9',
    '0x2': '1',
    '0x3': '8',
    '0x4': '2',
    '0x5': '0xb',
    '0x6': '3',
    '0x7': '0xa',
    '0x8': '4',
    '0x9': '0xd',
    '0xa': '5',
    '0xb': '0xc',
    '0xc': '6',
    '0xd': '0xf',
    '0xe': '7',
    '0xf': '0xe'
}
def matrix_multiplication1(Me, s):
    s00 = int(s[0][0], base=2) 
    s01 = int(s[0][1], base=2) 
    s10 = int(s[1][0], base=2) 
    s11 = int(s[1][1], base=2) 
    a00 =  (1*s00) ^ int((M4[hex(s10)]), base=16)
    a01 =  (1*s01) ^ int((M4[hex(s11)]), base=16)
    a10 = int(M4[hex(s00)], base=16) ^ (1 * s10)
    a11 = int(M4[hex(s01)], base=16) ^ (1 * s11)
    
    a00 = bin(a00)[2:].zfill(4)
    a01 = bin(a01)[2:].zfill(4)
    a10 = bin(a10)[2:].zfill(4)
    a11 = bin(a11)[2:].zfill(4)
    return [
        [a00, a01],
        [a10, a11]
    ]
def matrix_multiplication2(Mf, s):
    s00 = int(s[0][0], base=2) 
    s01 = int(s[0][1], base=2) 
    s10 = int(s[1][0], base=2) 
    s11 = int(s[1][1], base=2) 
    a00 =  int((M9[hex(s00)]), base=16) ^ int((M2[hex(s10)]), base=16)
    a01 =  int((M9[hex(s01)]), base=16) ^ int((M2[hex(s11)]), base=16)
    a10 =  int((M2[hex(s00)]), base=16) ^ int((M9[hex(s10)]), base=16)
    a11 =  int((M2[hex(s01)]), base=16) ^ int((M9[hex(s11)]), base=16)
    
    a00 = bin(a00)[2:].zfill(4)
    a01 = bin(a01)[2:].zfill(4)
    a10 = bin(a10)[2:].zfill(4)
    a11 = bin(a11)[2:].zfill(4)
    return [
        [a00, a01],
        [a10, a11]
    ]
def shift_column(text: str) -> str:
    first_half, second_half = split_half(text)
    (f0, f1), (f2, f3) = split_half(first_half), split_half(second_half)
    # column major form
    s = [
        [f0, f2],
        [f1, f3]
    ]
    result = matrix_multiplication1(Me, s)
    output = result[0][0] + result[1][0] + result[0][1] + result[1][1]  # column major
    return output
def inverse_shift_column(text: str) -> str:
    first_half, second_half = split_half(text)
    (f0, f1), (f2, f3) = split_half(first_half), split_half(second_half)
    # column major form
    s = [
        [f0, f2],
        [f1, f3]
    ]
    result = matrix_multiplication2(Mf, s)
    output = result[0][0] + result[1][0] + result[0][1] + result[1][1]  # column major
    return output
first_round_output = shift_column(result)
print(first_round_output)

# add round 1 key
result = add_round_key(first_round_output, key1)
print(result)

# Second round
# 1. Nibble substitution
result = sub_nib(result)
print(result)
1010001101000011
shift_result = shift_row(result)
print(shift_result)
1010001101000011
cipher_text = add_round_key(shift_result, key=key2)
print(cipher_text)

def generate_subkeys(key: str) -> str:
    round_one_constant = '10000000'
    round_two_constant = '00110000'

    w0, w1 = split_half(key)
    w2 = g_func(w0, w1, round_one_constant)
    w3 = xor(w2, w1)
    w4 = g_func(w2, w3, round_two_constant)
    w5 = xor(w4, w3)
    
    k0 = w0 + w1
    k1 = w2 + w3
    k2 = w4 + w5
    return k0, k1, k2
def encryption(plain_text: str, key: str) -> str:
    k0, k1, k2 = generate_subkeys(key)
    
    result = add_round_key(plain_text, key=k0)
    
    # round 1
    result = sub_nib(result)
    result = shift_row(result)
    first_round_output = shift_column(result)
    
    result = add_round_key(first_round_output, key=k1)
    
    # round 2 (final)
    result = sub_nib(result)
    result = shift_row(result)
    
    cipher_text = add_round_key(result, key=k2)
    
    return cipher_text
def decryption(cipher_text: str, key: str) -> str:
    k0, k1, k2 = generate_subkeys(key)
    
    result = add_round_key(cipher_text, key=k2)
    
    # inverse shift row
    result = shift_row(result)
    
    # inverse nibble substitution
    result = inverse_sub_nib(result)
    
    # add round key 1
    result = add_round_key(result, key=k1)
    
    # inverse mix columns
    result = inverse_shift_column(result)

    # inverse shift row
    result = shift_row(result)
    
    # inverse nibble substitution
    result = inverse_sub_nib(result)
    
    plain_text = add_round_key(result, key=k0)
    
    return plain_text    
# 16-bit plaintext and 16-bit key
plain_text = '1101011100101000'
key = '0100101011110101'
cipher_text = encryption(plain_text, key)
print(cipher_text)

decrypted_text = decryption(cipher_text, key)
print(decrypted_text)

assert decrypted_text == plain_text