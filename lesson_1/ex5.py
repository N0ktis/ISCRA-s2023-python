s = ''.join(input().split())
n = int(input())
newS = ''
for i in s:
    newS += chr(97 + ((ord(i) % 97 + n) % 26))
print(newS)