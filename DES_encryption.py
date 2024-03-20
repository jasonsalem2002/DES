from functions.utils import xor, bin2dec, dec2bin, binary_to_hex, keyGeneration
from necessaryFiles.permutations import initial_perm, final_perm, exp_d, per
from necessaryFiles.sboxes import sbox

def encrypt(plaintext, rkb, rk):
    plaintext = (f'{int(plaintext, 16):0>64b}')
    plaintext = ''.join(plaintext[initial_perm[i] - 1] for i in range(64))
    leftPlaintext = plaintext[0:32]
    rightPlaintext = plaintext[32:64]

    for i in range(16):
        rightPlaintextExpanded = ''.join(rightPlaintext[exp_d[i] - 1] for i in range(48))
        xor_x = xor(rightPlaintextExpanded, rkb[i])  # Use round key for current round
        sbox_str = ""
        for j in range(8):
            row = bin2dec(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
            col = bin2dec(
                int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4]))
            val = sbox[j][row][col]
            sbox_str = sbox_str + dec2bin(val)

        sbox_str = ''.join(sbox_str[per[i] - 1] for i in range(32))
        result = xor(leftPlaintext, sbox_str)
        leftPlaintext = result

        if i != 15:
            leftPlaintext, rightPlaintext = rightPlaintext, leftPlaintext
        combine = leftPlaintext + rightPlaintext
        cipher_text = ''.join(combine[final_perm[i] - 1] for i in range(64))

        print("Round ", i + 1, hex(int(leftPlaintext, 2))[2:].upper(), hex(int(rightPlaintext, 2))[2:].upper(), rk[i])  # Print round keys for each round

    print("Cipher Text:", binary_to_hex(cipher_text))
    return cipher_text


plaintext = "123456ABCD132536"
key = "AABB09182736CCDD"

rkb = keyGeneration(key)
rk = [] 
for keyR in rkb:
    rk.append(format(int(keyR, 2), '012X'))
ciphertext= encrypt(plaintext, rkb, rk)