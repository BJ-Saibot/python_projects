# Caesar cipher
# Develop's day - 03.06.2020
# Developer - Sergei Reshetnikov


def caesar_encrypt(plaintext):
    ciphertext = ""

    for char in plaintext:
        if char in ["x", "y", "z", "X", "Y", "Z"]:
            ciphertext += chr(ord(char) - 23)
        else:
            ciphertext += chr(ord(char) + 3)
    return ciphertext


def caesar_decrypt(ciphertext):
    plaintext = ""

    for char in ciphertext:
        if char in ["a", "b", "c", "A", "B", "C"]:
            plaintext += chr(ord(char) + 23)
        else:
            plaintext += chr(ord(char) - 3)
    return plaintext


if __name__ == "__main__":
    text = input("Please input the text: ")
    print("Encrypt text: " + caesar_encrypt(text))
    print("Decrypt text: " + caesar_decrypt(caesar_encrypt(text)))
