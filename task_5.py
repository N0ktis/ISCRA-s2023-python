s = input().lower()
s = s.replace(' ', '')
print(s)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input())
s_new = ''
for i in range(len(s)):
    s_new += alphabet[(alphabet.index(s[i]) + key) % 26]
print(s_new)