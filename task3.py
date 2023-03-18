c = input().split(' ')
stroka = str()
for i in c:
    m = int(abs(float(i)))
    stroka = stroka + str(m) + ' '
print(stroka[:-1])
