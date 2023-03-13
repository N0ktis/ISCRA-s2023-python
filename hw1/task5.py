offset = int(input('Enter offset: '))
inp = list(input('Enter string: ').lower())
for i in range(0, len(inp)):
     inp[i] = chr((ord(inp[i]) + offset) % 122 + (ord(inp[i]) + offset) // 122 * 96)
print(''.join(inp))
