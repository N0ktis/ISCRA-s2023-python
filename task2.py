sim1, sim2 = input().split('->')[0], input().split('->')[-1]
stroka = str()
for i in a:
    if sim1 == i:
        stroka = stroka + sim2
    else:
        stroka = stroka + i   
print(stroka)
