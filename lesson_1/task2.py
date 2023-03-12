"""
Copyright 2023 aaaaaaaalesha

На стандартный поток ввода передается текст в одну строку. Далее подаются правила замены в формате "A->B".
Необходимо последовательно применить эти правила к тексту (заменить все упоминания A на B).
После каждой такой замены результат выводится в стандартный поток вывода.

>> THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
>> A->4
>> I->1
>> E->3

Out:
    THE QUICK BROWN FOX JUMPS OVER THE L4ZY DOG
    THE QU1CK BROWN FOX JUMPS OVER THE L4ZY DOG
    TH3 QU1CK BROWN FOX JUMPS OV3R TH3 L4ZY DOG
"""

MAP_SEPARATOR = '->'

# Create list to not create new immutable string after every replacement.
text = input()

while True:
    original, update = input().split(MAP_SEPARATOR)
    text = text.replace(original, update)
    print(''.join(text))
