s = input().replace(" ", "")
num = int(input())

alp = 'abcdefghijklmnopqrstuvwxyz'

res = ''
len_alp = len(alp)

for i in s:
    res += alp[(alp.find(i)+num) % len_alp]

print(res)