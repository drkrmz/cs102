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
            if ord(symbol)+ord(shift)-ord("A") <= ord("Z"):
                ciphertext = ciphertext + chr(ord(shift)+ord(symbol)-ord("A"))
            else:
                ciphertext = ciphertext + chr(ord(shift)+ord(symbol)-ord("A")-26)
        else:
            if ord(symbol)+ord(shift)-ord("a") <= ord("z"):
                ciphertext = ciphertext + chr(ord(shift)+ord(symbol)-ord("a"))
            else:
                ciphertext = ciphertext + chr(ord(shift)+ord(symbol)-ord("a")-26)
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
            if ord(symbol)-ord(shift)+ord("A") >= ord("A"):
                plaintext = plaintext + chr(ord(symbol)-ord(shift)+ord("A"))
            else:
                plaintext = plaintext + chr(ord(symbol)-ord(shift)+ord("A")+26)
        else:
            if ord(symbol)-ord(shift)+ord("a") >= ord("a"):
                plaintext = plaintext + chr(ord(symbol)-ord(shift)+ord("a"))
            else:
                plaintext = plaintext + chr(ord(symbol)-ord(shift)+ord("a")+26)
        i = i + 1
    return plaintext
