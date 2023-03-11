a = input().lower()
shift = int(input())
newStr = ''
for i in a:
    newStr += chr(97 + ((ord(i) - 97) + shift) % 26)
print(newStr)
