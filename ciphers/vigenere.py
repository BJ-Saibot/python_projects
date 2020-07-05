# Vigenere cipher
# Develop's day - 04.06.2020
# Developer - Sergei Reshetnikov


def vigenere_encrypt(plaintext, keyword):
    while len(keyword) < len(plaintext):
        num = len(plaintext) - len(keyword)
        keyword += keyword[:num]

    ciphertext = ""
    couples_list = [list(x) for x in zip(plaintext, keyword)]

    for couple in couples_list:
        if couple[1].isupper():
            couple[1] = ord(couple[1]) - 65
            if ord(couple[0]) + couple[1] > 90:
                ciphertext += chr(ord("A") + (ord(couple[0]) + couple[1] - 91))
            else:
                ciphertext += chr(ord(couple[0]) + couple[1])
        else:
            couple[1] = ord(couple[1]) - 97
            if ord(couple[0]) + couple[1] > 122:
                ciphertext += chr(ord("a") + (ord(couple[0]) + couple[1] - 123))
            else:
                ciphertext += chr(ord(couple[0]) + couple[1])
    return ciphertext


def vigenere_decrypt(ciphertext, keyword):
    while len(keyword) < len(ciphertext):
        num = len(ciphertext) - len(keyword)
        keyword += keyword[:num]

    plaintext = ""
    couples_list = [list(x) for x in zip(ciphertext, keyword)]

    for couple in couples_list:
        if couple[1].isupper():
            couple[1] = ord(couple[1]) - 65
            if ord(couple[0]) + couple[1] > 90:
                plaintext += chr(ord("A") + (ord(couple[0]) + couple[1] - 91))
            else:
                plaintext += chr(ord(couple[0]) + couple[1])
        else:
            couple[1] = ord(couple[1]) - 97
            if ord(couple[0]) + couple[1] > 122:
                plaintext += chr(ord("a") + (ord(couple[0]) + couple[1] - 123))
            else:
                plaintext += chr(ord(couple[0]) + couple[1])
    return plaintext


print(vigenere_encrypt("ATTackATDawn", "lemon"))
