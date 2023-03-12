text = input().replace(' ','')
shift = int(input())
result = ''
for letter in text:
    result += chr((ord(letter)+shift) % 122)
print(result)