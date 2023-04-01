alfavit = "abcdefghijklmnopqrstuvwxyz"
a = input().split(' ')
kod = int(input())
b = ''.join(a)
stroka = ''
for i in b:
    index = alfavit.find(i)
    k = index + kod
    while k >= len(alfavit):
        k = k - len(alfavit)
    stroka = stroka + alfavit[k]
print(stroka))
