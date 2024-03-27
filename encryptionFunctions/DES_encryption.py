from functions.utils import xor, bin2dec, dec2bin, binary_to_hex
from necessaryFiles.permutations import initial_perm, final_perm, exp_d, per
from necessaryFiles.sboxes import sbox

def encrypt(plaintext, rkb, rk):
    plaintext = (f'{int(plaintext, 16):0>64b}')
    plaintext = ''.join(plaintext[initial_perm[i] - 1] for i in range(64))
    leftPlaintext = plaintext[0:32]
    rightPlaintext = plaintext[32:64]
    
    output = ""  # Initialize output string
    
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

        output += f"Round {i + 1}: {rk[i]} \n"
        output += f"  Left: {hex(int(leftPlaintext, 2))[2:].upper()} Right: {hex(int(rightPlaintext, 2))[2:].upper()} \n"
    cipher_text = binary_to_hex(cipher_text)
    output += f"Cipher Text: {cipher_text} \n"
    
    return output, cipher_text