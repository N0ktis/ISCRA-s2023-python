print('введите строку')
line = input()
print('введите цифровой ключ')
key = int(input())

print("".join([chr(ord('a') + (ord(symbol) - ord('a') + key) % 26) for symbol in line]))
