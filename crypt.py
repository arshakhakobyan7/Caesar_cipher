import string

def caesar(open_text, keyy):
    encrypt_text = []
    key_max_length = 26

    for i in open_text:
        t = i.islower()
        for j in range(key_max_length):
            if string.ascii_lowercase[j] == i.lower():
                if j + keyy < key_max_length:
                    letter = string.ascii_lowercase[j+keyy]
                else:
                    letter = string.ascii_lowercase[j+keyy-key_max_length]
                break
        if t:
            encrypt_text.append(letter)
        else:
            encrypt_text.append(letter.upper())

    return ''.join(encrypt_text)

text = input("Text: ")
keyy = int(input("Key: "))
print(caesar(text, keyy))