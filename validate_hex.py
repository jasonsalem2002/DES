def validate_hex(P):
    if not P:
        return False

    for char in P:
        if char not in "0123456789abcdefABCDEF":
            return False
    return True