text = input().replace(' ','')
shift = int(input())
result = ''
97 - 122
for letter in text:
    result += chr((ord(letter)+(shift % 26)) % 122)
print(result)
