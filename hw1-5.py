def ceaserCipher(str, key):
    new_str = ''
    for el in str:
        new_str = new_str + chr(((ord(el) - 97 + key) % 26) + 97)
    return(new_str)

print(ceaserCipher('i am atomic', 7))
print(ceaserCipher('i am atomic', 1024))
print(ceaserCipher('abcdefghijklmnopqrstuvwxyz', 27))