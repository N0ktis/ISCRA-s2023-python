s = input()
flag = True
while flag:
    print("Введите замену: ")
    l = input().split('->')
    s = s.replace(l[0], l[1])
    print(s)
    print("Продолжить?(Да/Нет): ")
    if input() == "Нет":
        flag = False