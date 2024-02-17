keyp = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,10, 2, 59, 51, 43, 35, 27,19, 11, 3, 60, 52, 44, 36,63, 55, 47, 39, 31, 23, 15,7, 62, 54, 46, 38, 30, 22,14, 6, 61, 53, 45, 37, 29,21, 13, 5, 28, 20, 12, 4]
shift_table = [1, 1, 2, 2,2, 2, 2, 2,1, 2, 2, 2,2, 2, 2, 1]
key_comp = [14, 17, 11, 24, 1, 5,3, 28, 15, 6, 21, 10,23, 19, 12, 4, 26, 8,16, 7, 27, 20, 13, 2,41, 52, 31, 37, 47, 55,30, 40, 51, 45, 33, 48,44, 49, 39, 56, 34, 53,46, 42, 50, 36, 29, 32]

def binary_to_hex(binary):
    # Pad binary string to ensure its length is a multiple of 6
    hex_code = ""
    
    for i in range(0, len(binary), 6):
        binary_group = binary[i:i+6]
        decimal_value = int(binary_group, 2)
        hex_digit = format(decimal_value, '02X')  # Convert decimal to hex, specify width of 2 and make uppercase
        hex_code += hex_digit
    
    return hex_code


def keyGeneration(key):
    binKey= (f'{int(key, 16):0>64b}')

    permutedKey = ''.join(binKey[keyp[i] - 1] for i in range(56))

    leftKey = permutedKey[0:28]
    rightKey = permutedKey[28:56]

    rk = []

    nth_shifts = shift_table[1]
    leftKey = leftKey[nth_shifts % len(leftKey):] + leftKey[:nth_shifts % len(leftKey)]
    rightKey = rightKey[nth_shifts % len(rightKey):] + rightKey[:nth_shifts % len(rightKey)]

    preKey = leftKey + rightKey
    print(preKey)
    keyR = ''.join(preKey[key_comp[j] - 1] for j in range(48))
    print(keyR)
    rk.append(format(int(keyR, 2), '012X'))
    return rk

def cipher():
    
    return None
plaintext = input("Enter the plaintext:02468ACEECA86420 ").upper()
key = "0F1571C947D9E859"
# input("Please enter a key:0F1571C947D9E859 ").upper()

print("First Round key: ",keyGeneration(key))
print("L1: ")
print("R1: ")