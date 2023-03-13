"""
## Задача 5

В стандартный поток ввода передается текст в одну строку. Далее следует целое число - ключ шифрования.
Выведете результат шифрования строки шифром Цезаря для данной строки и ключа.

**Пример:**

Ввод:
```
i am atomic
7
```
Вывод:
```
puhtuhavtpj
"""

inp = input().lower().split()
shift = int(input())
outp = []
for word in inp:
    outp.append("".join([ chr(97 + (((ord(ch) + shift) % 123)) % 97 ) for ch in word]))
print(" ".join(outp))
