from functions.utils import xor, bin2dec, dec2bin, binary_to_hex, keyGeneration
from necessaryFiles.permutations import initial_perm, final_perm, exp_d, per
from necessaryFiles.sboxes import sbox

def decrypt(cipher, key):
    binCipher = (f'{int(cipher, 16):0>64b}')
    rk = key[::-1]
        
    output = ""  # Initialize output string
    
    perm = ''.join(binCipher[initial_perm[i] - 1] for i in range(64))
    
    left = perm[0:32]
    right = perm[32:64]
        
    for i in range(16):
        right_expanded = ''.join(right[exp_d[i] - 1] for i in range(48))
        right_xor = xor(right_expanded, rk[i])
        
        sbox_str = ""
        for j in range(0, 48, 6):
            row = bin2dec(int(right_xor[j] + right_xor[j+5]))
            col = bin2dec(int(right_xor[j+1:j+5]))
            val = sbox[j//6][row][col]
            sbox_str += dec2bin(val)
        
        sbox_str = ''.join(sbox_str[per[i] - 1] for i in range(32))
        left_xor = xor(left, sbox_str)
        
        left = right
        right = left_xor
        
        output += f"Round {i + 1}: {binary_to_hex(left)} {binary_to_hex(right)} {binary_to_hex(rk[i])} \n"
    
    combined = right + left
    final = ''.join(combined[final_perm[i] - 1] for i in range(64))
    hex_code = binary_to_hex(final)
    
    output += f"Decrypted Text: {hex_code}"
    
    return output, hex_code

#testing C0B7A8D05F3A829C