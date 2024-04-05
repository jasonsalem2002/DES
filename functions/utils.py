from necessaryFiles.permutations import keyp, shift_table, key_comp

def validate_hex(P):

    if not P or len(P) > 16:  # its not just a validate hex function but also to check that input is restricted to less or equal than 16
        return False

    for char in P:
        if char not in "0123456789abcdefABCDEF":
            return False
    return True

def binary_to_hex(s):
    padded_length = ((len(s) + 3) // 4) * 4 
    s = s.zfill(padded_length) 
    
    hex_code = ""
    for i in range(0, len(s), 4):
        chunk = s[i:i+4]  
        decimal_value = int(chunk, 2) 
        hex_digit = format(decimal_value, 'X') 
        hex_code += hex_digit
    
    return hex_code

def keyGeneration(key):
    binKey = (f'{int(key, 16):0>64b}')

    permutedKey = ''.join(binKey[keyp[i] - 1] for i in range(56))

    leftKey = permutedKey[0:28]
    rightKey = permutedKey[28:56]

    # Initialize rkb list to store round keys
    rkb = []

    for i in range(16):
        nth_shifts = shift_table[i]
        leftKey = leftKey[nth_shifts % len(leftKey):] + leftKey[:nth_shifts % len(leftKey)]
        rightKey = rightKey[nth_shifts % len(rightKey):] + rightKey[:nth_shifts % len(rightKey)]

        preKey = leftKey + rightKey
        keyR = ''.join(preKey[key_comp[j] - 1] for j in range(48))
        rkb.append(keyR)

    return rkb

def xor(a, b):
	ans = ""
	for i in range(len(a)):
		if a[i] == b[i]:
			ans = ans + "0"
		else:
			ans = ans + "1"
	return ans

def bin2dec(binary):
    decimal, i= 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal
  
def dec2bin(num):
    res = bin(num).replace("0b", "")
    if(len(res) % 4 != 0):
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res