a = input()
n = int(input())
for b in a:
    b = chr(ord(b)+n)
    print(b, sep='', end='')