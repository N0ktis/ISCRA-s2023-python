string = input()
key = int(input())
result = ''
for letter in string:
    result = result + chr(((ord(letter) + key - 97) % 26) + 97)
print(result)
