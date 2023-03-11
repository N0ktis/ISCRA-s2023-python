s = list(input())
d = int(input()) % 26   #delta

for i in range(len(s)):
    tmp = d
    if s[i] == ' ':
        continue
    elif ord(s[i]) + tmp > ord('z') or ('A' <= s[i] <= 'Z') and (ord(s[i]) + tmp > ord('Z')):
        tmp -= 26
    s[i] = chr(ord(s[i]) + tmp)

s = ''.join(s)
print(s)