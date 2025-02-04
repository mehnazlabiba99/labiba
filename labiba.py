def encrypt(plaintext,key):
    plaintext = plaintext.upper()
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char == ' ':
            shifted_char = char
        else:
            shifted_char = chr((ord(char) - 65 + key) % 26)
            shifted_char = chr(ord(shifted_char) + 65)
        ciphertext = ciphertext + shifted_char
    return ciphertext
