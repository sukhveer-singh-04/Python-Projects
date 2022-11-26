def encrypt(text, key):
    result = ""

    # making Key of same size
    size_st = len(text)
    size_key = len(key)
    if size_st > size_key:
        multi = size_st // size_key
        rem = size_st % size_key
        key = (key) * multi
        for i in range(rem):
            key += key[i]

    # To Encrpt
    for i in range(len(text)):
        char = text[i]
        key_char = key[i]
        result += chr((ord(char) + ord(key_char) - 129) % 26 + 65)
    return result


text = input("Enter the plain text :").upper()
KEY = input("Enter a Key to Encrypt(e.g. - cat,dog...,etc) :").upper()


print("Text : " + text)
print("Cipher: " + encrypt(text, KEY))
