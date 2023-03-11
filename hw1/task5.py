inpline = input()
delta = int(input())
outline = ''
for i in inpline:
    outline += chr((ord(i) - ord('a') + delta) % 26 + ord('a'))
print(outline)