print('введите строку. будет произведена замена букв по своим правилам')
line = input()
print('вводите правила через ->')
while True:
    rule = input().split('->')
    if len(rule) != 2:
        print('вводите правила правильно')
        continue
    line = line.replace(rule[0], rule[1])
    print(line)
