stroka = input()
while True:
    str_sim2 = str()
    a = ''
    a = input()
    if a == '':
        break
    sim1, sim2 = a.split('->')[0], a.split('->')[1]
    for i in stroka:
        if  i == sim1:
            str_sim2 = str_sim2 + sim2
        else:
            str_sim2 = str_sim2 + i  
    stroka = str_sim2
    print(stroka)
