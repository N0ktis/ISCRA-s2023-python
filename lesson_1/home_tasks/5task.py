a = input().lower()
shift = int(input())
newStr = ''
for i in a:
    if ord(i) + shift <= 122:
        newStr += chr(ord(i) + shift)
    else:
        newStr += chr(96 + (shift - (ord('z') - ord(i))))

print(newStr)

a = ''
for i in newStr:
    if ord(i) - shift >= 97:
        a += chr(ord(i) - shift)
    else:
        a += chr(123 - (shift - (ord(i) - ord('a'))))
a = a.replace(':', ' ')
print(f'decoded \n{a}')