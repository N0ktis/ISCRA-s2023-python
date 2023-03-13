"""
## Задача 3

На стандартном потоке ввода задаётся последовательность целых чисел.
На стандартный поток вывода выведите модули целых частей этих чисел.

**Пример:**

|Ввод|Вывод|
|-|-|
|```0.23 0 -12 5 -7.11 2```|```0 0 12 5 7 2```|
"""

inp = input()

print([abs(int(float(x))) for x in inp.split()])
#print(list(map(abs, map(int, map(float, inp.split())))))
#print(list(map(lambda x : abs(int(float(x))),inp.split())))
