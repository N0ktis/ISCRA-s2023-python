"""
## Задача 2

На стандартный поток ввода передается текст в одну строку. Далее подаются правила замены в формате "A->B".  
Необходимо последовательно применить эти правила к тексту (заменить все упоминания A на B).  
После каждой такой замены результат выводится в стандартный поток вывода.  

**Пример:**

Ввод:
```
THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
A->4
I->1
E->3
```
Вывод:
```
THE QUICK BROWN FOX JUMPS OVER THE L4ZY DOG
THE QU1CK BROWN FOX JUMPS OVER THE L4ZY DOG
TH3 QU1CK BROWN FOX JUMPS OV3R TH3 L4ZY DOG
```

Для данной задачи необходимо ознакомиться с работой цикла `while`. В частности, использовать цикл вида `while True`.
"""

inp = input()
while True:
    rule = input().split("->")
    inp = inp.replace(rule[0],rule[-1])
    print(inp)
