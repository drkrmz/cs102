def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    i = 0
    while i < len(plaintext):
        symbol = plaintext[i]
        shift = keyword[i % len(keyword)]
        if "A" <= shift <= "Z":
            code_symbol = ord(symbol) + ord(shift) - ord("A")
            if ord(symbol)+ord(shift)-ord("A") <= ord("Z"):
                ciphertext = ciphertext + chr(code_symbol)
            else:
                ciphertext = ciphertext + chr(code_symbol - 26)
        else:
            code_symbol = ord(symbol) + ord(shift) - ord("a")
            if code_symbol <= ord("z"):
                ciphertext = ciphertext + chr(code_symbol)
            else:
                ciphertext = ciphertext + chr(code_symbol-26)
        i = i + 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    i = 0
    while i < len(ciphertext):
        symbol = ciphertext[i]
        shift = keyword[i % len(keyword)]
        if "A" <= symbol <= "Z":
            code_symbol = ord(symbol) - ord(shift) + ord("A")
            if code_symbol >= ord("A"):
                plaintext = plaintext + chr(code_symbol)
            else:
                plaintext = plaintext + chr(code_symbol + 26)
        else:
            code_symbol = ord(symbol) - ord(shift) + ord("a")
            if code_symbol >= ord("a"):
                plaintext = plaintext + chr(code_symbol)
            else:
                plaintext = plaintext + chr(code_symbol+26)
        i = i + 1
    return plaintext
