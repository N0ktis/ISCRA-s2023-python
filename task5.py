alfavit = "abcdefghijklmnopqrstuvwxyz"
a = input().split(' ')
kod = int(input())
b = ''.join(a)
stroka = str()
for i in b:
    k = 0
    for j in alfavit:
        if i == j:
            if k + kod >= len(alfavit):
                stroka = stroka + alfavit[k+kod-26]
            else:
                stroka = stroka + alfavit[k+kod]
        else:
            pass
        k += 1
print(stroka)
