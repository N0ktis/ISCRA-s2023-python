# 5 task

line = input()
key = int(input())
res = ''
for x in line:
    # res += chr((ord(x) + key) % 26)
    res += chr((ord(x) - ord('a') + key) % 26 + ord('a'))
print(res)
