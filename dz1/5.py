print('введите строку')
line = input()
print('введите цифровой ключ')
key = int(input())

print("".join([chr(97 + (ord(symbol) + key) % 26) for symbol in line.replace(" ", "")]))
