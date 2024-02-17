def binary_to_hex(binary):
    # Pad binary string to ensure its length is a multiple of 6
    hex_code = ""
    
    # Convert each group of 6 binary digits to hexadecimal
    # for i in range(0, len(binary), 6):
    #     binary_group = binary[i:i+6]
    #     decimal_value = int(binary_group, 2)
    #     hex_digit = format(decimal_value, '02X')  # Convert decimal to hex, specify width of 2 and make uppercase
    #     hex_code += hex_digit
    
    # return hex_code

    # Convert each group of 6 binary digits to hexadecimal
    for i in range(0, len(binary), 6):
        binary_group = binary[i:i+6]
        decimal_value = int(binary_group, 2)
        hex_digit = hex(decimal_value).upper()
        print(hex_digit)  # Convert decimal to hex, remove '0x' prefix and make uppercase
        hex_code += hex_digit
    
    return hex_code

# Test the function
binary_input = "011110000011001111000011001000001101101001110000"
hex_output = binary_to_hex(binary_input)
print("Hexadecimal:", hex_output)

