import secrets

def generate_random_key():
    # Generate 8 bytes (64 bits) of random data
    random_data = secrets.token_bytes(8)
    
    # Convert the random data to a hexadecimal string
    random_hex = random_data.hex().upper()
    
    # Format the random hexadecimal string to match the desired pattern
    formatted_key = f"{random_hex[0:2]}{random_hex[6:8]}{random_hex[4:6]}{random_hex[2:4]}{random_hex[10:12]}{random_hex[14:16]}{random_hex[12:14]}{random_hex[8:10]}"
    
    return formatted_key

# Generate a random key
random_key = generate_random_key()
print("Random Key:", random_key)
